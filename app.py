# app.py — Main Flask application for File Integrity System

from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import config
from utils.hash_utils import compute_hash, hashes_match
from utils.aws_utils  import (
    upload_file_to_s3,
    get_file_from_s3,
    save_metadata_to_db,
    get_metadata_from_db,
    list_files_in_db,
)

# ── App setup ────────────────────────────────────────────────────

app = Flask(__name__)
app.secret_key             = config.SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = config.MAX_CONTENT_MB * 1024 * 1024


def allowed_file(filename: str) -> bool:
    """Return True if the file extension is permitted."""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in config.ALLOWED_EXTENSIONS
    )


# ── Routes ───────────────────────────────────────────────────────

@app.route("/")
def index():
    """Render the main UI page."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """
    Upload a file:
      1. Receive file from form
      2. Compute SHA-256 hash
      3. Store file in S3
      4. Save metadata (hash, size) in DynamoDB
      5. Return result JSON
    """
    if "file" not in request.files:
        return jsonify({"success": False, "error": "No file part in request."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"success": False, "error": "No file selected."}), 400

    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "error":   f"File type not allowed. Permitted: {', '.join(config.ALLOWED_EXTENSIONS)}"
        }), 400

    filename  = secure_filename(file.filename)
    file_data = file.read()
    file_hash = compute_hash(file_data)
    file_size = len(file_data)

    # ── Upload to S3 ─────────────────────────────────
    s3_result = upload_file_to_s3(file_data, filename)
    if not s3_result["success"]:
        return jsonify({"success": False, "error": f"S3 upload failed: {s3_result['error']}"}), 500

    # ── Save metadata to DynamoDB ─────────────────────
    db_result = save_metadata_to_db(filename, file_hash, file_size)
    if not db_result["success"]:
        return jsonify({"success": False, "error": f"DB save failed: {db_result['error']}"}), 500

    return jsonify({
        "success":   True,
        "message":   "File uploaded successfully.",
        "filename":  filename,
        "hash":      file_hash,
        "size":      file_size,
        "size_kb":   round(file_size / 1024, 2),
    })


@app.route("/verify", methods=["POST"])
def verify():
    """
    Verify file integrity:
      1. Receive filename from form
      2. Fetch stored hash from DynamoDB
      3. Download file from S3
      4. Recompute hash
      5. Compare → return INTACT or TAMPERED
    """
    data     = request.get_json(silent=True) or request.form
    filename = data.get("filename", "").strip()

    if not filename:
        return jsonify({"success": False, "error": "Filename is required."}), 400

    filename = secure_filename(filename)

    # ── Get stored hash ───────────────────────────────
    db_result = get_metadata_from_db(filename)
    if not db_result["success"]:
        return jsonify({"success": False, "error": db_result["error"]}), 404

    stored_hash = db_result["item"]["hash"]
    uploaded_at = db_result["item"].get("uploaded_at", "N/A")

    # ── Download file from S3 ─────────────────────────
    s3_result = get_file_from_s3(filename)
    if not s3_result["success"]:
        return jsonify({"success": False, "error": s3_result["error"]}), 404

    # ── Recompute hash ────────────────────────────────
    current_hash = compute_hash(s3_result["data"])

    # ── Compare ───────────────────────────────────────
    intact = hashes_match(stored_hash, current_hash)
    status = "INTACT" if intact else "TAMPERED"

    return jsonify({
        "success":      True,
        "filename":     filename,
        "status":       status,
        "intact":       intact,
        "stored_hash":  stored_hash,
        "current_hash": current_hash,
        "uploaded_at":  uploaded_at,
    })


@app.route("/files", methods=["GET"])
def list_files():
    """List all tracked files from DynamoDB."""
    result = list_files_in_db()
    if not result["success"]:
        return jsonify({"success": False, "error": result["error"]}), 500
    return jsonify({"success": True, "files": result["items"]})


# ── Error handlers ───────────────────────────────────────────────

@app.errorhandler(413)
def file_too_large(_):
    return jsonify({
        "success": False,
        "error":   f"File too large. Maximum size is {config.MAX_CONTENT_MB} MB."
    }), 413


@app.errorhandler(404)
def not_found(_):
    return jsonify({"success": False, "error": "Route not found."}), 404


# ── Entry point ──────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)