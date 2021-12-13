import self
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from The_view_of_news.serializer import Newslistserializer, NewsItemSerializer
from The_view_of_news.models import News
from rest_framework.pagination import PageNumberPagination

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = Newslistserializer
    pagination_class = PageNumberPagination

    def list(self,request,*args,**kwargs):
        search = request.query_params.get('search', '')
        queryset = News.objects.filter(title__contains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = Newslistserializer(page,many=True,
                                            context={'user': request.user})
            return self.get_pagination_response(serializer.data)

        serializer = Newslistserializer(queryset, many=True,
                                        context={'user': request.user})
        return Response(serializer.data)