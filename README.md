<div align="center">

```
███████╗██╗██╗     ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
██╔════╝██║██║     ██╔════╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
█████╗  ██║██║     █████╗  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██╔══╝  ██║██║     ██╔══╝  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
██║     ██║███████╗███████╗╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
```

# ⬡ FileGuard: Cloud-Based File Integrity Monitoring System

<br/>

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![AWS S3](https://img.shields.io/badge/Amazon_S3-Storage-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3)
[![DynamoDB](https://img.shields.io/badge/DynamoDB-Database-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)](https://aws.amazon.com/dynamodb)
[![SHA-256](https://img.shields.io/badge/SHA--256-Hashing-1D6A3A?style=for-the-badge&logo=security&logoColor=white)](#)
[![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

> **Upload once. Fingerprint forever. Know instantly if your files have been tampered with.**

<br/>

---

</div>

## 🎯 Overview

**FileGuard** is a modern cloud-native web application that detects file **modification, corruption, and tampering** in real-time without any additional tools or agents. 

Using **SHA-256 cryptographic fingerprinting**, FileGuard computes a unique digital signature for each uploaded file. Store this signature once, then verify anytime—if even a single byte changes, FileGuard instantly alerts you.

```
One-Click Verification:  ✓  INTACT   →  File is safe, unchanged
                         ✗  TAMPERED →  File has been modified
```

---

## ⚡ Key Features

| Feature | Benefit |
|---------|---------|
| 🔒 **SHA-256 Fingerprinting** | Industry-standard cryptographic hashing—detects even 1-byte changes |
| ☁️ **AWS S3 Integration** | Secure cloud storage with automatic backup and reliability |
| 🗄️ **DynamoDB Metadata** | Lightning-fast NoSQL database for hash lookups and file tracking |
| ⚡ **Instant Verification** | Verify any file in seconds from anywhere with internet access |
| 🎨 **Modern Dark UI** | Clean, intuitive web interface with drag-and-drop support |
| 📊 **Dashboard & Insights** | View all tracked files, hashes, sizes, and upload timestamps in one table |
| 🛡️ **Security First** | Timing-safe comparison, filename sanitization, type allowlist |
| 🔧 **Modular Architecture** | Clean separation of concerns—easy to extend and maintain |

---

## 🏗️ System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                   Frontend (Browser)                       │
│            HTML5 · CSS3 · Vanilla JavaScript               │
│         Drag-drop upload · Real-time verification          │
└─────────────────────┬──────────────────────────────────────┘
                      │ HTTP/JSON
                      ▼
┌────────────────────────────────────────────────────────────┐
│              Flask REST API Backend                         │
│  ┌──────────────────┐      ┌──────────────────────────┐    │
│  │   /upload        │      │    /verify               │    │
│  │   /verify        │  ←→  │    /files                │    │
│  │   /files         │      │    Middleware            │    │
│  └──────────────────┘      └──────────────────────────┘    │
│           │                         │                      │
│    ┌──────▼──────┐          ┌───────▼─────────┐            │
│    │ hash_utils  │          │   aws_utils     │            │
│    │ SHA-256     │          │ boto3 client    │            │
│    └─────────────┘          └─────────────────┘            │
└─────────────────────┬──────────────────────────────────────┘
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
    ┌─────────────┐         ┌──────────────────┐
    │  Amazon S3  │         │  DynamoDB        │
    │             │         │                  │
    │  File Store │         │  Metadata Store  │
    │  (Durable)  ��         │  (Fast Lookups)  │
    └─────────────┘         └──────────────────┘
         ▲                         ▲
         │                         │
         └────────────┬────────────┘
                      │
        ┌─────────────▼──────────┐
        │  ✓ INTACT  or  ✗ TAMPERED
        │  Hash comparison result
        └────────────────────────┘
```

---

## 📋 Project Structure

```
file-integrity-system/
│
├── 📄 app.py                    # Main Flask application (routes & logic)
├── 📄 config.py                 # Configuration & environment setup
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # This file
├── 📄 .env.example               # Environment variables template
│
├── 📁 templates/
│   └── index.html               # Frontend UI (upload, verify, file list)
│
├── 📁 static/
│   └── style.css                # Modern dark theme stylesheet
│
└── 📁 utils/
    ├── __init__.py
    ├── hash_utils.py            # SHA-256 hashing logic
    └── aws_utils.py             # S3 & DynamoDB communication (boto3)
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **AWS Account** with:
  - S3 bucket created
  - DynamoDB table: `FileIntegrityMetadata`
  - IAM user with S3 & DynamoDB permissions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Manjunath-G-K/file-integrity-system.git
cd file-integrity-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

Create a `.env` file:

```env
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
S3_BUCKET_NAME=your-bucket-name
DYNAMODB_TABLE=FileIntegrityMetadata

# Flask Configuration
FLASK_SECRET_KEY=your-random-secret-key-here
FLASK_ENV=development
```

> ⚠️ **Security:** Add `.env` to `.gitignore` — never commit credentials!

### 4️⃣ Run Application

```bash
python app.py
```

Open browser: **http://localhost:5000**

---

## ☁️ AWS Setup

### Create S3 Bucket

```bash
aws s3 mb s3://your-bucket-name --region us-east-1
```

### Create DynamoDB Table

```bash
aws dynamodb create-table \
  --table-name FileIntegrityMetadata \
  --attribute-definitions AttributeName=filename,AttributeType=S \
  --key-schema AttributeName=filename,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

**DynamoDB Schema:**

| Attribute | Type | Purpose |
|-----------|------|---------|
| `filename` | String (PK) | Unique identifier |
| `hash` | String | SHA-256 hex digest |
| `size` | Number | File size in bytes |
| `uploaded_at` | String | ISO 8601 timestamp |

---

## 🔄 How It Works

### Upload Flow

```
1. User selects file
   ↓
2. Flask /upload route receives file
   ↓
3. hash_utils.compute_hash() → SHA-256 fingerprint
   ↓
4. aws_utils.upload_file_to_s3() → File stored in S3
   ↓
5. aws_utils.save_metadata_to_db() → Hash + metadata → DynamoDB
   ↓
6. JSON response with hash, size, timestamp
```

### Verification Flow

```
1. User requests verification of filename
   ↓
2. Flask /verify route processes request
   ↓
3. aws_utils.get_metadata_from_db() → Retrieve stored hash
   ↓
4. aws_utils.get_file_from_s3() → Download current file
   ↓
5. hash_utils.compute_hash() → Recompute current hash
   ↓
6. hash_utils.hashes_match() → Constant-time comparison
   ↓
7. Return ✓ INTACT or ✗ TAMPERED
```

---

## 📡 API Endpoints

### POST `/upload`
Upload a file for integrity tracking.

**Request:**
```
multipart/form-data with "file" field
```

**Response (200):**
```json
{
  "success": true,
  "message": "File uploaded successfully",
  "filename": "document.pdf",
  "hash": "a3f9b2c7d1e4f8a9b2c7d1e4f8a9...",
  "size": 245760,
  "size_kb": 240.0
}
```

---

### POST `/verify`
Verify a file's integrity.

**Request:**
```json
{
  "filename": "document.pdf"
}
```

**Response (INTACT - 200):**
```json
{
  "success": true,
  "filename": "document.pdf",
  "status": "INTACT",
  "intact": true,
  "stored_hash": "a3f9b2c7d1e4f8a9...",
  "current_hash": "a3f9b2c7d1e4f8a9...",
  "uploaded_at": "2025-05-08T10:30:00Z"
}
```

**Response (TAMPERED - 200):**
```json
{
  "success": true,
  "filename": "document.pdf",
  "status": "TAMPERED",
  "intact": false,
  "stored_hash": "a3f9b2c7d1e4f8a9...",
  "current_hash": "d9e1f456789abcde...",
  "uploaded_at": "2025-05-08T10:30:00Z"
}
```

---

### GET `/files`
Retrieve list of all tracked files.

**Response (200):**
```json
{
  "success": true,
  "files": [
    {
      "filename": "document.pdf",
      "hash": "a3f9b2c7...",
      "size": 245760,
      "uploaded_at": "2025-05-08T10:30:00Z"
    },
    {
      "filename": "archive.zip",
      "hash": "b4g8c3d9...",
      "size": 1048576,
      "uploaded_at": "2025-05-08T11:15:00Z"
    }
  ]
}
```

---

## 🔐 Security Features

| Feature | Implementation |
|---------|-----------------|
| **Cryptographic Hashing** | SHA-256 (256-bit, one-way, irreversible) |
| **Timing-Safe Comparison** | `hmac.compare_digest()` prevents timing attacks |
| **Path Traversal Protection** | `werkzeug.utils.secure_filename()` sanitization |
| **File Type Validation** | Allowlist of safe file extensions |
| **Credential Management** | Environment variables only (never hardcoded) |
| **HTTPS Ready** | Flask can run behind SSL proxy |
| **CORS Ready** | Configurable cross-origin requests |

---

## 🧪 Testing

| # | Scenario | Action | Expected | Status |
|---|----------|--------|----------|--------|
| 1 | Upload valid file | POST /upload with PDF | Stored in S3 & DynamoDB | ✅ |
| 2 | Immediate verification | POST /verify after upload | INTACT response | ✅ |
| 3 | Tamper detection | Modify file in S3, then verify | TAMPERED response | ✅ |
| 4 | Missing file | Verify non-existent file | Error message | ✅ |
| 5 | Large file | Upload 20 MB+ file | Successful upload | ✅ |
| 6 | File listing | GET /files | All files displayed | ✅ |

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0+ | Web framework |
| boto3 | 1.34+ | AWS SDK |
| Werkzeug | 3.0+ | WSGI utilities & security |
| python-dotenv | 1.0+ | Environment loading |

Install all:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuration

**Environment Variables:**

| Variable | Required | Example |
|----------|----------|---------|
| `AWS_REGION` | Yes | `us-east-1` |
| `AWS_ACCESS_KEY_ID` | Yes | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Yes | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `S3_BUCKET_NAME` | Yes | `my-integrity-bucket` |
| `DYNAMODB_TABLE` | Yes | `FileIntegrityMetadata` |
| `FLASK_SECRET_KEY` | Yes | `your-secret-key-min-32-chars` |
| `FLASK_ENV` | No | `development` or `production` |

---

## 🚀 Future Enhancements

- [ ] **User Authentication** — Login & per-user file isolation
- [ ] **Email Notifications** — Alert owner when tampering detected
- [ ] **Auto-Verification** — Scheduled hourly/daily integrity checks
- [ ] **Version History** — Track all previous hashes per file
- [ ] **Batch Operations** — Upload & verify multiple files
- [ ] **Admin Dashboard** — Charts, statistics, activity logs
- [ ] **File Encryption** — AES-256 encryption before upload
- [ ] **Multi-Cloud** — Support for GCS and Azure Blob
- [ ] **API Keys** — Token-based access control
- [ ] **Webhooks** — Notify external systems on tampering

---

## 🏆 Technologies

```
Backend:       Python, Flask, boto3
Cloud:         AWS S3, DynamoDB
Security:      SHA-256, HMAC, secure-filename
Frontend:      HTML5, CSS3, Fetch API
DevOps:        Docker-ready, environment-based config
```

---

## 📄 License

MIT License — See [LICENSE](LICENSE) file for details.

```
Copyright (c) 2025 Manjunath G K

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files to deal in
the software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the software.
```

---

## 👨‍💼 Author

<div align="center">

**Manjunath G K**

*Department of Computer Science & Engineering*  
*University BDT College of Engineering, Davanagere – 577004*  
*Constituent College of Visvesvaraya Technological University, Belagavi*

**Subject:** Cloud Computing Laboratory — **BCS 601**  
**Guide:** Prof. Mohan K, Assistant Professor, Dept. of CSE  
**Batch:** 2024–2025

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via Issues
- Suggest features via Discussions
- Submit Pull Requests for improvements

---

## 📞 Support

For questions or issues:
1. Check [existing issues](../../issues)
2. Review [API documentation](#-api-endpoints)
3. Consult [AWS setup guide](#-aws-setup)

---

<div align="center">

### ⬡ FileGuard

**Upload once. Verify forever.**

Built with ❤️ for Cloud Computing Laboratory  
*Flask · SHA-256 · Amazon S3 · DynamoDB · Python*

![FileGuard](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green?style=flat-square)

</div>
