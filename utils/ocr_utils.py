import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def extract_text_from_image(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img)
    return text.strip()

