from django.urls import path
from news_scrapy_app import aus_news_views
urlpatterns = [
    path('aus_politics/',aus_news_views.AUS_POLITICS,name='auspolitics'),
     path('aus_sports/',aus_news_views.AUS_SPORTS,name='aussports'),
    path('aus_economy/',aus_news_views.AUS_ECONOMY,name='ausseconomy'),
path('aus_weather/',aus_news_views.AUS_WEATHER,name='ausweather'),
    

]