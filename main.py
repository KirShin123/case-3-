
from Functions import change_document_style
def main():
    files_to_process = [
    'content/1.docx',
    'content/2.docx',
    'content/3.docx',
    'content/4.docx',
    'content/5.docx'
    ]

    for file_path in files_to_process:
        print(f'Выводит текстовые файлы» {file_path}')
        change_document_style(file_path) 
        

<<<<<<< HEAD
# Инициализационный скрипт
if __name__ == "__main__":
    main()
=======
for file_path in files_to_process:
    print(f'Выводит текстовые файлы» {file_path}')
    change_document_style(file_path) 
>>>>>>> 2f32cdb8be0eeae74a5e072599523b6d26a0397b
