from django.contrib.auth.models import User
from django.db import models


class Type_of_the_laws(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
         return self.name
class Laws(models.Model):
    Title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True,null = True)
    Full_description = models.TextField(blank=True,null= True)
    Laws = models.ForeignKey(Type_of_the_laws, on_delete=models.CASCADE)
    Link = models.URLField(null=True,blank = True)
    publication_date = models.DateField()
class FavoriteLaws(models.Model):
    laws = models.ForeignKey(Laws, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
