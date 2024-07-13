# from django.contrib import admin
from django.urls import path
from news_scrapy_app import views
urlpatterns = [
 path('',views.base,name='base'),
#  pakistan news
 path('paknews/',views.pak,name='pakistan'), 
 path('politcs/',views.politics,name='politics'),
 path('gaza/',views.gaza,name='gaza'), 
#  indian news

 
# path('politics/',views.indian_politic,name='indian'),
# path('Religions/',views.indian_religion,name='religions'),
path('indweather/',views.indian_w_Delhi,name='delhi'),
# china news 
path('chinapolitics/',views.china_politic,name='chinap'),
path('accounts/login/',views.login1,name='login'),
path('registration/',views.customerregistrationview.as_view(), name='registration'),
#  path('ProfileView/',views.ProfileView.as_view(),name='Profile'),
 path('profile/',views.ProfileView.as_view(),name='profile'),
 path('changepass/',views.user_change_pass,name='change'),
 path('changedone/',views.changedone,name='done'),
#  path('pais/',views.pak45,name='pak45')
]
 
 
   

