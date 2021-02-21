import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_arpcd_pigeons(ring):
    arpcd = 'http://www.arpcd.com/index.php?option=com_pigeon&view=resultform'

    page = requests.post(arpcd, data={'ban_id': str(ring)})

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all('table')
    df = pd.DataFrame()
    try:
        df = pd.read_html(str(table[1]))[0]
    except:
        df = pd.DataFrame()
        print('get_brpoa_pigeons NOT FOUND',ring)

    return df