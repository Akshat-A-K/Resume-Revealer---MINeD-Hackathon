from docx2pdf import convert
def converttopdf(input_file, ouptput_file):
    convert(input_file, ouptput_file)
    return ouptput_file