<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="150"/>

# FILEGUARD 

### ⚡ Next-Generation Cloud File Integrity & Tamper Detection System

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=24&pause=1000&color=00F7FF&center=true&vCenter=true&width=950&lines=Cloud-Native+Cybersecurity+Platform;SHA-256+Integrity+Verification;Amazon+S3+%2B+DynamoDB+Powered;Detect+Tampered+Files+Instantly;Built+for+Cloud+Computing+Laboratory" />

<br/>

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazonaws"/>
<img src="https://img.shields.io/badge/Amazon_S3-Object_Storage-FF9900?style=for-the-badge&logo=amazons3"/>
<img src="https://img.shields.io/badge/DynamoDB-NoSQL_Database-4053D6?style=for-the-badge&logo=amazondynamodb"/>
<img src="https://img.shields.io/badge/SHA--256-Cryptographic_Security-00C853?style=for-the-badge"/>
<img src="https://img.shields.io/badge/STATUS-LIVE-00E5FF?style=for-the-badge"/>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&text=UPLOAD%20•%20VERIFY%20•%20PROTECT&fontAlign=50&fontAlignY=35&color=0:0B1020,50:00F7FF,100:00FFB3&fontColor=ffffff&fontSize=34&animation=fadeIn"/>

</div>

---

# 🌌 What is FileGuard X?

**FileGuard X** is a futuristic cloud-based cybersecurity system designed to verify whether files stored in the cloud have been modified, corrupted, replaced, or tampered with.

The platform creates a unique **SHA-256 cryptographic fingerprint** for every uploaded file and securely stores it using AWS cloud services.

During verification, the file is downloaded again, re-hashed, and compared with the original fingerprint.

Even changing **1 character** inside the file creates a completely different SHA-256 hash.

That means:

```text
MATCHED HASH   →   ✅ FILE IS SAFE
DIFFERENT HASH →   ❌ FILE TAMPERED
```

---

# ⚡ Intelligent Verification Pipeline

                                                  
                              ╔════════════════════════════════════════════════════════════╗
                              ║                    FILEGUARD X ENGINE                      ║
                              ╚════════════════════════════════════════════════════════════╝
                                        
                                                📤 USER UPLOADS FILE
                                                            │
                                                            ▼
                                              ⚡ GENERATE SHA-256 FINGERPRINT
                                                            │
                                                            ▼
                                                 ☁️ STORE FILE IN AMAZON S3
                                                            │
                                                            ▼
                                              🧠 STORE HASH INSIDE DYNAMODB
                                                            │
                                                    🔍 VERIFY REQUEST
                                                            │
                                                            ▼
                                                ☁️ DOWNLOAD FILE FROM S3
                                                            │
                                                            ▼
                                               ⚡ GENERATE NEW SHA-256 HASH
                                                            │
                                                            ▼
                                                  🧠 FETCH ORIGINAL HASH
                                                            │
                                                            ▼
                                                   🔄 COMPARE BOTH HASHES
                                                            │
                                                 ┌──────────┴──────────┐
                                                 │                     │
                                                 ▼                     ▼
                                        
                                           ✅ INTACT              ❌ TAMPERED
                                           File Safe              File Modified
                                                  

---

# 🌍 Real-World Applications



| Industry | Usage |
|---|---|
| 🏥 Healthcare | Verify medical reports are unchanged |
| 🏦 Banking | Detect unauthorized modification of financial files |
| 🎓 Universities | Protect certificates and student records |
| ⚖️ Legal Systems | Maintain digital evidence integrity |
| 🏢 Enterprises | Monitor sensitive cloud documents |
| ☁️ Cloud Platforms | Detect replaced or modified uploaded files |



---

# 🏗️ Advanced Cloud Architecture

```text
                                   ┌──────────────────────────────────────────┐
                                   │              FRONTEND LAYER              │
                                   │      HTML • CSS • JavaScript UI          │
                                   └────────────────┬─────────────────────────┘
                                                    │ HTTP Requests
                                                    ▼
                                   ┌──────────────────────────────────────────┐
                                   │             FLASK BACKEND                │
                                   │                app.py                    │
                                   │                                          │
                                   │   /upload   /verify   /files             │
                                   └──────────────┬──────────────┬────────────┘
                                                  │              │
                                                  ▼              ▼
                                   
                                   ┌────────────────┐       ┌───────────────────┐
                                   │   AMAZON S3    │       │ AMAZON DYNAMODB   │
                                   │                │       │                   │
                                   │ File Storage   │       │ SHA-256 Metadata  │
                                   │ Uploaded Files │       │ File Integrity DB │
                                   └────────────────┘       └───────────────────┘
```

---

# ☁️ AWS Services Used



| AWS Service | Purpose |
|---|---|
| 🖥️ Amazon EC2 | Hosts Flask application |
| ☁️ Amazon S3 | Stores uploaded files securely |
| ⚡ DynamoDB | Stores hashes and metadata |
| 🔐 IAM | Access and permission control |
| 🌐 Security Groups | Firewall and network security |
| 💻 SSH | Secure EC2 remote access |


---

# 🛡️ Cybersecurity Features



| Feature | Protection |
|---|---|
| 🔐 SHA-256 Fingerprinting | Detects even 1-bit modification |
| ⚡ Secure Hash Comparison | Prevents timing-based attacks |
| ☁️ Storage Isolation | Separates files and metadata |
| 🧼 Filename Sanitization | Blocks malicious filenames |
| 🔑 Environment Variables | Protects AWS credentials |
| 🛡️ Tamper Detection Engine | Real-time integrity verification |
| 🧠 Modular Architecture | Secure and scalable structure |



---

# 💻 Live Terminal Execution

```bash
$ python app.py

╔══════════════════════════════════════════╗
║          FILEGUARD X INITIALIZED         ║
╚══════════════════════════════════════════╝

[✓] Flask Server Started
[✓] AWS Services Connected
[✓] S3 Bucket Ready
[✓] DynamoDB Table Active

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📤 Upload Request Received:
    File → report.pdf

⚡ Generating SHA-256 Fingerprint...
✓ Fingerprint Created Successfully

☁️ Uploading File to Amazon S3...
✓ Upload Completed

🧠 Saving Metadata to DynamoDB...
✓ Metadata Stored

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 Verification Process Started...

☁️ Downloading File from S3...
✓ File Retrieved Successfully

⚡ Recomputing SHA-256 Hash...
✓ Hash Generated

🔄 Comparing Original & Current Hash...

RESULT:
✅ INTACT — No Tampering Detected
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

## Start Application

```bash
python app.py
```

---

# ☁️ EC2 Deployment Commands

## Connect to EC2 Instance

```bash
ssh -i file-integrity-key.pem ubuntu@18.208.193.44
```

---

## Activate Python Virtual Environment

```bash
source venv/bin/activate
```

---

## Open Project Directory

```bash
cd file-integrity-system
```

---

## Run Flask Application

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

# 🚀 Future Vision



| Planned Feature | Description |
|---|---|
| 🔔 Smart Alerts | Email notifications for tampering |
| 👤 Authentication | Multi-user secure login system |
| 📊 Analytics Dashboard | File activity monitoring |
| 🔄 Auto Verification | Scheduled integrity scanning |
| 🔐 AES-256 Encryption | File encryption before upload |
| ☁️ Multi-Cloud Support | AWS + Azure + Google Cloud |
| 📱 Mobile Optimization | Responsive mobile UI |
| 🤖 AI Threat Detection | Intelligent anomaly monitoring |



---

# 👨‍💻 Author



# Manjunath G K

### Cloud Computing Laboratory — BCS 601

### Guided By

# Prof. Mohan K

University BDT College of Engineering Davanagere Karnataka - 577004

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&height=160&section=footer&color=0:00F7FF,50:0B1020,100:000000"/>
