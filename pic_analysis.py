import pytesseract
from PIL import Image
import os
import fitz
import io

#analyze picture
def analyze_pic(path):
    """Uses OCR to get text from picture"""
    with Image.open(path) as img:
        #use OCR to get text from image
        text = pytesseract.image_to_string(img, lang='eng')
    return text

#analyze pdf
def analyze_pdf(path):
    """Uses OCR to get text from pdf"""
    images = []
    pdf_document = fitz.open(path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        images.append(img)
    return images
