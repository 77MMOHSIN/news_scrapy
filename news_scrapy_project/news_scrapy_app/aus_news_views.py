from django.shortcuts import render,HttpResponseRedirect
from .aus_news_scrapy import aus_politics,aus_politics1,aus_politics2,aus_sports,aus_sports1,aus_sports2,aus_economy,aus_economy1,aus_economy2,aus_weather,aus_weather1,aus_weather2,aus_weather3,aus_weather4,aus_weather5,aus_weather6
def AUS_POLITICS(request):
    aus=aus_politics()
    aus1=aus_politics1()
    aus2=aus_politics2()
    return render( request,'aus/aus_politics.html',{'aus':aus,'aus1':aus1,'aus2':aus2})
def AUS_SPORTS(request):
    ausp=aus_sports()
    ausp1=aus_sports1()
    ausp2=aus_sports2()
    return render(request,'aus/aus_sports.html',{'ausp':ausp,'ausp1':ausp1,'ausp2':ausp2})
def AUS_ECONOMY(request):
    ause=aus_economy()
    ause1=aus_economy1()
    ause2=aus_economy2()
    
    

    return render(request,'aus/aus_economy.html',{'ause':ause,'ause1':ause1,'ause2':ause2,})
def AUS_WEATHER(request):
    ausw=aus_weather()
    ausw1=aus_weather1()
    ausw2=aus_weather2()
    ausw3=aus_weather3()
    ausw4=aus_weather4()
    ausw5=aus_weather5()
    ausw6=aus_weather6()
    
    
    return render(request,'aus/aus_weather.html',{'ausw':ausw,'ausw1':ausw1,'ausw2':ausw2,'ausw3':ausw3,'ausw4':ausw4,'ausw5':ausw5,'ausw6':ausw6})