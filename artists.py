from api import API


class Artist(API):
    def __int__(self, api_key, content="json", timeout=5, sleep_time=1.5):
        super().__init__(api_key, content, timeout, sleep_time)

    def get_artist(self, mbid):
        """ Get Artist Info """
        path = "1.0/artist/{}".format(mbid)
        return self._make_request(path)