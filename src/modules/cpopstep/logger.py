# logger.py
import sys
from docx import Document

doc = Document()

def log_message(message: str):
    print(message)
    doc.add_paragraph(message)
