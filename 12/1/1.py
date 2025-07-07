import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    Cleans the text from html tags and writes this text to another file.

    :param html_file: str
    :param result_file: str
    :return: None (write new result_file.txt)
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        while '<' in html and '>' in html:
            start = html.find('<')
            end = html.find('>')
            html = html[:start] + html[end + 1:]
        new_html = html.splitlines()
        html_without_empty_lines = [line.strip() for line in new_html if
                                    line.strip()]
        clean_html = '\n'.join(html_without_empty_lines)
    with codecs.open(result_file, 'w', 'utf-8') as clean_file:
        clean_file.write(clean_html)


delete_html_tags('draft.html')
