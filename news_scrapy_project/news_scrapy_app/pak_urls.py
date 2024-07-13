from django.urls import path
from news_scrapy_app import pak_news_views
urlpatterns = [
    path('Politics/',pak_news_views.newns,name='politics'),
    path('weather/',pak_news_views.pakweather,name='weather'),
     path('pak_sports/',pak_news_views.pak_sports1,name='sports'),
     path('pak_Economy/',pak_news_views.pak_economy,name='Economy'),
     
     



]


