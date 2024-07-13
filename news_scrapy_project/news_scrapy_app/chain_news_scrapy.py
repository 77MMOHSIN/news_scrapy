import requests
from bs4 import BeautifulSoup
def chain_politic():
    url = 'https://www.cgtn.com/politics'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="bottom_content_item_6_2_1 cg-newsWrapper-in")
    a=chain.text
    
    return a

def chain_politic1():
    url = 'https://www.globaltimes.cn/china/politics/index.html'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="common_title")
    a=chain.text
    return a


def chain_politic2():
    url = 'https://chinadigitaltimes.net/china-news/main/politics/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h2', class_="post-title entry-title")
    a=chain.text
    return a


# chain_Economy
def chain_Economy():
    url = 'https://www.ecns.cn/business/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('ul', class_="bizlst dashedlne mart5 overhid")
    a=chain.text
    return a
def chain_Economy1():
    url = 'https://www.cgtn.com/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h3', class_="left_headline_5_1 news-headline")
    a=chain.text
    return a
# chain Sports
def chain_sports():
    url = 'https://www.cgtn.com/sports'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h3', class_="news-headline headline-area")
    a=chain.text
    return a

def chain_sports1():
    url = 'https://www.foxsports.com/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="hc-item")
    a=chain.text
    return a
def chain_sports2():
    url = 'https://www.eurosport.com/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h3', class_="card-hover-underline font-bold -md:caps-s6-fx md-lg:caps-s6-fx lg:caps-s6-fx -md:lines-2 md-lg:lines-3 lg:lines-3 text-onLight-02")
    a=chain.text
    return a

def chain_weather1():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=Beijing+today+weather'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def chain_weather2():
    url = 'https://search.yahoo.com/search;_ylt=Awr48o1XsAJm1CgA.ipXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA0lPcUhBMGRFU3JhQnB6Lm9ienNZY0EEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIyBHF1ZXJ5A1NoYW5naGFpJTIwdG9kYXklMjB3ZWF0aGVyBHRfc3RtcAMxNzExNDUyNjU2?p=Shanghai+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a

def chain_weather3():
    url = 'https://search.yahoo.com/search;_ylt=Awr49WpWsQJm.RICGvZXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkAzNrOUsuMnNxUzlTREx1Y2JmSnJ6REEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIzBHF1ZXJ5A0d1YW5nemhvdSUyMHRvZGF5JTIwd2VhdGhlcgR0X3N0bXADMTcxMTQ1MzAwMQ--?p=Guangzhou+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def chain_weather4():
    url = 'https://search.yahoo.com/search;_ylt=AwrOoxTKswJmrTUCgj5XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2Nqa2l4eXBBUlB5OE9CNHAuSmtUNUEEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMyMQRxdWVyeQNUaWFuamluJTIwdG9kYXklMjB3ZWF0aGVyBHRfc3RtcAMxNzExNDUzMzI1?p=Tianjin+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a

def chain_weather5():
    url = 'https://search.yahoo.com/search;_ylt=AwrO_y3ptAJmLC0CwtpXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1dNcFFPLkNWU251R2VTNEtVdjdnN0EEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMyMwRxdWVyeQNDaG9uZ3FpbmclMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE0NTM2ODM-?p=Chongqing+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a

def chain_time():
    url = 'https://www.timeanddate.com/worldclock/china'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',class_="h1")
    a=chain.text
    return a
def chain_time1():
    url = 'https://www.timeanddate.com/worldclock/china'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',id="ctdat")
    a=chain.text
    return a

def us_time():
    url = 'https://www.timeanddate.com/worldclock/@6252001'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',class_="h1")
    a=chain.text
    return a
def us_time1():
    url = 'https://www.timeanddate.com/worldclock/@6252001'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',id="ctdat")
    a=chain.text
    return a
def aus_time():
    url = 'https://www.timeanddate.com/worldclock/australia/sydney'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',class_="h1")
    a=chain.text
    return a
def aus_time1():
    url = 'https://www.timeanddate.com/worldclock/australia/sydney'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',id="ctdat")
    a=chain.text
    return a
def nz_time():
    url = 'https://www.timeanddate.com/worldclock/new-zealand'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',class_="h1")
    a=chain.text
    return a 
def nz_time1():
    url = 'https://www.timeanddate.com/worldclock/new-zealand'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',id="ctdat")
    a=chain.text
    return a
def pk_time():
    url = 'https://www.timeanddate.com/worldclock/pakistan'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',class_="h1")
    a=chain.text
    return a 
def pk_time1():
    url = 'https://www.timeanddate.com/worldclock/pakistan'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('span',id="ctdat")
    a=chain.text
    return a
