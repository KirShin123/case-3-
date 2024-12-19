
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

def change_document_style(file_path):
    document = Document(file_path)


    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(14)

    for paragraph in document.paragraphs:
        paragraph.style = style
        paragraph_format = paragraph.paragraph_format
        paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        paragraph_format.line_spacing = 1.5
    document.save(file_path)