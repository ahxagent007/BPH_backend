import requests
import json
import pandas as pd

def OldDBSearch(ringNo):
    old_url = "http://bdracingpigeon.bdpigeonweb.com/Pigeons/search.php?s=" + ringNo;
    response = requests.get(old_url)
    json_data = json.loads(response.content)
    old_df = pd.DataFrame(json_data['records'])
    return old_df

OldDBSearch('111112')