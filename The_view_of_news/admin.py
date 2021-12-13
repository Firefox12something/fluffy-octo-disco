from django.contrib import admin
from The_view_of_news.models import News, NewsImage, FavoriteNews
# Register your models here.
class ImageInline(admin.StackedInline):
    model = NewsImage
    extra = 3


class NewsAdmin(admin.ModelAdmin):
   list_display = 'id title publication_date'.split()
   inlines = [ImageInline]

admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage)
admin.site.register(FavoriteNews)


