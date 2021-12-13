from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Laws)
admin.site.register(FavoriteLaws)
admin.site.register(Type_of_the_laws)