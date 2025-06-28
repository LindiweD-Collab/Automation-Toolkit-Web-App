# 🚀 Automation Toolkit Web App

A fully functional **Automation Dashboard** built using **Streamlit**, designed to help users automate everyday tasks like **file renaming**, **email validation**, **CSV conversion**, and **data extraction** from **PDFs** and **images (OCR)** — all through a user-friendly web interface.

---

## 🔧 Project Overview

This toolkit showcases how automation can simplify repetitive tasks from a central web platform. It's ideal for small teams, virtual assistants, or individuals looking to boost productivity without coding.

---

## 🧰 Features

✅ **Rename a batch of files**  
✅ **Extract text from PDFs and images (OCR)**  
✅ **Validate email addresses**  
✅ **Convert CSV to Excel**  
  

---

## 📁 File Structure

automation_toolkit/
├── app.py # Main Streamlit app
|
├── utils/ # Utility scripts
|
│ ├── file_utils.py # File renaming, conversions
|
│ ├── ocr_utils.py # OCR (PDF/image text extraction)
|
│ └── validators.py # Email validation
|
├── requirements.txt # Python dependencies


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
Python 🐍

Streamlit 📊

PyTesseract 🔍

Pandas & OpenPyXL 📁

Regex for email validation 📧
```

### 📄 License
This project is licensed under the MIT License.
Feel free to use, fork, and contribute!


### 🧠 Author
Built by Lindiwe Thabsile Dlomo — Passionate about automation, productivity, and open-source tools.


---

