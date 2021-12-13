from django.db import models
from django.contrib.auth.models import User
class The_Rest_of_Publication(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Publication_ICNL(models.Model):
    Title = models.CharField(max_length=100)
    Publication_date = models.DateField()
    Full_text = models.TextField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)



class Favorite_Publication(models.Model):
    publication = models.ForeignKey(Publication_ICNL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
