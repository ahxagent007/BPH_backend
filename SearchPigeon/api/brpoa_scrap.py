import requests
from bs4 import BeautifulSoup

brpoa = 'http://www.brpoa.com.bd/index.php/search-pigeon-race-result'

page = requests.post(brpoa, data={'ban_id':'11'})

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
