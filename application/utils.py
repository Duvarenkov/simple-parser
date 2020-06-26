from bs4 import BeautifulSoup
from urllib.request import urlopen

TAGS_TO_PARSE = ('meta', 'h1', 'h2', 'h3', 'ul', 'table', 'img')


def parse_url(url):
    """
    Fetch URL then parse it and return found tags in JSON
    """
    with urlopen(url) as resp:
       html = resp.read()

    soup = BeautifulSoup(html, 'html.parser')
    result = {
        tag: [str(el) for el in soup.find_all(tag)]
        for tag in TAGS_TO_PARSE
    }

    return result
