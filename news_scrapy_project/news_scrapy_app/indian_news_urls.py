from django.urls import path
from news_scrapy_app import indian_news_views
urlpatterns = [
    
 path('indian_politics/',indian_news_views.Indian_politics,name='indianpolitics'),
  path('indian_Sports/',indian_news_views.Indian_sports,name='indianSports'),
   path('indian_Economy/',indian_news_views.Indian_economy,name='indianeconomy'),
   path('indian_weather/',indian_news_views.indian_Weathers,name='indianWeather'),
   



]


