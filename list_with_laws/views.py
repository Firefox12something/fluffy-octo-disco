from django.shortcuts import render
import self
from rest_framework.generics import  ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from list_with_laws.serializer import Laws_serializer,LawsListSerializer,Laws_Type_Serislizer, ItemLawsSerializer
from list_with_laws.models import Laws, Type_of_the_laws,FavoriteLaws

class LawsListAPIView(ListAPIView):
    queryset = Laws.objects.all()
    serializer_class = LawsListSerializer
    pagination_class = PageNumberPagination

    def list(self, request,*args,**kwargs):
        search = request.query_params.get('search','')
        queryset = Laws.objects.filter(title_contains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = LawsListSerializer(page,many=True,
                                            context={'user':request.user})
            return self.get_pagination_response(serializer.data)
        serializer = LawsListSerializer(queryset,many=True,
                                        context={'user':request.user})
        return Response(serializer.data)

