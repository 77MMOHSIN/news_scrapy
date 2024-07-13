import requests
from bs4 import BeautifulSoup


def worldsnews_scrapy():
    url = 'https://arynews.tv/'
    header={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="td-module-meta-info").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
def pak_politics_news_scrapy():
    url = 'https://www.geo.tv/category/pakistan'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="entry-title").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")    



def pak_politics_news_scrapy3():
    url = 'https://www.samaa.tv/latest-news'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="text").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")  
def pak_politics_news_scrapy4():
    url = 'https://dunyanews.tv/livehd/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="media").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")        

# pak_weather
def pakistan_weather():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=pakistan+weather+today'
    # header='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='d-f ai-s').text
    return p;

def pakistan_lahore():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=lahore+pakistan+weather'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='d-f ai-s').text
    return p;
def pakistan_karachi():
    url = 'https://search.yahoo.com/search;_ylt=AwrgwNcYm.VlwWESQpxXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA3VSZHViNUJMU0lLOWVYZWUyZ3d2VUEEbl9yc2x0AzAEbl9zdWdnAzgEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI0BHF1ZXJ5A2thcmFjaGklMjBwYWtpc3RhbiUyMHdlYXRoZXIEdF9zdG1wAzE3MDk1NDY0NDA-?p=karachi+pakistan+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='d-f ai-s').text
    return p;
    
def pakistan_bahawapur():
    url = 'https://search.yahoo.com/search;_ylt=AwrO.jxXnOVlVQIT.ipXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2pzeHJaeFJ4UmN1QWJqRVo1alg0ckEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI3BHF1ZXJ5A0JhaGF3YWxwdXIlMjBwYWtpc3RhbiUyMHdlYXRoZXIEdF9zdG1wAzE3MDk1NDcyMTg-?p=Bahawalpur+pakistan+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='d-f ai-s').text
    return p;
def pakistan_multan():
    url = 'https://search.yahoo.com/search;_ylt=AwrjZGLYn.VlPTMT2llXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1BOTDBjYlhSUWthZXcyT1gzeXpySUEEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIzBHF1ZXJ5A211bHRhbiUyMHBha2lzdGFuJTIwd2VhdGhlcgR0X3N0bXADMTcwOTU0ODI1Nw--?p=multan+pakistan+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='d-f ai-s').text
    return p;

def pakistan_vehari():
    url = 'https://search.yahoo.com/search;_ylt=Awr99XtcouVldz8TihNXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA0FIb2JFNkFmU0RlekFNNG44OW56eEEEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzEEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIzBHF1ZXJ5A3ZlaGFyaSUyMHBha2lzdGFuJTIwd2VhdGhlcgR0X3N0bXADMTcwOTU0ODc1MQ--?p=vehari+pakistan+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry=&mkr=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    vehari=soup.find('div',class_='d-f ai-s').text
    return vehari;

# sports news
def pak_sports_news():
    url = 'https://a-sports.tv/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('h3',class_="entry-title td-module-title").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")        

def pak_sports_news1():
    url = 'https://dunyanews.tv/en/Cricket'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="sectionBody").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")        

def pak_sports_news2():
    url = 'https://www.samaa.tv/sports'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_="text").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")

def pak_Economy():
    url = 'https://lahorenews.tv/index.php/Business/6/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('a',class_='px-2').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}") 
def pak_Economy1():
    url = 'https://www.express.pk/business/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('h1',class_="title").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")        
    
def pak_Economy3():
    url = 'https://92newshd.tv/category/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('a',class_="post_link").text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
    
    
    
  
        
 