from django.urls import path
from news_scrapy_app import chain_news_views
urlpatterns = [
    
    path('chain_politics/',chain_news_views.Chain_politics,name='chainpolitics'),
 path('chain_Economy/',chain_news_views.Chain_economy,name='chainEconomy'),
 path('chain_Sports/',chain_news_views.Chain_sports,name='chainsports'),
path('chain/',chain_news_views.Chain_weathers,name='chainsweathers'),

]
