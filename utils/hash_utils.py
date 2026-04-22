# utils/hash_utils.py — SHA-256 hashing helpers

import hashlib
import io


def compute_hash(file_data: bytes) -> str:
    """
    Compute the SHA-256 hash of raw bytes.

    Args:
        file_data: The file content as bytes.

    Returns:
        Lowercase hex-encoded SHA-256 digest string.
    """
    sha256 = hashlib.sha256()
    sha256.update(file_data)
    return sha256.hexdigest()


def compute_hash_from_stream(stream, chunk_size: int = 8192) -> str:
    """
    Compute SHA-256 by reading a file-like object in chunks.
    Memory-efficient for large files.

    Args:
        stream:     A readable binary stream (e.g. file object, BytesIO).
        chunk_size: Number of bytes to read per iteration.

    Returns:
        Lowercase hex-encoded SHA-256 digest string.
    """
    sha256 = hashlib.sha256()
    stream.seek(0)                          # always start from the beginning
    while True:
        chunk = stream.read(chunk_size)
        if not chunk:
            break
        sha256.update(chunk)
    stream.seek(0)                          # reset for any subsequent reads
    return sha256.hexdigest()


def hashes_match(hash_a: str, hash_b: str) -> bool:
    """
    Constant-time comparison of two hash strings to prevent timing attacks.

    Args:
        hash_a: First hash.
        hash_b: Second hash.

    Returns:
        True if identical, False otherwise.
    """
    import hmac
    return hmac.compare_digest(hash_a.lower(), hash_b.lower())