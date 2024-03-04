import requests
from bs4 import BeautifulSoup
import html5lib
from .scraping import get_url_if_not_none, get_data
import json

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
                    article_paragrphe = article_content.find_all('p', class_='asset')
                    all_paragraphe = []
                    for index, paragraphe in enumerate(article_paragrphe):
                        print(paragraphe.text.strip())
                        if "HuffPost " in paragraphe.text.strip():
                            pass
                        else:
                            all_paragraphe.append((index, get_url_if_not_none(paragraphe)))
                    with open("content.json", "w", encoding='utf-8') as f:
                        json.dump(all_paragraphe, f, ensure_ascii=False,indent=4)
                    return all_paragraphe
            except:
                return None
def run():
    Article_content(data)
