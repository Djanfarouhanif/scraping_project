import requests
from bs4 import BeautifulSoup
import html5lib
from .scraping import get_url_if_not_none, get_data


data = get_data()

def Article_content(data):
    if data:
        for url in data:
            try:
                response = requests.get(url)
                response.encoding = response.apparent_encoding
                if response:
                    html = response.text
                    soup = BeautifulSoup(html, 'html5lib')
                    header = soup.find('header', class_='article-header')
                    article_title = get_url_if_not_none(header.find('h1', class_="article-title"))
                    article_shapo = get_url_if_not_none(header.find('p', class_='article-chapo'))
                    article_content = soup.find("div", class_='article-content')
                    article_paragrphe = article_content.find_all('p', class_='asset-text')
                    all_paragraphe = []
                    for paragraphe in article_content:
                        if 'HuffPost' not in paragraphe:
                            all_paragraphe.append(get_url_if_not_none(paragraphe))
                    return len(all_paragraphe)
            except:
                return None


print(Article_content(data))
