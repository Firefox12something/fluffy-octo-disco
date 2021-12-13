from rest_framework import serializers

import The_view_of_news.admin
from The_view_of_news.models import News, NewsImage,FavoriteNews
class Newslistserializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id is_favourite title short_description publication_date image'.split()

    def get_is_favourite(self,news):
        user = self.context['user']
        if user.is_anonymous:
            return  False
        return bool(FavoriteNews.objects.filter(news=news,user=user).count()>0)
class NewsItemSerializer(serializers.ModelSerializer):
  is_favorite = serializers.SerializerMethodField()
  images = serializers.SerializerMethodField()

  class Meta:
      model = News
      fields = 'id is_favorite title full_description link images'.split()
  def get_is_favorit(self,news):
    user = self.context['user']
    if user.is_anonymous:
        return False
    return bool(FavoriteNews.objects.filter(news=news,user=user).count()>0)

  def get_images(self,news):
    return [i.image.url for i in NewsImage.objects.filter(news=news)]