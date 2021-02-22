from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SearchPigeon.api.arpcd_scrap import get_arpcd_pigeons
from SearchPigeon.api.brpfc_scrap import get_brpfc_pigeons
from SearchPigeon.api.brpoa_scrap import get_brpoa_pigeons
from SearchPigeon.api.old_db_api import OldDBSearch


@api_view(['GET'])
def search_pigeon(request, ring_no):
    cache_TTL = 60*60*24
    cache_data = cache.get(ring_no)
    if not cache_data == None:
        return JsonResponse({'status': 1, 'msg': 'Data Load', 'records': cache_data})
    else:

        arcpd_df = get_arpcd_pigeons(ring_no)
        brpfc_df = get_brpfc_pigeons(ring_no)
        brpoa_df = get_brpoa_pigeons(ring_no)
        old_bd_df = OldDBSearch(ring_no)

        # ARPCD - Single Index
        # BRPFC - Multi Index
        # BRPOA - Multi Index

        if not arcpd_df.empty:
            arcpd_df.rename(
                columns={"BAN": "PigeonRingNumber", "Rank": "Position", "Race Spot": "RaceName", "Name & ID": "OwnerName",
                         "Velocity": "PigeonVelocity", "No Of Pigeon": "TotalPigeons", "Date": "RaceDate",
                         "Distance [KM]": "Distance"}, inplace=True)
            arcpd_df['ClubName'] = 'ARPCD'

        if not brpfc_df.empty:
            brpfc_df = brpfc_df['Pigeon Details...']
            brpfc_df.rename(
                columns={"BAN": "PigeonRingNumber", "Rank": "Position", "Race Spot": "RaceName", "Name & ID": "OwnerName",
                         "Velocity": "PigeonVelocity", "No of Pigeon": "TotalPigeons", "Date": "RaceDate",
                         "Distance [KM]": "Distance"}, inplace=True)
            brpfc_df['ClubName'] = 'BRPFC'

        if not brpoa_df.empty:
            brpoa_df = brpoa_df['Pigeon Details...']
            brpoa_df.rename(
                columns={"BAN": "PigeonRingNumber", "Rank": "Position", "Race Spot": "RaceName", "Name": "OwnerName",
                         "Velocity": "PigeonVelocity", "No of Pigeon": "TotalPigeons", "Date": "RaceDate",
                         "Distance [KM]": "Distance"}, inplace=True)
            brpoa_df['ClubName'] = 'BRPOA'


        '''print(arcpd_df.columns)
        print(brpfc_df.columns)
        print(brpoa_df.columns)
        print(old_bd_df.columns)'''


        records = []
        for index, row in arcpd_df.iterrows():
            pgn = {
                "PigeonRingNumber": row['PigeonRingNumber'],
                "Position": row['Position'],
                "RaceName": row['RaceName'],
                "OwnerName": row['OwnerName'],
                "ClubName": row['ClubName'],
                "PigeonVelocity": row['PigeonVelocity'],
                "TotalPigeons": row['TotalPigeons'],
                "RaceDate": row['RaceDate'],
                "Distance":row['Distance']
            }
            records.append(pgn)
        for index, row in brpfc_df.iterrows():
            pgn = {
                "PigeonRingNumber": row['PigeonRingNumber'],
                "Position": row['Position'],
                "RaceName": row['RaceName'],
                "OwnerName": row['OwnerName'],
                "ClubName": row['ClubName'],
                "PigeonVelocity": row['PigeonVelocity'],
                "TotalPigeons": row['TotalPigeons'],
                "RaceDate": row['RaceDate'],
                "Distance":row['Distance']
            }
            records.append(pgn)

        for index, row in brpoa_df.iterrows():
            pgn = {
                "PigeonRingNumber": row['PigeonRingNumber'],
                "Position": row['Position'],
                "RaceName": row['RaceName'],
                "OwnerName": row['OwnerName'],
                "ClubName": row['ClubName'],
                "PigeonVelocity": row['PigeonVelocity'],
                "TotalPigeons": row['TotalPigeons'],
                "RaceDate": row['RaceDate'],
                "Distance":row['Distance']
            }
            records.append(pgn)

        for index, row in old_bd_df.iterrows():
            pgn = {
                "PigeonRingNumber": row['PigeonRingNumber'],
                "Position": row['Position'],
                "RaceName": row['RaceName'],
                "OwnerName": row['OwnerName'],
                "ClubName": row['ClubName'],
                "PigeonVelocity": row['PigeonVelocity'],
                "TotalPigeons": row['TotalPigeons'],
                "RaceDate": row['RaceDate'],
                "Distance":row['Distance']
            }
            records.append(pgn)
        cache.set(ring_no, records, cache_TTL)
        return JsonResponse({'status': 1, 'msg': 'Data Load', 'records': records})
