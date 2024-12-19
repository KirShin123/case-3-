
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

def change_document_style(file_path):
    document = Document(file_path)

    # Проходимся по всем абзацам документа
    for paragraph in document.paragraphs:
        # Устанавливаем шрифт и размер
        for run in paragraph.runs:
            font = run.font
            font.name = 'Times New Roman'
            font.size = 14000000  # Размер шрифта в пунктах (14 pt = 28 half-points)

        # Устанавливаем межстрочный интервал
        paragraph_format = paragraph.paragraph_format
        paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE

    # Сохраняем документ под тем же именем
    document.save(document_path)



def change_documents(directory_path):
  # Перебираем все документы в папке
  for file_path in directory_path.glob('*.docx'):
      print(f"Обрабатываем файл {file_path.name}")
      change_document_style(file_path)
      print(f"Файл {file_path.name} обработан")