from django.shortcuts import render,HttpResponseRedirect
from .worlds_news_scrapy import Asia,Asia1,Asia3,Europe,Europe1,Europe2,Africa,Africa1,Africa2,Uk,Uk1,Uk2,US,US1,US2,AS1,AS2,AS3
def WORLD(request):
    as23=Asia()
    as24=Asia1()
    as25=Asia3()
    # europe news
    eur=Europe()
    eur1=Europe1()
    eur2=Europe2()
    afr=Africa()
    afr1=Africa1()
    afr2=Africa2()
    # uk
    uk1=Uk()
    uk2=Uk1()
    uk3=Uk2()
    # us cannada
    us1=US()
    us2=US1()
    us3=US2()
    # australia
    astr=AS1()
    astr1=AS2()
    astr2=AS3()
    return render(request,'worldnews/world.html',{'as23':as23,'as24':as24,'as25':as25,'eur':eur,'eur1':eur1,'eur2':eur2,'afr':afr,'afr1':afr1,'afr2':afr2,'uk1':uk1,'uk2':uk2,'uk3':uk3,'us1':us1,'us2':us2,'us3':us3,'astr':astr,'astr1':astr1,'astr2':astr2})
