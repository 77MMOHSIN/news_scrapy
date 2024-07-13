from django.shortcuts import render,HttpResponseRedirect
from .nz_news_scrapy import nz_politics,nz_politics1,nz_politics3,nz_sports,nz_sports1,nz_sports2,nz_economy,nz_economy2,nz_weather,nz_weather1,nz_weather2,nz_weather3,nz_weather4,nz_weather5
def NZ_POLITICS(request):
    nz=nz_politics()
    nz1=nz_politics1()
    
    nz3=nz_politics3()
    return render(request,'nz/nz_politics.html',{'nz':nz,'nz1':nz1,'nz3':nz3})

def NZ_SPORTS(request):
    nzs=nz_sports()
    nzs1=nz_sports1()
    nzs2=nz_sports2()
    return render(request,'nz/nz_sports.html',{'nzs':nzs,'nzs1':nzs1,'nzs2':nzs2})
def NZ_ECONOMY(request):
    nze=nz_economy()
    nze2=nz_economy2()
    return render(request,'nz/nz_economy.html',{'nze':nze,'nze2':nze2})
def NZ_WEATHER(request):
    nzw=nz_weather()
    nzw1=nz_weather1()
    nzw2=nz_weather2()
    nzw3=nz_weather3()
    nzw4=nz_weather4()
    nzw5=nz_weather5()
    
    return render(request,'nz/nz_weather.html',{'nzw':nzw,'nzw1':nzw1,'nzw2':nzw2,'nzw3':nzw3,'nzw4':nzw4,'nzw5':nzw5})
