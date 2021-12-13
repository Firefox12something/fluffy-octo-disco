from rest_framework import serializers

from list_with_laws.models import Laws , Type_of_the_laws, FavoriteLaws
class Laws_Type_Serislizer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_the_laws
        fields = '__all__'

class Laws_serializer (serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Laws
        fields = "id Laws ".split()


    def get_is_favorite(self,Laws):
        user = self.context['user']
        if user.is_anonymous:
            return False
        return bool(FavoriteLaws.objects.filter(Laws=Laws,user=user).count()>0)

class LawsListSerializer(serializers.ModelSerializer):
 is_favorite = serializers.SerializerMethodField()

 class Meta:
     model = Laws
     fields = "id publication_date short_description Title "
 def get_is_favorite(self,Laws):
  user = self.context['user']
  if user.is_anonymous:
      return False
  return bool(FavoriteLaws.objects.filter(Laws=Laws,user=user).count()>0)


class ItemLawsSerializer(serializers.ModelSerializer):
     is_favorite = serializers.SerializerMethodField()

     class Meta:
         model = Laws
         fields = "id Full_description Title publication_date Link Laws ".split()

     def get_is_favorite(self,Laws):
         user = self.context['user']
         if user.is_anonymous:
             return False

         return bool(FavoriteLaws.objects.filter(Laws=Laws,user=user).count()>0)



