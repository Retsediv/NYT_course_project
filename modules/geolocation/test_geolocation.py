from modules.geolocation import Geolocation

keys = ["AIzaSyDr8AapNc0IQvG-RJKYJi7jD_BRD7izHiI", "AIzaSyBit41NBregOXu7pVcb-PTl_TEeRrfOKCg"]
geo = Geolocation(keys)
print(geo.get_geo("Lviv"))
