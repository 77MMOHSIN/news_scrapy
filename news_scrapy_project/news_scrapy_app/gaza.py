import requests
from bs4 import BeautifulSoup



def scrape_gaza5():
    url = 'https://www.aljazeera.com/'
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        p=soup.find('h3',class_='article-card__title').text
        print(p)
        print('pakistan  is beautiful news')
        return p;
    else:
        raise Exception(f"Failed to fetch data from {url}")
def scrape_gaza6():
    url = 'https://arynews.tv/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

    
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        p=soup.find('h3',class_='entry-title td-module-title').text
        print(p)
        print('pakistan is beautiful news')
        return p;
    
    else:
        raise Exception(f"Failed to fetch data from {url}")
