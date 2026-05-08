<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="140"/>

# FILEGUARD X

### ⚡ AI-Ready Cloud File Integrity & Tamper Detection Platform

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=900&lines=SHA-256+Cryptographic+Verification;AWS+Cloud-Native+Architecture;Real-Time+Tamper+Detection;Built+with+Flask+%2B+Amazon+S3+%2B+DynamoDB;Cloud+Computing+Laboratory+Project" />

<br/>

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazonaws"/>
<img src="https://img.shields.io/badge/Amazon_S3-Storage-FF9900?style=for-the-badge&logo=amazons3"/>
<img src="https://img.shields.io/badge/DynamoDB-NoSQL-4053D6?style=for-the-badge&logo=amazondynamodb"/>
<img src="https://img.shields.io/badge/SHA--256-Secure-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/STATUS-ACTIVE-00ff99?style=for-the-badge"/>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0f0f,100:00F7FF&height=120&section=header&text=UPLOAD%20%E2%86%92%20VERIFY%20%E2%86%92%20DETECT&fontSize=30&fontColor=ffffff&animation=fadeIn"/>

</div>

---

# 🌌 Overview

**FileGuard X** is a futuristic cloud-native cybersecurity platform that verifies whether a file has been modified, corrupted, or tampered with after upload.

The system uses:

- 🔐 **SHA-256 cryptographic hashing**
- ☁️ **Amazon S3 cloud object storage**
- ⚡ **Amazon DynamoDB ultra-fast metadata storage**
- 🖥️ **Flask backend architecture**
- 🌐 **Interactive browser-based UI**

Even a **single-bit modification** creates a completely different fingerprint.

That means tampering becomes instantly detectable.

---

# ⚡ Core Concept

```text
UPLOAD FILE
     │
     ▼
GENERATE SHA-256 HASH
     │
     ▼
STORE FILE IN AMAZON S3
     │
     ▼
STORE HASH IN DYNAMODB
     │
────────────────────────────
     │
VERIFY FILE LATER
     │
     ▼
DOWNLOAD FILE FROM S3
     │
     ▼
GENERATE NEW HASH
     │
     ▼
COMPARE BOTH HASHES
     │
 ┌──────────────┐
 │ HASH MATCH ? │
 └──────┬───────┘
        │
   YES  │  NO
        │
        ▼
  ✅ INTACT
  ❌ TAMPERED
```

---

# 🌍 Real World Applications

| Industry | Use Case |
|---|---|
| 🏥 Healthcare | Verify medical reports are unchanged |
| 🏦 Banking | Protect financial documents |
| 🎓 Universities | Prevent modification of student records |
| ⚖️ Legal Systems | Preserve digital evidence integrity |
| 🏢 Enterprises | Monitor sensitive cloud files |
| ☁️ Cloud Storage | Detect unauthorized file replacement |

---

# 🧠 How It Works

## 📤 Upload Engine

When the user uploads a file:

1. Flask backend receives the file
2. SHA-256 fingerprint generated
3. File stored securely in Amazon S3
4. Hash + metadata stored in DynamoDB
5. System returns verification-ready status

---

## 🔍 Verification Engine

When verification starts:

1. File downloaded from S3
2. New SHA-256 hash generated
3. Stored hash fetched from DynamoDB
4. Both hashes compared securely
5. Final result displayed:

```text
✅ INTACT     → File is safe
❌ TAMPERED  → File modified
```

---

# 🏗️ Cloud Architecture

```text
┌───────────────────────────────┐
│        Frontend Layer         │
│ HTML • CSS • JavaScript       │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│         Flask Backend         │
│            app.py             │
└───────┬───────────┬───────────┘
        │           │
        ▼           ▼
┌─────────────┐ ┌────────────────┐
│ Amazon S3  │ │ Amazon DynamoDB│
│ File Store │ │ Hash Metadata  │
└─────────────┘ └────────────────┘
```

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon EC2 | Hosts Flask application |
| Amazon S3 | Stores uploaded files |
| DynamoDB | Stores SHA-256 hashes |
| IAM | Secure permissions |
| Security Groups | Firewall access control |
| SSH | Secure remote EC2 access |

---

# 🛡️ Security Features

### 🔐 SHA-256 Cryptographic Fingerprinting

Industry-standard irreversible hashing algorithm.

---

### ⚡ Timing-Safe Comparison

Uses secure comparison methods to prevent timing attacks.

---

### ☁️ Cloud Storage Isolation

Files and metadata stored separately for enhanced protection.

---

### 🧼 Secure Filename Sanitization

Prevents malicious file path injection attacks.

---

### 🔑 Environment Variable Protection

AWS credentials are never hardcoded into source files.

---


# 💻 Terminal Execution

```bash
$ python app.py

 * Serving Flask app 'FileGuard X'
 * Running on http://127.0.0.1:5000

[SYSTEM] Uploading report.pdf...

✓ SHA-256 Fingerprint Generated
✓ File Stored in Amazon S3
✓ Metadata Saved in DynamoDB

[SYSTEM] Starting Verification...

✓ Downloaded File from S3
✓ Recomputed SHA-256 Hash
✓ Comparing Fingerprints...

RESULT:
✓ INTACT
```

---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/file-integrity-system.git
cd file-integrity-system
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env`

```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
S3_BUCKET_NAME=your_bucket_name
DYNAMODB_TABLE=FileIntegrityMetadata
FLASK_SECRET_KEY=your_secret_key
```

---

## Run Application

```bash
python app.py
```

---

# ☁️ EC2 Deployment Commands

## Connect to EC2

```bash
ssh -i file-integrity-key.pem ubuntu@18.208.193.44
```

---

## Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## Open Project Directory

```bash
cd file-integrity-system
```

---

## Run Flask Server

```bash
python app.py
```

---

# 📂 Project Structure

```text
file-integrity-system/
│
├── app.py
├── config.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── utils/
    ├── hash_utils.py
    └── aws_utils.py
```

---

# 🚀 Future Scope

- 🔔 Email alert system
- 👤 User authentication
- 📊 Analytics dashboard
- 🔄 Automatic scheduled verification
- 🔐 AES-256 encryption
- ☁️ Multi-cloud support
- 📱 Mobile optimization
- 🤖 AI-powered anomaly detection

---

# 👨‍💻 Author

<div align="center">

# Manjunath G K

### Cloud Computing Laboratory — BCS 601

### Guided By:
## Prof. Mohan K

University BDT College of Engineering

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:0f0f0f&height=120&section=footer"/>

</div>
