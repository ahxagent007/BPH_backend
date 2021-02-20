from django.db import models

class pigeon(models.Model):
    PigeonRingNumber = models.CharField(max_length=200)
    Position = models.IntegerField()
    RaceName = models.CharField(max_length=200)
    OwnerName = models.CharField(max_length=200)
    ClubName = models.CharField(max_length=200)
    PigeonVelocity = models.FloatField()
    TotalPigeons = models.IntegerField()
    RaceDate = models.CharField(max_length=200)
    Distance = models.FloatField()