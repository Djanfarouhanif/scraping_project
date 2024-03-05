from django.shortcuts import render
from .models import Url_content, Article
from .scraping import get_data
from .article_scrap import Article_content
import json

def add_url_if_not_exists(urls):
    if urls:
        for url in urls:
            if Url_content.objects.filter(url=url).exists():
                return None
            else:
                new_url = Url_content.objects.create(url=url)
                new_url.save()
    else:
        return None


data = get_data()
add_url_if_not_exists(data)
all_url = Url_content.objects.all()
urls = []

for url in all_url:
    urls.append(url.url)
    
Article_content(urls)

def index(request):
    return render(request)

#==================================================CreateDeContainte===============================================

def Content(article):
    title = article['title']
    article_chapo = article['article_chapo']
    article_containte = article['article_content']
    if Article.objects.filter(title=title).exists():
        pass
    else:
        new_article = Article.objects.create(title=title, article_chapo=article_chapo, content=article_containte)
        new_article.save()
    return title, article_chapo, article_containte


def Create_article():
    with open('content.json', 'r', encoding='utf-16') as f:
        data = json.load(f)

    for index in range(len(data)):
        article_c = data[index]
        Content(article_c)

Create_article()
#===============*******************Fin*************************===============================================
print(len(Article.objects.all()))