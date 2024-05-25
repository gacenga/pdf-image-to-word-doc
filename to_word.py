from docx import Document

def to_word(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)