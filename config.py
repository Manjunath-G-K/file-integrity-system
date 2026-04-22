# config.py — Central configuration for the File Integrity System

import os

# ── AWS Settings ────────────────────────────────────────────────
AWS_REGION        = os.environ.get("AWS_REGION", "ap-south-1")
AWS_ACCESS_KEY    = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_KEY    = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

# ── S3 ──────────────────────────────────────────────────────────
S3_BUCKET_NAME    = os.environ.get("S3_BUCKET_NAME", "file-integrity-bucket")

# ── DynamoDB ────────────────────────────────────────────────────
DYNAMODB_TABLE    = os.environ.get("DYNAMODB_TABLE", "FileIntegrityMetadata")

# ── Flask ────────────────────────────────────────────────────────
SECRET_KEY        = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-in-prod")
MAX_CONTENT_MB    = 50          # max upload size in megabytes
ALLOWED_EXTENSIONS = {          # accepted file types
    "txt", "pdf", "png", "jpg",
    "jpeg", "csv", "json", "xml",
    "zip", "docx", "xlsx",
}