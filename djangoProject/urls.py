"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from The_view_of_news import views as news_views
from list_with_laws import views as Laws_views
from library_of_nko import views as Publication
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/Laws/',Laws_views.LawsListAPIView.as_view()),
    path('api/v1/news/',news_views.NewsListAPIView.as_view()),
    path('api/v1/Publication_ICNL',Publication.Publication_of_ICNL_APIView),
    path ('api/v1/Rest_Publication',Publication.The_rest_of_publication_APIView),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

