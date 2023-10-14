import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'
response = requests.get(URL)
html = response.text

soup = BS(html,'html.parser')
container = soup.find('div', {'class':'container body-container'})
main = container.find('div', {'class': 'main-content'})
listing = main.find('div',{'class':'listing-wrapper'})
post = listing.find_all('div',{'class':'listign'})
for posts in post:
    side = posts.find('div',{'class':'left-side'})
    title = side.find('p').text.strip()
    print(title)






















