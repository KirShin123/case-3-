from functions import change_document_style

files_to_process = [
'/content/1.docx',
'/content/2.docx',
'/content/3.docx',
'/content/4.docx',
'/content/5.docx'
]

for file_path in files_to_process:
    print(f'РћР±СЂР°Р±Р°С‚С‹РІР°РµРј С„Р°Р№Р» {file_path}')
    change_document_style(file_path) 

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
    document.safe(file_path)
