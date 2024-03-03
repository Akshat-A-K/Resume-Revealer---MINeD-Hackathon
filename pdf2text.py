import fitz
import string

def extract_ascii(text):
    ascii_chars = set(string.ascii_letters + string.punctuation + string.digits + string.whitespace)
    ascii_text = ''.join(char for char in text if char in ascii_chars)
    return ascii_text

def get_text(pdf_file_path, output_file_name):
    pdf_document = fitz.open(pdf_file_path)

    text_content = ''

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text_content += page.get_text()
    text= extract_ascii(text_content)
    text= text.replace("| link","")
    text=text.replace("| Link","")
    text=text.replace("#","")
    text=text.replace("|","")
    print(text)
    pdf_document.close()
    with open(output_file_name, 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    return text