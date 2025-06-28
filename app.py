import streamlit as st
from utils.file_utils import batch_rename, csv_to_excel
from utils.ocr_utils import extract_text_from_pdf, extract_text_from_image
from utils.validators import is_valid_email

st.set_page_config(page_title="Automation Toolkit", layout="wide")

st.title("🤖 Automation Toolkit Web App")

task = st.sidebar.selectbox("Select a Task", [
    "Batch Rename Files", "PDF Text Extractor", "Image OCR",
    "Email Validator", "CSV to Excel Converter"
])

if task == "Batch Rename Files":
    st.header("📁 Batch Rename Files")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
    prefix = st.text_input("Enter a prefix")
    if st.button("Rename"):
        if uploaded_files and prefix:
            renamed = batch_rename(uploaded_files, prefix)
            st.success(f"Renamed {len(renamed)} files.")
        else:
            st.warning("Please upload files and provide a prefix.")

elif task == "PDF Text Extractor":
    st.header("📄 Extract Text from PDF")
    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        st.text_area("Extracted Text", text, height=300)

elif task == "Image OCR":
    st.header("🖼️ Extract Text from Image")
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if image_file:
        text = extract_text_from_image(image_file)
        st.text_area("Extracted Text", text, height=300)

elif task == "Email Validator":
    st.header("📧 Email Validator")
    email = st.text_input("Enter Email")
    if email:
        if is_valid_email(email):
            st.success("✅ Valid Email")
        else:
            st.error("❌ Invalid Email")

elif task == "CSV to Excel Converter":
    st.header("📊 CSV to Excel Converter")
    csv_file = st.file_uploader("Upload CSV", type="csv")
    if csv_file:
        excel_bytes = csv_to_excel(csv_file)
        st.download_button("Download Excel File", data=excel_bytes, file_name="converted.xlsx")

