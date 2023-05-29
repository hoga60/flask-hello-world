import requests
from bs4 import BeautifulSoup
def read( word ):
    url = f'https://ideaking.info/searchresult/page=1&keywords={word}&type=image'
    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('div', id='search-results-gallery')
    pic = data.find('img')['src']
    return pic