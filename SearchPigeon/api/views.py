from django.http import JsonResponse
from rest_framework.decorators import api_view

import requests

@api_view(['GET'])
def search_pigeon(request):

    brpel = 'https://brpel.com/pigeon-database-tts'
    brpoa = 'http://www.brpoa.com.bd/index.php/search-pigeon-race-result'
    brpfc = 'http://www.brpfc.org/index.php/search-pigeon-race-result'
    arpcd = 'http://www.arpcd.com/index.php?option=com_pigeon&view=resultform'


    return JsonResponse({'msg' : 'OK'})