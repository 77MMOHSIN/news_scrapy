from django.shortcuts import render,HttpResponseRedirect
from .pak_news_scrapy import worldsnews_scrapy,pak_politics_news_scrapy,pak_politics_news_scrapy3,pak_politics_news_scrapy4,pakistan_weather,pakistan_lahore,pakistan_karachi,pakistan_bahawapur,pakistan_multan,pakistan_vehari,pak_sports_news,pak_sports_news1,pak_sports_news2,pak_Economy,pak_Economy1,pak_Economy3
# show news in html page 
def newns(request):
    news=worldsnews_scrapy()
    politics=pak_politics_news_scrapy()
    
    politics3=pak_politics_news_scrapy3()
    politics4=pak_politics_news_scrapy4()
    return render(request,'paknews/pak_politics.html',{'news':news,'politics':politics,'politics3':politics3,'politics4':politics4})
def pakweather(request):
    weathe=pakistan_weather()
    lahore=pakistan_lahore()
    karachi=pakistan_karachi()
    bahawalpur=pakistan_bahawapur()
    multan=pakistan_multan()
    vehari=pakistan_vehari
    return render(request,'paknews/pakweather.html',{'weather':weathe,'lahore':lahore,'karachi':karachi,'bahawalpur':bahawalpur,'multan':multan,'vehari':vehari})
def pak_sports1(request):
    sports=pak_sports_news()
    sports1=pak_sports_news1()
    sports2=pak_sports_news2()
    return render(request,'paknews/pak_sports.html',{'sports':sports,'sport1':sports1,'sports2':sports2})
def pak_economy(request):
    economy=pak_Economy()
    economy1=pak_Economy1()
    economy2=pak_Economy3()
    return render(request,'paknews/pakeconomy.html',{'economy':economy,'economy1':economy1,'economy2':economy2})



