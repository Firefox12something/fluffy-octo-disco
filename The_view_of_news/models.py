from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    short_description = models.TextField()
    Full_description = models.TextField()
    link = models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class NewsImage(models.Model):
  image = models.ImageField(upload_to='')
  news = models.ForeignKey(News, on_delete=models.CASCADE)

def __str__(self):
 return  self.image.path


class FavoriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
