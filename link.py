import PyPDF2

def get_links(filename):
    links=[]
    pdf_reader = PyPDF2.PdfReader(filename)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        annotations = page.get('/Annots')
        if annotations:
            for annotation in annotations:
                annotation_object = annotation.get_object()
                if annotation_object.get('/Subtype') == '/Link':
                    link = annotation_object.get('/A').get('/URI')
                    if link:
                        links.append(link)
    return links
