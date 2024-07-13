from django.shortcuts import render,HttpResponseRedirect
from .chain_news_scrapy import chain_politic,chain_politic1,chain_politic2,chain_Economy,chain_Economy1,chain_sports,chain_sports1,chain_sports2,chain_weather1,chain_weather2,chain_weather3,chain_weather4,chain_weather5
def Chain_politics(request):
    chain=chain_politic()
    chain1=chain_politic1()
    chain2=chain_politic2()
    return render(request,'chian_news/chain_politics.html',{'chain':chain,'chain1':chain1,'chain2':chain2})
def Chain_economy(request):
    economy=chain_Economy()
    economy1=chain_Economy1()
    return render(request,'chian_news/chain_Economy.html',{'economy':economy,'economy1':economy1})
def Chain_sports(request):
    Sports=chain_sports()
    Sports1=chain_sports1()
    Sports2=chain_sports2()

    return render(request,'chian_news/chain_sports.html',{'Sports':Sports,'Sports1':Sports1,'Sports2':Sports2})

def Chain_weathers(request):
    weather=chain_weather1()
    weather1=chain_weather2()
    weather2=chain_weather3()
    weather3=chain_weather4()
    weather4=chain_weather5()
    
    return render(request,'chian_news/chain_weather.html',{'weather':weather,'weather1':weather1,'weather2':weather2,'weather3':weather3,'weather4':weather4})