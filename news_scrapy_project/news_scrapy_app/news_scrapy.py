import requests
from bs4 import BeautifulSoup



# pakistan news


def scrape_pakistan():
    url = 'https://www.aljazeera.com/opinions/2024/2/29/pakistan-when-a-blasphemy-accusation-is-evidence-the-sentence-often-death'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('header',class_='article-header').text
        return result;
        print(result)

        
        
        # Extract data using Beautiful Soup
        # Example:
        # titles = soup.find_all('h2', class_='title')
        # data = [title.text for title in titles]
        
    else:
        raise Exception(f"Failed to fetch data from {url}")

def scrape_pakistan2():
    url = 'https://arynews.tv/pakistan-day-being-celebrated-with-traditional-zeal/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result=soup.find('h1',class_='tdb-title-text')
        return result;
   
# def scrape_pakistan3():
#     url = 'https://www.aljazeera.com/news/2024/2/26/ex-pm-nawazs-daughter-is-pakistans-first-female-provincial-chief-minister'
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         result=soup.find('header',class_='article-header').text
        
#         return result;        
#     else:
#         raise Exception(f"Failed to fetch data from {url}")
# def scrape_pakistan4():
#     url = 'https://www.bbc.com/news/world-asia-68313625'
#     headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}


#     response = requests.get(url,headers=headers)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         result=soup.find('h1',class_="sc-82e6a0ec-0 fxXQuy").text
        
#         return result;        
#     else:
#         raise Exception(f"Failed to fetch data from {url}")
# def scrape_pakistan5():
#     url = 'https://www.bbc.com/news/world-asia-68462846'
#     headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

#     response = requests.get(url,headers=headers)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         p=soup.find('header',class_='ssrcss-3j32hl-LegacyHeaderWrapper e149gcku1').text
#         return p;
    
#     else:
#         raise Exception(f"Failed to fetch data from {url}")    

def scrape_gaza():
    url = 'https://www.aljazeera.com/news/liveblog/2024/3/4/israels-war-on-gaza-live-israel-repeats-attacks-as-children-die-of-hunger'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        p=soup.find('div',class_='article-header').text
        return p;
    else:
        raise Exception(f"Failed to fetch data from {url}")    
def scrape_gaza1():
    url = 'https://www.aljazeera.com/news/liveblog/2024/3/5/israels-war-on-gaza-live-israeli-attacks-on-aid-seekers-continue'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        p=soup.find('h1',class_='compact-featured-area__title').text
        return p;
    
    else:
        raise Exception(f"Failed to fetch data from {url}")    
  
    #pakistan weather  

 
# def pakistan_sports():
#     url = 'https://a-sports.tv/psl-9-islamabad-united-against-peshawar-zalmi/'
#     headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
#     response = requests.get(url,headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     sports=soup.find('div', class_='tdb-block-inner td-fix-index')
#     a=sports.text
#     return a;
 
#  indian news
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

# china news starts
def china_politics():
    url = 'https://www.bbc.com/news/uk-wales-68471131'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('header', class_="ssrcss-3j32hl-LegacyHeaderWrapper e149gcku1")
    a=indian.text
    return a
def china_politics1():
    url = 'https://www.bbc.com/news/world-asia-china-63310524'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('header', class_="ssrcss-3j32hl-LegacyHeaderWrapper e149gcku1")
    a=indian.text
    return a
def china_politics2():
    url ='https://www.aljazeera.com/news/2023/6/18/uss-blinken-lands-in-china-but-hopes-for-breakthrough-low'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('header', class_="article-header")
    a=indian.text
    return a
def china_politics3():
    url ='https://www.aljazeera.com/news/2023/4/16/putin-meets-with-chinas-defense-minister-in-moscow'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('header', class_="article-header")
    a=indian.text
    return a
def china_politics4():
    url ='https://www.foxnews.com/category/world/world-regions/china'
    headers={'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    indian=soup.find('div', class_="embed-media advanced")
    a=indian.text
    return a
