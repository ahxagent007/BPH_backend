# Generated by Django 3.1.7 on 2021-02-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PigeonRingNumber', models.CharField(max_length=200)),
                ('Position', models.IntegerField()),
                ('RaceName', models.CharField(max_length=200)),
                ('OwnerName', models.CharField(max_length=200)),
                ('ClubName', models.CharField(max_length=200)),
                ('PigeonVelocity', models.FloatField()),
                ('TotalPigeons', models.IntegerField()),
                ('RaceDate', models.CharField(max_length=200)),
                ('Distance', models.FloatField()),
            ],
        ),
    ]
