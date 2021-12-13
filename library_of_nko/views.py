from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import  ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from library_of_nko.models import Publication_ICNL,The_Rest_of_Publication,Favorite_Publication
from library_of_nko.serializer import Publication_Rest_serializer,Publication_ICNL_serializer


class  Publication_of_ICNL_APIView(ListAPIView):
    queryset = Publication_ICNL.objects.all()
    serializer_class = Publication_ICNL_serializer
    pagination_class = PageNumberPagination

    def list(self,request,*args,**kwargs):
        search = request.query_params.get('search','')
        queryset = Publication_ICNL.objects.filter(title_contains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serialiizer = Publication_ICNL_serializer(page,many=True,
                                                      context={'user':request.user})
            return self.get_pagination_response(serialiizer.data)
        serializer = Publication_ICNL_serializer(queryset,many=True,
                                                 context={'user':request.user})
        return Response(serializer.data)


class The_rest_of_publication_APIView(ListAPIView):
    queryset = Publication_ICNL.objects.all()
    serializer_class = Publication_Rest_serializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', '')
        queryset = The_Rest_of_Publication.objects.filter(title_contains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serialiizer = Publication_Rest_serializer(page, many=True,
                                                      context={'user': request.user})
            return self.get_pagination_response(serialiizer.data)
        serializer = Publication_Rest_serializer(queryset, many=True,
                                                 context={'user': request.user})
        return Response(serializer.data)

