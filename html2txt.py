from bs4 import BeautifulSoup

def html_to_text_with_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    text_content = soup.get_text(separator='\n', strip=True)

    for a_tag in soup.find_all('a'):
        text_content += f'\n{a_tag.get_text()} ({a_tag["href"]})'

    return text_content

def convert_html_to_text(html_file_path, text_file_path):

    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    text_content = html_to_text_with_links(html_content)

    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text_content)

convert_html_to_text('Resume.html', 'output_html.txt')