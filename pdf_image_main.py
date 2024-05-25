from to_word import to_word
from pic_analysis import analyze_pic, analyze_pdf
import pytesseract
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def analyze():
    try:
        path, output_path = upload()
        output_path = output_path.get().strip()
        if path.lower().endswith('.pdf'):
            all_text = ""
            images = analyze_pdf(path)
            for image in images:
                text = pytesseract.image_to_string(image, lang='eng')
                all_text += text + '\n'
            to_word(all_text, output_path)
        elif path.lower().endswith(('.jpg', '.png', '.jpeg')):
            text = analyze_pic(path)
            to_word(text, output_path)
        result.config(text="SUccessfully analyzed")
    except Exception as e:
        result.config(text=f"Error: {e}")

def upload():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Image files", "*.png;*.jpg;*.jpeg;*.tiff")])
    if file_path:
        save_as = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
        if save_as:
            return file_path, save_as

#create main window
root = tk.Tk()
root.title("pdf/img to word")

#create and placeupload buttoni
upload_button = tk.Button(root, text="UPLOAD", command=upload)
upload_button.pack(pady=10)

#create and place button
Analyze_button = tk.Button(root, text="SCAN", command=analyze)
Analyze_button.pack(pady=10)

#create and place result label
result = tk.Label(root, text="", font=('Monospace', 10))
result.pack(pady=10)

#run application
root.mainloop()
