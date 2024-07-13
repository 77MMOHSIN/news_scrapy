import requests
from bs4 import BeautifulSoup

def Us_politics():
    url = 'https://edition.cnn.com/politics'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__text container_lead-plus-headlines__text').text
    return p;
def Us_politics1():
    url = 'https://edition.cnn.com/us'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='card container__item container__item--type-media-image container__item--type-section container_lead-plus-headlines__item container_lead-plus-headlines__item--type-section').text
    return p;
def Us_politics2():
    url = 'https://www.foxnews.com/politics'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('article',class_='article story-1').text
    return p;
def Us_politics3():
    url = 'https://www.cbsnews.com/politics/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('h4',class_='item__hed').text
    return p;

def Us_politics4():
    url ='https://www.nbcnews.com/politics'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='multi-up__article multi-up__tease-card--three-up-main').text
    return p;
# us Sports
def Us_sports():
    url ='https://www.cbssports.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='top-marquee-main').text
    return p;

def Us_sports1():
    url ='https://www.sportingnews.com/us'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='lead-item__title').text
    return p;

def Us_sports2():
    url ='https://www.foxnews.com/sports'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='info').text
    return p;

def Us_economy():
    url ='https://www.nbcnews.com/business'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('article',class_='tease-card tease-card__content tease-card__content--news').text
    return p;

def Us_economy1():
    url ='https://www.pbs.org/newshour/economy'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('article',class_='card-lg').text
    return p;

def Us_economy2():
    url ='https://edition.cnn.com/business'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__headline container_lead-plus-headlines-with-images__headline').text
    return p;

def Us_weather():
    url ='https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=New+York+City+today+weather'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;
def Us_weather1():
    url ='https://search.yahoo.com/search;_ylt=Awr.1U_DoANmLwQA4i5XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA0dwZjRLNVdmVGZ5a2ZwWjk3ZVpFSEEEbl9yc2x0AzAEbl9zdWdnAzMEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI1BHF1ZXJ5A0xvcyUyMEFuZ2VsZXMlMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE1MTQ2MDU-?p=Los+Angeles+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;
def Us_weather2():
    url ='https://search.yahoo.com/search;_ylt=Awrgw81xpANmCgQACs9XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkAzNuZi5La3U3UlRTN0JKWHZUUDhnb0EEbl9yc2x0AzAEbl9zdWdnAzcEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5A0NoaWNhZ28lMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE1MTUyMTA-?p=Chicago+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;
def Us_weather3():
    url ='https://search.yahoo.com/search;_ylt=Awr98IqwpQNmlm8AWhtXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA0FUbzZidTFSVGJHQ1lac05ITGZQTEEEbl9yc2x0AzAEbl9zdWdnAzQEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5A0hvdXN0b24lMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE1MTU3MTk-?p=Houston+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;
def Us_weather4():
    url ='https://search.yahoo.com/search;_ylt=AwrOuoYVqANmaAQAEidXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA3dHbUZmOGdlUXcyN0I4RU4wYjNtMUEEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMyNgRxdWVyeQNQaGlsYWRlbHBoaWElMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE1MTU5MjM-?p=Philadelphia+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;
def Us_weather5():
    url ='https://search.yahoo.com/search;_ylt=AwrO7k59qANmUgQAClJXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA3B1VW50a080Um9tSUxVVWltRFZGM0EEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5A1Bob2VuaXglMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE1MTYwMDE-?p=Phoenix+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div', class_="d-f ai-s").text
    return p;







