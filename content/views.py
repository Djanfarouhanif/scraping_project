from django.shortcuts import render
from .models import Url_content, Article
from .scraping import run
from .article_scrap import Article_content
import json
import random

#=============fonctions pour ajouter les urls dans la basse de donner===========================
def add_url_if_not_exists(urls):
    if urls:
        for url in urls:
            #----------Verifier que url existe ou pas---------------------
            if Url_content.objects.filter(url=url).exists():
                pass
                return None
            else:
                new_url = Url_content.objects.create(url=url)
                new_url.save()
    else:
        return None

#==========pour ajouter les urls dans la base de donner===================
links = run()
add_url_if_not_exists(links)

all_url = Url_content.objects.all()
urls = []

for url in all_url:
    urls.append(url.url)

links = Article_content(urls)
#==================================================CreateDeContainte===============================================

def Content(article):
    
    title = article['title']
    article_chapo = article['article_chapo']
    article_containte = article['article_content']
    article_link = article['link']
    url = Url_content.objects.get(url=article_link)
    if Article.objects.filter(title=title).exists():
        pass
    else:
        new_article = Article.objects.create(url_content = url, title=title, article_chapo=article_chapo, content=article_containte)
        new_article.save()
    return title, article_chapo, article_containte


def Create_article():
    data = links
    if data:
        for index in range(len(data)):
            article_c = data[index]
            Content(article_c)

Create_article()
#===============*******************Fin*************************===============================================
def index(request):
    artilcles = Article.objects.all()
   
    all_article = []
    for article in artilcles:
        all_article.append(article)

    final_sug = random.sample(all_article, 5)

    context = {"final_suggestions": final_sug}
    return render(request, 'page2.html', context)

def post(request):
    article_id= request.GET['post_id']
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'index.html', context)