import aspose.pdf as ap

options = ap.TeXLoadOptions()
def tex_to_pdf(input_file, ouput_file):
    document = ap.Document(input_file , options)
    document.save(ouput_file)