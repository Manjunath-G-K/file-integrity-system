# utils/aws_utils.py — S3 + DynamoDB helpers

import io
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timezone

import config


# ── Shared boto3 session ─────────────────────────────────────────

def _session():
    """Build a boto3 session using credentials from config."""
    kwargs = {"region_name": config.AWS_REGION}
    if config.AWS_ACCESS_KEY and config.AWS_SECRET_KEY:
        kwargs["aws_access_key_id"]     = config.AWS_ACCESS_KEY
        kwargs["aws_secret_access_key"] = config.AWS_SECRET_KEY
    return boto3.Session(**kwargs)


def _s3():
    return _session().client("s3")


def _dynamodb():
    return _session().resource("dynamodb")


# ── S3 helpers ───────────────────────────────────────────────────

def upload_file_to_s3(file_data: bytes, filename: str) -> dict:
    """
    Upload raw bytes to S3.

    Args:
        file_data: File content as bytes.
        filename:  Key / object name to use in S3.

    Returns:
        {"success": True, "s3_key": filename}
        {"success": False, "error": <message>}
    """
    try:
        s3 = _s3()
        s3.upload_fileobj(
            io.BytesIO(file_data),
            config.S3_BUCKET_NAME,
            filename,
        )
        return {"success": True, "s3_key": filename}
    except ClientError as exc:
        return {"success": False, "error": str(exc)}


def get_file_from_s3(filename: str) -> dict:
    """
    Download a file from S3 and return its bytes.

    Args:
        filename: S3 object key.

    Returns:
        {"success": True, "data": <bytes>}
        {"success": False, "error": <message>}
    """
    try:
        s3  = _s3()
        buf = io.BytesIO()
        s3.download_fileobj(config.S3_BUCKET_NAME, filename, buf)
        buf.seek(0)
        return {"success": True, "data": buf.read()}
    except ClientError as exc:
        code = exc.response["Error"]["Code"]
        if code in ("NoSuchKey", "404"):
            return {"success": False, "error": f"File '{filename}' not found in S3."}
        return {"success": False, "error": str(exc)}


def delete_file_from_s3(filename: str) -> dict:
    """Delete a file from S3 (optional utility)."""
    try:
        _s3().delete_object(Bucket=config.S3_BUCKET_NAME, Key=filename)
        return {"success": True}
    except ClientError as exc:
        return {"success": False, "error": str(exc)}


# ── DynamoDB helpers ─────────────────────────────────────────────

def save_metadata_to_db(filename: str, file_hash: str, file_size: int) -> dict:
    """
    Store file metadata (name, hash, size, timestamp) in DynamoDB.

    Args:
        filename:  The original file name (used as partition key).
        file_hash: SHA-256 hex digest.
        file_size: File size in bytes.

    Returns:
        {"success": True}
        {"success": False, "error": <message>}
    """
    try:
        table = _dynamodb().Table(config.DYNAMODB_TABLE)
        table.put_item(Item={
            "filename":   filename,
            "hash":       file_hash,
            "size":       file_size,
            "uploaded_at": datetime.now(timezone.utc).isoformat(),
        })
        return {"success": True}
    except ClientError as exc:
        return {"success": False, "error": str(exc)}


def get_metadata_from_db(filename: str) -> dict:
    """
    Retrieve stored metadata for a given file.

    Args:
        filename: The file name (partition key).

    Returns:
        {"success": True, "item": {filename, hash, size, uploaded_at}}
        {"success": False, "error": <message>}
    """
    try:
        table    = _dynamodb().Table(config.DYNAMODB_TABLE)
        response = table.get_item(Key={"filename": filename})
        item     = response.get("Item")
        if not item:
            return {"success": False, "error": f"No record found for '{filename}'."}
        return {"success": True, "item": item}
    except ClientError as exc:
        return {"success": False, "error": str(exc)}


def list_files_in_db(limit: int = 50) -> dict:
    """
    List all tracked files from DynamoDB (scan, for small tables).

    Returns:
        {"success": True, "items": [...]}
        {"success": False, "error": <message>}
    """
    try:
        table    = _dynamodb().Table(config.DYNAMODB_TABLE)
        response = table.scan(Limit=limit)
        return {"success": True, "items": response.get("Items", [])}
    except ClientError as exc:
        return {"success": False, "error": str(exc)}