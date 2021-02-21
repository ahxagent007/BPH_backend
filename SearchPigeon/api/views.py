from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
from SearchPigeon.api.arpcd_scrap import get_arpcd_pigeons
from SearchPigeon.api.brpfc_scrap import get_brpfc_pigeons
from SearchPigeon.api.brpoa_scrap import get_brpoa_pigeons
from SearchPigeon.api.old_db_api import OldDBSearch


@api_view(['GET'])
def search_pigeon(request):
    try:
        ring_no = request.POST.get('ring_no')

        arcpd_df = get_arpcd_pigeons(ring_no)
        brpfc_df = get_brpfc_pigeons(ring_no)
        brpoa_df = get_brpoa_pigeons(ring_no)
        old_bd_df = OldDBSearch(ring_no)

        arcpd_df.rename(
            columns={"BAN":"PigeonRingNumber", "Rank":"Position", "Race Spot":"RaceName", "Name & ID":"OwnerName",
                     "Velocity":"PigeonVelocity", "No of Pigeon":"TotalPigeons", "Date":"RaceDate",
                     "Distance [KM]":"Distance"}, inplace=True)
        arcpd_df['ClubName'] = 'ARPCD'

        brpfc_df.rename(
            columns={"BAN":"PigeonRingNumber", "Rank":"Position", "Race Spot":"RaceName", "Name & ID":"OwnerName",
                     "Velocity":"PigeonVelocity", "No of Pigeon":"TotalPigeons", "Date":"RaceDate",
                     "Distance [KM]":"Distance"}, inplace=True)
        brpfc_df['ClubName'] = 'BRPFC'

        brpoa_df.rename(
            columns={"BAN":"PigeonRingNumber", "Rank":"Position", "Race Spot":"RaceName", "Name":"OwnerName",
                     "Velocity":"PigeonVelocity", "No of Pigeon":"TotalPigeons", "Date":"RaceDate",
                     "Distance [KM]":"Distance"}, inplace=True)
        brpoa_df['ClubName'] = 'BRPOA'

        all_result_df = pd.concat([arcpd_df, brpfc_df, brpoa_df, old_bd_df], ignore_index=True)
        return JsonResponse({'status':1, 'msg':'Data Load', 'records':all_result_df.values.tolist()})
    except:
        return JsonResponse({'status' : 0, 'msg':'Missing'})

    return JsonResponse({'msg' : 'OK'})