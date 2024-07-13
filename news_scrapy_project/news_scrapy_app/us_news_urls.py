from django.urls import path
from news_scrapy_app import us_news_views
urlpatterns = [
    
path('us_politics/',us_news_views.US_POLITCS,name='uspolitics'),
path('us_sports/',us_news_views.US_SPORTS,name='ussports'),
path('us_economy/',us_news_views.US_ECONOMY,name='useconomy'),

path('us_weather/',us_news_views.US_WEATHERS,name='usweather')


]


