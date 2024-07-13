from django.shortcuts import render,HttpResponseRedirect
from .models import Customer
from django.views import View
from .form import CustomerRegistrationForm,Customerprofileform,LoginForm,ChangePass
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

from .news_scrapy import scrape_pakistan,scrape_pakistan2,scrape_gaza,scrape_gaza1,indian_weather1,indian_weather,indian_weather2,indian_weather3,indian_weather4,indian_weather5,china_politics,china_politics1,china_politics2,china_politics3,china_politics4
from .gaza import scrape_gaza5,scrape_gaza6
from .indian_news_scrapy import indian_time
from .chain_news_scrapy import chain_time,chain_time1,us_time,us_time1,aus_time,aus_time1,nz_time,nz_time1,pk_time,pk_time1
# def pak45(request):
#     swp=scrape_gaza5()
#     scr=scrape_gaza6()
#     return render(request,'pakis.html',{'swp':swp,'scr':scr})


def login1(request):
    if request.method=='POST':
     fm=LoginForm(request=request,data=request.POST) 
     if fm.is_valid():
         uunam=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         User=authenticate(username=uunam,password=upass)
         if User is not None:
            login(request,User)
        #  messages.success(request,"logged is successfully !!")             
         return HttpResponseRedirect('/')  
    else:       
        fm=LoginForm()
    return render(request,'login.html',{'form':fm })



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class customerregistrationview(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html', {'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success (request,'registration is Submitted Successfully!!!!')
            form.save()
           
        return render(request,'customerregistration.html', {'form':form})

def user_change_pass(request):
    if request.method=='POST':
     fm=ChangePass(user=request.user,data=request.POST)   
     if fm.is_valid():
        fm.save() 
        update_session_auth_hash(request,fm.user)
        return HttpResponseRedirect('/profile/')
    
    else:    
     fm=ChangePass(user=request.user)
    return render(request,'changepassword.html',{'form':fm})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
        def get(self, request):        
            form=Customerprofileform()
            return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
        def post(self,request):
            form=Customerprofileform(request.POST)                                                              
            if form.is_valid():
                usr=request.user
                name=form.cleaned_data['name']
                Numb=form.cleaned_data['Number']
                cit=form.cleaned_data['city']
                addrs=form.cleaned_data['address']
                state=form.cleaned_data['state']
                req=Customer(user=usr ,name=name,Number=Numb,city=cit,address=addrs,state=state)
                req.save()
                messages.success(request,'Congratulations!!profile update Successfully')
            return render(request,'profile.html',{'form':form,'active':'btn-primary'})
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
# change password with old password
def user_change_pass(request):
    if request.method=='POST':
     fm=ChangePass(user=request.user,data=request.POST)   
     if fm.is_valid():
        fm.save() 
        update_session_auth_hash(request,fm.user)
        return HttpResponseRedirect('/changedone/')
    
    else:    
     fm=ChangePass(user=request.user)
    return render(request,'changepassword.html',{'form':fm})    
def changedone(request):
    return render(request,'changedone.html')
def home(request):
    return render(request,'home.html')




# Create your views here.
def base(request):
    indiantime=indian_time()
    chaintime=chain_time()
    chaintime1=chain_time1()
    ustime=us_time()
    ustime1=us_time1() 
    austime=aus_time()
    austime1=aus_time1()
    nztime=nz_time()
    nztime1=nz_time1()
    pktime=pk_time()
    pktime1=pk_time1()
    return render(request,'base.html',{'indiantime':indiantime,'chaintime':chaintime,'chaintime1':chaintime1,'ustime':ustime,'ustime1':ustime1,'austime':austime,'austime1':austime1,'nztime':nztime,'nztime1':nztime1,'pktime':pktime,'pktime1':pktime1})
# pakistan website
def pak(request):
    pak=scrape_pakistan()
    return render(request,'pakistan.html',{'pak':pak})
def politics(request):
    # pak3=scrape_pakistan3()
    pak2=scrape_pakistan2()
    # pak4=scrape_pakistan4()
    # pak5=scrape_pakistan5()
    return render(request,'pakistan.html',{'pak2':pak2})
def gaza(request):
    gaza=scrape_gaza()
    gaza1=scrape_gaza1()
    swp=scrape_gaza5()
    scr=scrape_gaza6()
    return render(request,'gaza.html',{'gaza':gaza,'gaza1':gaza1,'swp':swp,'scr':scr})

# pakistan weather
# sports
# def pak_sports(request):
#     sports=pakistan_sports()
#     return render(request,'paksports.html',{'sports':sports})

# indian website



def indian_w_Delhi(request):
    indianw=indian_weather1()
    indian1=indian_weather()
    indian12=indian_weather2()
    indianw=indian_weather3()
    indianw4=indian_weather4()
    indianw5=indian_weather5()
    return render(request,'ind_weather.html',{'indianw':indianw,'indian1':indian1,'indian12':indian12,'indianw':indianw,'indianw4':indianw4,'vehari1':indianw5})
def china_politic(request):
    china=china_politics()
    china1=china_politics1()
    china2=china_politics2()
    china3=china_politics3()
    china4=china_politics4()
    return render(request,'china_politic.html',{'china':china,'china1':china1,'china2':china2,'china3':china3,'china4':china4})