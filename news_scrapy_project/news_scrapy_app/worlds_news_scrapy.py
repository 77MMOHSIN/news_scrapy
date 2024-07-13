import requests
from bs4 import BeautifulSoup

def Asia():
    url = 'https://www.aljazeera.com/asia/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='gc__header-wrap').text
    return p;

def Asia1():
    url = 'https://edition.cnn.com/world/asia'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='card container__item container__item--type-media-image container__item--type-section container_lead-plus-headlines__item container_lead-plus-headlines__item--type-section').text
    return p;
def Asia3():
    url = 'https://www.theguardian.com/world/asia'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('li',class_='dcr-1qmyfxi').text
    return p;

# europe news start
def Europe():
    url = 'https://edition.cnn.com/world/europe'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__text container_lead-plus-headlines-with-images__text').text
    return p;

def Europe1():
    url = 'https://www.aljazeera.com/europe/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='gc__content').text
    return p;
def Europe2():
    url = 'https://www.bbc.com/news/world/europe'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='sc-4fedabc7-1 kbvCmj').text
    return p

# africa

def Africa():
    url = 'https://edition.cnn.com/world/africa'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__text container_lead-plus-headlines-with-images__text').text
    return p
def Africa1():
    url = 'https://www.aljazeera.com/africa/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='gc__content').text
    return p

def Africa2():
    url = 'https://www.bbc.com/news/world/africa'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='sc-4fedabc7-1 kbvCmj').text
    return p

def Uk():
    url = 'https://edition.cnn.com/world/united-kingdom'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__headline container_lead-plus-headlines-with-images__headline').text
    return p

def Uk1():
    url = 'https://news.sky.com/uk'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='ui-story-content').text
    return p
def Uk2():
    url = 'https://www.channel4.com/news/uk'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('span',class_='headline').text
    return p
def US():
    url = 'https://www.aljazeera.com/us-canada/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('h3',class_='gc__title').text
    return p

def US1():
    url = 'https://www.bbc.com/news/us-canada'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='sc-4fedabc7-1 kbvCmj').text
    return p
def US2():
    url = 'https://www.cbc.ca/news'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='primaryHeadline desktopHeadline').text
    return p
def AS1():
    url = 'https://www.bbc.com/news/world/australia'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='sc-4fedabc7-1 kbvCmj').text
    return p
def AS2():
    url = 'https://edition.cnn.com/world/australia'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='container__text container_lead-plus-headlines-with-images__text').text
    return p
def AS3():
    url = 'https://www.sbs.com.au/news'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url ,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p=soup.find('div',class_='MuiCardContent-root e1o065bq4 css-o210ao').text
    return p

