from django.shortcuts import render
from .models import Url_content
from .scraping import get_data
from .article_scrap import Article_content, run

run()
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


def index(request):
    return render(request)