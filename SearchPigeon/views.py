from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from SearchPigeon.api.arpcd_scrap import get_arpcd_pigeons
from SearchPigeon.api.brpfc_scrap import get_brpfc_pigeons
from SearchPigeon.api.brpoa_scrap import get_brpoa_pigeons
from SearchPigeon.models import pigeon


def ARPCD(request):
    for i in range(6000,6000):
        arcpd_df = get_arpcd_pigeons(i)
        print(i,'***************************************** ARPCD')
        for index, row in arcpd_df.iterrows():
            pg = pigeon.objects.filter(PigeonRingNumber= row['BAN'], PigeonVelocity= row['Velocity'], RaceDate=row['Date'])
            if pg.count() == 0:
                print(i, '###', row['Rank'], row['BAN'], row['Race Spot'], row['Name & ID'], 'ARPCD', row['Velocity'], row['No Of Pigeon'], row['Date'], row['Distance [KM]'])
                pigeon.objects.create(
                    PigeonRingNumber = row['BAN'],
                    Position = row['Rank'],
                    RaceName = row['Race Spot'],
                    OwnerName = row['Name & ID'],
                    ClubName = 'ARPCD',
                    PigeonVelocity = row['Velocity'],
                    TotalPigeons = row['No Of Pigeon'],
                    RaceDate = row['Date'],
                    Distance = row['Distance [KM]'])
            else:
                print(i, '### EXISTS :: :: :: :: :: :: ')

    return HttpResponse('ARCPD DONE')

def BRPFC(request):
    for i in range(10,10):
        brpfc_df = get_brpfc_pigeons(i)
        print(i,'***************************************** BRPFC')
        print(brpfc_df.columns)
        if not brpfc_df.empty:
            for index, row in brpfc_df.iterrows():
                pg = pigeon.objects.filter(PigeonRingNumber= row['Pigeon Details...']['BAN'], PigeonVelocity= row['Pigeon Details...']['Velocity'], RaceDate=row['Pigeon Details...']['Date'])
                if pg.count() == 0:
                    print(i, '###', row['Pigeon Details...']['Rank'], row['Pigeon Details...']['BAN'], row['Pigeon Details...']['Race Spot'], row['Pigeon Details...']['Name & ID'],
                          'BRPFC', row['Pigeon Details...']['Velocity'], row['Pigeon Details...']['No of Pigeon'], row['Pigeon Details...']['Date'], row['Pigeon Details...']['Distance [KM]'])
                    pigeon.objects.create(
                        PigeonRingNumber = row['Pigeon Details...']['BAN'],
                        Position = row['Pigeon Details...']['Rank'],
                        RaceName = row['Pigeon Details...']['Race Spot'],
                        OwnerName = row['Pigeon Details...']['Name & ID'],
                        ClubName = 'BRPFC',
                        PigeonVelocity = row['Pigeon Details...']['Velocity'],
                        TotalPigeons = row['Pigeon Details...']['No of Pigeon'],
                        RaceDate = row['Pigeon Details...']['Date'],
                        Distance = row['Pigeon Details...']['Distance [KM]'])
                else:
                    print(i, '### EXISTS :: :: :: :: :: :: ')

    return HttpResponse('BRPFC DONE')

def BRPOA(request):
    for i in range(10,10):
        brpoa_df = get_brpoa_pigeons(i)
        print(brpoa_df.columns)
        print(i,'***************************************** BRPOA')
        if not brpoa_df.empty:
            for index, row in brpoa_df.iterrows():
                pg = pigeon.objects.filter(PigeonRingNumber= row['Pigeon Details...']['BAN'], PigeonVelocity= row['Pigeon Details...']['Velocity'], RaceDate=row['Pigeon Details...']['Date'])
                if pg.count() == 0:
                    print(i, '###', row['Pigeon Details...']['Rank'], row['Pigeon Details...']['BAN'], row['Pigeon Details...']['Race Spot'], row['Pigeon Details...']['Name'],
                        'BRPOA', row['Pigeon Details...']['Velocity'], row['Pigeon Details...']['No of Pigeon'], row['Pigeon Details...']['Date'], row['Pigeon Details...']['Distance [KM]'])
                    pigeon.objects.create(
                        PigeonRingNumber = row['Pigeon Details...']['BAN'],
                        Position = row['Pigeon Details...']['Rank'],
                        RaceName = row['Pigeon Details...']['Race Spot'],
                        OwnerName = row['Pigeon Details...']['Name'],
                        ClubName = 'BRPOA',
                        PigeonVelocity = row['Pigeon Details...']['Velocity'],
                        TotalPigeons = row['Pigeon Details...']['No of Pigeon'],
                        RaceDate = row['Pigeon Details...']['Date'],
                        Distance = row['Pigeon Details...']['Distance [KM]'])
                else:
                    print(i, '### EXISTS :: :: :: :: :: :: ')

    return HttpResponse('BRPOA DONE')
