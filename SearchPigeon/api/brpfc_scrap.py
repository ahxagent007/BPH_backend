import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_brpfc_pigeons(ring):
    brpfc = 'http://www.brpfc.org/index.php/search-pigeon-race-result'

    page = requests.post(brpfc, data={'ban_id': str(ring)})

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all('table')

    try:
        df = pd.read_html(str(table[1]))[0]
    except:
        df = None
        print('get_brpfc_pigeons NOT FOUND',ring)

    return df