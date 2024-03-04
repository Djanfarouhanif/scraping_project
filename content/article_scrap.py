import requests
from bs4 import BeautifulSoup
import html5lib
from .scraping import get_url_if_not_none, get_data
import json

data = get_data()

def Article_content(data):
    if data:
        data_article = []
        var = ['info']
        index = 0
        for i, url in enumerate(data):
            var.append(f"info{i+1}")
            var[i] = {}
            index = i
            
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
                    for  paragraphe in article_paragrphe:
                        if "HuffPost " in paragraphe.text.strip():
                            pass
                        else:
                            all_paragraphe.append( get_url_if_not_none(paragraphe))
                    var[index]['title'] = article_title
                    
                    var[index]['article_chapo'] = article_shapo
                    var[index]['article_content'] = " ".join(all_paragraphe)
                    data_article.append(var[i])
            except:
                return None
        with open('content.json', 'w', encoding='utf-16') as f:
            json.dump(data_article, f, ensure_ascii=False,indent=4 )

