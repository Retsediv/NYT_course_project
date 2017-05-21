import json
import urllib.request
import urllib.error
from time import sleep


class Geolocation:
    """ Getting coordinates for places"""

    def __init__(self, keys):
        """
        Create instance of class and set a list of api keys

        :param keys: list of api keys
        :type keys: list
        """
        self._keys = keys

    def get_geo(self, s):
        """
        Return pair of coordinates latitude, longitude for given place(s)

        :param str s: place(city)
        :return tuple: lat, lng
        """
        try:
            i = 0
            while len(self._keys):
                sleep(0.5)

                url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + urllib.request.quote(s) + \
                      '&types=geocode&key=' + self._keys[i]

                r = urllib.request.urlopen(url)
                r = json.loads(r.read().decode('utf-8'))

                print(r['status'])

                if r['status'] == 'OVER_QUERY_LIMIT' or r['status'] == 'REQUEST_DENIED':
                    self._keys.pop(0)
                    continue

                if r['status'] != 'ZERO_RESULTS':
                    return r['results'][0]['geometry']['location']["lat"], r['results'][0]['geometry']['location']["lng"]
                else:
                    return 0, 0
        except urllib.error.HTTPError:
            return 0, 0
