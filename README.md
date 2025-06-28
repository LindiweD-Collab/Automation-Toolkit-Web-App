# 🚀 Automation Toolkit Web App

A fully functional **Automation Dashboard** built using **Streamlit**, designed to help users automate everyday tasks like **file renaming**, **email validation**, **CSV conversion**, and **data extraction** from **PDFs** and **images (OCR)** — all through a user-friendly web interface.

---

## 🔧 Project Overview

This toolkit showcases how automation can simplify repetitive tasks from a central web platform. It's ideal for small teams, virtual assistants, or individuals looking to boost productivity without coding.

---

## 🧰 Features

✅ Rename a batch of files and download them as a ZIP  
✅ Extract text from PDFs and images using OCR (Tesseract)  
✅ Validate email addresses  
✅ Convert CSV to Excel format  
✅ Download task logs  
✅ Send logs via email (Gmail SMTP)  
✅ Option to clear saved files and logs  
✅ Logs saved automatically per session    
  

---

## 📁 File Structure

Automation-Toolkit-Web-App/
├── app.py # Main Streamlit app
├── tasks.py # Scheduled job logic (for future automation)
├── logs/ # Saved logs (auto-created)
├── renamed_files/ # Renamed files (auto-created)
├── utils/ # Helper functions
│ ├── file_utils.py # File rename, CSV→Excel, ZIP, log
│ ├── ocr_utils.py # Image/PDF OCR
│ ├── validators.py # Email validation
│ └── email_utils.py # Send logs via email
├── requirements.txt


---

## 🖥️ Getting Started

### 1. Clone the repository

```
git clone https://github.com/LindiweD-Collab/Automation-Toolkit-Web-App.git
cd Automation-Toolkit-Web-App
```
### 2. Install dependencies
It is recommended to use a virtual environment.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Install Tesseract OCR (required for image/PDF text extraction)
On Ubuntu:
```
sudo apt update
sudo apt install tesseract-ocr
```

On Windows:
```
Download the installer from https://github.com/tesseract-ocr/tesseract

Ensure the path to the Tesseract executable is added to your system's environment variables.
```

### 🚀 Run the App
```
streamlit run app.py
Open http://localhost:8501 in your browser.
```

### ⚙️ Technologies Used
```
Python 

Streamlit 

Pandas, OpenPyXL, XlsxWriter 

PyTesseract (OCR) 

smtplib (email sender) 

Regex (email validation)
```

### ✉️ Email Log Feature (Gmail)
***To use the email log feature:***

-Go to Google App Passwords

-Generate a new app password for "Mail"

-Use that app password in the Streamlit form

⚠️ This is required if your Gmail has 2FA enabled. Your login password will not work.



### 🧼 Maintenance Features
```
✅ Option to clear old logs and renamed files after processing

📦 Automatic creation of logs/ and renamed_files/ folders

📄 Downloadable session logs with timestamps
```

### 📄 License
This project is licensed under the MIT License.
Feel free to use, fork, and contribute!


### 🧠 Author
Built by Lindiwe Thabsile Dlomo — Passionate about automation, productivity, and open-source tools.


---

