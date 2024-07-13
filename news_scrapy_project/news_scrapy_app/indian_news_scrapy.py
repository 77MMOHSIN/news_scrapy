
import requests
from bs4 import BeautifulSoup


# indian_politics
def indian_politic():
    url = 'https://www.republicworld.com/india/politics/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="cardpdLeft").text
        
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}")        
def indian_politic1():
    url = 'https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('li',class_="s-ls_li").text
        
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}")     
def indian_politic2():
    url = 'https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="news_Itm").text
        
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}") 
    
def indian_politic3():
    url = 'https://www.news18.com/politics/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('h3',class_="jsx-704b44ef308e1a3a").text 
        return indian;        
    
def indian_politic4():
    url = 'https://www.indiatoday.in/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="B1S3_content__wrap__9mSB6").text
 
        
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}")     

    # indian_sports
def indian_sports():
    url = 'https://www.news18.com/cricket/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('h3',class_="jsx-35bbca2f76bb9cf0").text       
        return indian;
    else:
        raise Exception(f"Failed to fetch data from {url}")     
def indian_sports1():
    url = 'https://zeenews.india.com/cricket'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="news_description desc-title").text      
        return indian;        
    else:
        
        raise Exception(f"Failed to fetch data from {url}") 
def indian_sports2():
    url = 'https://news.abplive.com/sports'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="_top-story-wrap-col-1").text      
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}") 

def indian_Economy():
    url = 'https://zeenews.india.com/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('div',class_="news_description category-desc").text      
        return indian;        
    else:
        raise Exception(f"Failed to fetch data from {url}") 
    
def indian_Economy1():
    url = 'https://www.news18.com/business/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('h3',class_="jsx-704b44ef308e1a3a").text      
        return indian; 
           
    else:
        raise Exception(f"Failed to fetch data from {url}") 

def indian_Economy2():
    url = 'https://www.businesstoday.in/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        indian=soup.find('a',class_="ftr_wdg_ttl").text      
        return indian;
            
    else:
        raise Exception(f"Failed to fetch data from {url}")             
  # indian weather
def indian_weather1():
    url = 'https://search.yahoo.com/search?fr2=p%3ads%2cv%3aomn%2cm%3asa%2cbrws%3achrome%2cpos%3a2&fr=mcafee&type=E210US91215G0&p=indian+delhi+weather+today'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a
def indian_weather():
    url = 'https://search.yahoo.com/search;_ylt=Awr9.NTyOehlvNYBWhtXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2RWOHV0bmEyUWllMnpQcGpRQXM0bkEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI3BHF1ZXJ5A2luZGlhbiUyME11bWJhaSUyMHdlYXRoZXIlMjB0b2RheQR0X3N0bXADMTcwOTcyMDQ0MQ--?p=indian+Mumbai+weather+today&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a

def indian_weather2():
    url = 'https://search.yahoo.com/search;_ylt=Awrg0GXyQuhlbgQASnFXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1BScFA5QWZvVHUySzF3QXNEemxsRkEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzMwBHF1ZXJ5A2luZGlhbiUyMEh5ZGVyYWJhZCUyMHdlYXRoZXIlMjB0b2RheQR0X3N0bXADMTcwOTcyMDgxNg--?p=indian+Hyderabad+weather+today&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a
def indian_weather3():
    url = 'https://search.yahoo.com/search;_ylt=AwrjfNFpROhlgb8Cgj5XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1c0SEc1aTV2U29lblZIYlE3RUoyQ0EEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI4BHF1ZXJ5A2luZGlhbiUyMGtvbGthdGElMjB3ZWF0aGVyJTIwdG9kYXkEdF9zdG1wAzE3MDk3MjEyMjI-?p=indian+kolkata+weather+today&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a
def indian_weather4():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=indian+Bangalore+weather'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a
def indian_weather5():
    url = 'https://search.yahoo.com/search;_ylt=AwrOrtlKSehl_QsCOsdXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA3QycUlRZzVyUjh5bXhuMUdtVEpON0EEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI4BHF1ZXJ5A2luZGlhbiUyMENoZW5uYWklMjB3ZWF0aGVyJTIwdG9kYXkEdF9zdG1wAzE3MDk3MjIxMjc-?p=indian+Chennai+weather+today&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="d-f ai-s")
    a=indian.text
    return a
    


def indian_time():
    url = 'https://dateandtime.info/country.php?code=IN'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('time', class_="hms_fulldate results")
    a=indian.text
    return a
