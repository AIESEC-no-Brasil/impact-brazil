# + 5.4400, -72.2800 = 0,   0
# -22.9027, -43.2075 = 637, 683
# -23.5337, -46.6252 = 654, 610
# -15.7797, -47.9297 = 464, 572
#
#
# latOff =  5.440000
# perLat = -0.044397
#
# longOff = -72.28000
# perLong =  0.042381
#
# (l - lO) / pL = coord
# BH = 19.9167° S, 43.9345° W = 669, 571
import re

from django.core.management import BaseCommand
import requests
from unidecode import unidecode
from bs4 import BeautifulSoup

from api.models import City


class Command(BaseCommand):
    help = "Configures each city's coordinates"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        def calc_xy(lat, lng):
            lat_off = 5.440000
            per_lat = -0.044397

            lng_off = -72.28000
            per_lng = 0.042381

            x = (lng - lng_off) / per_lng
            y = (lat - lat_off) / per_lat

            return int(round(x)), int(round(y))

        cities = City.objects.filter(mapX__exact=0, mapY__exact=0)

        for city in cities:
            city_name = unidecode(city.name).lower().replace(" ", "-")
            fetched = requests.get("http://latitudelongitude.org/br/" + city_name + "/").content
            bs = BeautifulSoup(fetched, features="html.parser")

            try:
                lat_lng_regex = '(-[\d\.]+), (-[\d\.]+)'
                results = bs.find('span', text=re.compile(lat_lng_regex))
                searched = re.search(lat_lng_regex, str(results))
                lat = searched.group(1)
                lng = searched.group(2)

                lat = float(lat)
                lng = float(lng)

                x, y = calc_xy(lat, lng)

                city.mapX = x
                city.mapY = y
                city.save()

                print(f'Set {city_name}: {lat}, {lng} => {x}, {y}')
            except Exception as e:
                print(f'{city_name} failed: {e}')
