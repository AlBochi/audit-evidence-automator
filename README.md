# 🧾 Audit Evidence Automator

**Author**: Al Bochi, Cloud Security Compliance Lead at Saillent

---

## 📌 Overview

`audit-evidence-automator` is a powerful automation tool designed to simplify and accelerate the audit evidence collection process for cloud security compliance. It automatically captures live screenshots, generates professional PDF evidence reports, and bundles them into audit-ready packages aligned with frameworks like **SOC 2**, **HIPAA**, and **ISO 27001**.

---

## ✅ Features

- Automated capture of live cloud console screenshots using Selenium  
- Dynamic generation of detailed HTML and PDF compliance reports  
- Support for multiple compliance frameworks via customizable control templates  
- Bundles all evidence into a single ZIP file for easy sharing with auditors and stakeholders  

---

## 🚀 Quick Start

### Prerequisites:

```bash
sudo apt update
sudo apt install -y wkhtmltopdf python3-pip xvfb
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
