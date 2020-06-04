# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim
import pandas as pd


geolocator = Nominatim(user_agent="my_app/1", format_string="%s, Cleverland OH")
address, (latitude, longitude) = geolocator.geocode("11111 Euclide Ave")


