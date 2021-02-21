import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_brpoa_pigeons(ring):
    brpoa = 'http://www.brpoa.com.bd/index.php/search-pigeon-race-result'

    page = requests.post(brpoa, data={'ban_id': str(ring)})

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all('table')
    df = pd.DataFrame()
    try:
        df = pd.read_html(str(table[1]))[0]
    except:
        df = pd.DataFrame()
        print('get_brpoa_pigeons NOT FOUND',ring)

    return df