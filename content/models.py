from django.db import models

class Url_content(models.Model):
    url = models.URLField()

    
class Article(models.Model):
    title = models.CharField(max_length=200)
    article_chapo = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title