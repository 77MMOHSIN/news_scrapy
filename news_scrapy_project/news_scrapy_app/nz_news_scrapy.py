import requests
from bs4 import BeautifulSoup

def nz_politics():
    url = 'https://www.newshub.co.nz/home/politics.html'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='c-LargeGridItem').text
        
        
        return result;          
    else:
        raise Exception(f"Failed to fetch data from {url}")


def nz_politics1():
    url = 'https://www.rnz.co.nz/news/political'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='o-digest o-digest--news o-digest--extended lead-story u-blocklink has-thumbnail').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")

def nz_politics3():
    url = 'https://www.1news.co.nz/tags/politics/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='story').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
        
def nz_sports():
    url = 'https://www.1news.co.nz/sport/cricket/'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='story').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
def nz_sports1():
    url = 'https://www.odt.co.nz/sport'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='col-sm-6 second-column').text
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
def nz_sports2():
    url = 'https://www.newshub.co.nz/home/sport.html'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('h3',class_='c-NewsTile-title').text
        
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
                                                  

def nz_economy():
    url = 'https://www.newshub.co.nz/home/money/Economy.html'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('h2',class_='c-NewsTile-title').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
                                
def nz_economy2():
    url = 'https://www.rnz.co.nz/news/business'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('div',class_='o-digest o-digest--news o-digest--extended lead-story u-blocklink has-thumbnail').text
        
        
        return result;        
    else:
        raise Exception(f"Failed to fetch data from {url}")
                                                            
def nz_weather():
    url = 'https://search.yahoo.com/search?fr=mcafee&type=E210US91215G0&p=Auckland+today+weather'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
                                
def nz_weather1():
    url = 'https://search.yahoo.com/search;_ylt=Awr99rweXQZmlQQA2llXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA3dMRlJyMUVBUld1SUZMeEEzNmpCVEEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI0BHF1ZXJ5A1dlbGxpbmd0b24lMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE2OTM3NzY-?p=Wellington+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def nz_weather2():
    url = 'https://search.yahoo.com/search;_ylt=AwrjZEY1XwZm5gcBWphXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2pPTEw0TGliUVRLdGRvdjNTZnRIRkEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI2BHF1ZXJ5A0NocmlzdGNodXJjaCUyMHRvZGF5JTIwd2VhdGhlcgR0X3N0bXADMTcxMTY5NDAwMA--?p=Christchurch+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a    

def nz_weather3():
    url = 'https://search.yahoo.com/search;_ylt=Awr99rwVYAZmfn8BClJXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1E5UXhhX050VEhlUUxHbUdiVEp0RkEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIyBHF1ZXJ5A0hhbWlsdG9uJTIwdG9kYXklMjB3ZWF0aGVyBHRfc3RtcAMxNzExNjk0MjI3?p=Hamilton+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def nz_weather4():
    url = 'https://search.yahoo.com/search;_ylt=AwrOsnj4YAZmQEoAAgBXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA2RnV1ZaSE5CU09HcHJDMDI1WFY5NUEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIyBHF1ZXJ5A1RhdXJhbmdhJTIwdG9kYXklMjB3ZWF0aGVyBHRfc3RtcAMxNzExNjk0NDA0?p=Tauranga+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a
def nz_weather5():
    url = 'https://search.yahoo.com/search;_ylt=AwrO_.apYQZmuKcAipBXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA21jYWZlZQRmcjIDc2ItdG9wBGdwcmlkA1ZiMlpFTzJwU0NLU2o3ZzRaMlpkeUEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5A0R1bmVkaW4lMjB0b2RheSUyMHdlYXRoZXIEdF9zdG1wAzE3MTE2OTQ2NTI-?p=Dunedin+today+weather&fr=mcafee&type=E210US91215G0&fr2=sb-top&iscqry='
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    chain=soup.find('div', class_="d-f ai-s")
    a=chain.text
    return a                             