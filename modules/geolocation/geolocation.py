import json
import urllib.request


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
        for i in range(len(self._keys)):
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + urllib.request.quote(s) + \
                  '&types=geocode&key=' + self._keys[i]

            r = urllib.request.urlopen(url)
            r = json.loads(r.read().decode('utf-8'))

            if r['status'] == 'OVER_QUERY_LIMIT':
                self._keys.remove(self._keys[i])
            else:
                break

        return r['results'][0]['geometry']['location']["lat"], r['results'][0]['geometry']['location']["lng"]
