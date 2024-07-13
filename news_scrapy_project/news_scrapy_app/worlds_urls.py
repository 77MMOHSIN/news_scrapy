from django.urls import path
from news_scrapy_app import worlds_views
urlpatterns = [
    path('world/',worlds_views.WORLD,name='worldnews')


]