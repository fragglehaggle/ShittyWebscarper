import requests
import urllib.parse
from bs4 import BeautifulSoup
CMN_URL = 'https://2e.aonprd.com/' # url prefix for image linking - HTML doesn't store natively
for n in range(7,1051):
    url = 'https://2e.aonprd.com/Monsters.aspx?ID={}'.format(n)
    page = requests.get(url)
    #print(f"getting {url}")
    soup = BeautifulSoup(page.content, 'html.parser')  # I don't know currently, but I think it's just a HTML parse
    title = soup.find('h1', class_='title')  #Finds information based on the soup class parse the H1 class for the website - For AEONPRD the H1 text is the name of the monster
    IMG = soup.find_all('img', class_='thumbnail')  #Finds information from the soup parser, specifically the PNG file for monster thumbails
    if (title is not None):
        StripText = title.get_text()  # Get_text will parse the information retrieved from h1
        print(title)
    else:
        pass
    for im in IMG:
        IMG_URL = urllib.parse.urljoin(CMN_URL, im['src'])#I have no idea what im is, but it collects the information after src
        IMG_URL2 = IMG_URL.replace('\\', '/')#replaces backslashes with forwardslashes
        print(IMG_URL2)
