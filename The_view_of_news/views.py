import self
from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from The_view_of_news.serializer import Newslistserializer, NewsItemSerializer
from The_view_of_news.models import News
from rest_framework.pagination import PageNumberPagination


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = Newslistserializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', '')
        queryset = News.objects.filter(title__contains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = Newslistserializer(page, many=True,
                                            context={'user': request.user})
            return self.get_pagination_response(serializer.data)

        serializer = Newslistserializer(queryset, many=True,
                                        context={'user': request.user})
        return Response(serializer.data)


@api_view(['GET'])
def News_item_View(request, id):
    try:
        news = News.objects.get(id=id)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'HEHEHE'})
    data = Newslistserializer(news).data
    return Response(data=data)


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def registration(request):
    username = request.data['username']
    password = request.data['password']
    User.objects.create_user(username=username,
                             password=password)
    return Response(data={'message': 'User Created'})
