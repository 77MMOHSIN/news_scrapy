from django.shortcuts import render,HttpResponseRedirect
from .indian_news_scrapy import indian_politic,indian_politic1,indian_politic2,indian_politic3,indian_politic4,indian_sports,indian_sports1,indian_sports2,indian_Economy,indian_Economy1,indian_Economy2,indian_weather1,indian_weather,indian_weather2,indian_weather3,indian_weather4,indian_weather5
def Indian_politics(request):
    indian=indian_politic()
    indian1=indian_politic1()
    indian2=indian_politic2()
    indian3=indian_politic3()
    indian4=indian_politic4()
    return render(request,'indian_news/indian_politics.html',{'indian':indian,'indian1':indian1,'indian2':indian2,'indian3':indian3,'indian4':indian4})
def Indian_sports(request):
    sports=indian_sports()
    sports1=indian_sports1()
    sports2=indian_sports2()
    return render(request,'indian_news/indian_sports.html',{'sports':sports,'sports1':sports1,'sports2':sports2})
def Indian_economy(request):
    economy=indian_Economy()
    economy1=indian_Economy1()
    economy2=indian_Economy2()
    return render(request,'indian_news/indian_Economy.html',{'economy':economy,'economy1':economy1,'economy2':economy2})

# indian weather
def indian_Weathers(request):
    indianw=indian_weather1()
    indian1=indian_weather()
    indian12=indian_weather2()
    indianw=indian_weather3()
    indianw4=indian_weather4()
    indianw5=indian_weather5()
    
    return render(request,'indian_news/indian_weather.html',{'indianw':indianw,'indian1':indian1,'indian12':indian12,'indianw':indianw,'indianw4':indianw4,'vehari1':indianw5})