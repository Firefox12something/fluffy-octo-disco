from rest_framework import serializers
from library_of_nko.models import Publication_ICNL,The_Rest_of_Publication , Favorite_Publication

class Publication_Rest_serializer(serializers.ModelSerializer):
    class Meta:
        model = The_Rest_of_Publication
        fields = '__all__'

class Publication_ICNL_serializer(serializers.ModelSerializer):
    class Meta:
        model = Publication_ICNL
        fields = '__all__'


    def get_is_favorite(self,Publication_ICNL):
        user = self.context['user']
        if user.is_anonymous:
            return False
        return bool(Favorite_Publication.objects.filter(Publication_ICNL=Publication_ICNL,user=user).count()>0)
