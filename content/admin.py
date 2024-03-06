from django.contrib import admin

# Register your models here.
from .models import Article, Url_content

admin.site.register(Article)
admin.site.register(Url_content)