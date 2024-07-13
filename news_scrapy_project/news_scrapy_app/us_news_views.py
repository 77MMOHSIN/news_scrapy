from django.shortcuts import render,HttpResponseRedirect
from .us_news_scrapy import Us_politics,Us_politics1,Us_politics2,Us_politics3,Us_politics4,Us_sports,Us_sports1,Us_sports2,Us_economy,Us_economy1,Us_economy2,Us_weather,Us_weather1,Us_weather2,Us_weather3,Us_weather4,Us_weather5
def US_POLITCS(request):
    us=Us_politics()
    us1=Us_politics1()
    us2=Us_politics2()
    us3=Us_politics3()
    us4=Us_politics4()
    return render(request,'us_news/us_politics.html',{'us':us,'us1':us1,'us2':us2,'us3':us3,'us4':us4})
def US_SPORTS(request):
    usp=Us_sports()
    usp1=Us_sports1()
    usp2=Us_sports2()
    
    return render(request,'us_news/us_sports.html',{'usp':usp,'usp1':usp1,'usp2':usp2})
# us Economy

def US_ECONOMY(request):
    use=Us_economy()
    use1=Us_economy1()
    use2=Us_economy2()
    return render(request,'us_news/us_economy.html',{'use':use,'use1':use1,'use2':use2})

def US_WEATHERS(request):
    usw=Us_weather()
    usw1=Us_weather1()
    usw2=Us_weather2()
    usw3=Us_weather3()
    usw4=Us_weather4()
    usw5=Us_weather5()
    return render(request,'us_news/us_weather.html',{'usw':usw,'usw1':usw1,'usw2':usw2,'usw2':usw2,'usw3':usw3,'usw4':usw4,'usw5':usw5})
