import requests
from bs4 import BeautifulSoup
def aus_politics():
    url = 'https://www.skynews.com.au/australia-news/politics'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h4', class_="storyblock_title")
    a=chain.text
    return a

def aus_politics1():
    url = 'https://www.9news.com.au/politics'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="story__details")
    a=chain.text
    return a

def aus_politics2():
    url = 'https://www.sbs.com.au/news/topic/politics'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h3', class_="MuiTypography-root MuiTypography-h6 e1o065bq2 css-f5ktw1")
    a=chain.text
    return a

# sports news
def aus_sports():
    url = 'https://wwos.nine.com.au/cricket'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="story-block__info-container")
    a=chain.text
    return a

def aus_sports1(): 
    url = 'https://www.skynews.com.au/australia-news/sport'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h4', class_="storyblock_title")
    a=chain.text
    return a
def aus_sports2(): 
    url = 'https://www.espn.in/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    parent=soup.find('div',class_='contentItem__titleWrapper')
    
    a=parent.text
    return a


def aus_economy():
    url = 'https://www.skynews.com.au/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h4', class_="storyblock_title")
    a=chain.text
    return a
def aus_economy1():
    url = 'https://7news.com.au/business/economy'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('h2', class_="Card-Headline css-yha00h-StyledHeadline e1w8lw9x9")
    a=chain.text
    return a
def aus_economy2():
    url = 'https://www.abc.net.au/news/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    aus=soup.find('span', class_="KeyboardFocus_keyboardFocus__NLJda")
    a=aus.text
 
    return a
def aus_weather():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=Melbourne+today+weather'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather1():
    url = 'https://search.yahoo.com/search;_ylt=AwrEpf6WAwVmmQQA0oRXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA0pmSDRKeTY1U0Y2UTN6N1hZVF9zR0EEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIwBHF1ZXJ5A1N5ZG5leSUyMHRvZGF5JTIwd2VhdGhlcgR0X3N0bXADMTcxMTYwNjQyNA--?p=Sydney+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather2():
    url = 'https://search.yahoo.com/search?fr2=p%3ads%2cv%3aomn%2cm%3asa%2cbrws%3achrome%2cpos%3a1&fr=mcafee&type=E210US91215G0&p=brisbane+weather'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather3():
    url = 'https://search.yahoo.com/search;_ylt=AwrEtkP9CQVmugQAsjZXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2J0VGg3cHE3U1EuczlVZUxfX2h3akEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzE5BHF1ZXJ5A1BlcnRoJTIwdG9kYXklMjB3ZWF0aGVyBHRfc3RtcAMxNzExNjA2NjQy?p=Perth+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather4():
    url = 'https://search.yahoo.com/search;_ylt=AwrEr1bXCgVm6AQAqt5XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1BxS3RfZjYuUzhxLjROSS50V2NvQ0EEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI0BHF1ZXJ5A1dvbGxvbmdvbmclMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE2MDY3Mzc-?p=Wollongong+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather5():
    url = 'https://search.yahoo.com/search;_ylt=AwrFZmg2CwVmYAQAihNXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA19JaGRiYW5tUjlTelVfcFJsaTBXUEEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI0BHF1ZXJ5A0xhdW5jZXN0b24lMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE2MDY4Nzk-?p=Launceston+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def aus_weather6():
    url = 'https://search.yahoo.com/search;_ylt=AwrFARLECwVmhwQAKiNXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2dNOU4zTVZXUmhPYnRkbTEweGM3T0EEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5A0dlZWxvbmclMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE2MDY5OTg-?p=Geelong+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a



