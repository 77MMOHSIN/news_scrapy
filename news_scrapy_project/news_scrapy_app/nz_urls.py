from django.urls import path
from news_scrapy_app import nz_news_views
urlpatterns = [
    path('nz_politics/',nz_news_views.NZ_POLITICS,name='nzpolitics'),
    path('nz_sports/',nz_news_views.NZ_SPORTS,name='nzsports'),
    path('nz_economy/',nz_news_views.NZ_ECONOMY,name='nzeconomy'),
    path('nz_weather/',nz_news_views.NZ_WEATHER,name='nzweather'),

    
]