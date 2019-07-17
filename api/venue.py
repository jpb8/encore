from api.api import API


class Venue(API):
    def __int__(self, api_key, content="json", timeout=5, sleep_time=0.75):
        super().__init__(api_key, content, timeout, sleep_time)

    def info(self, venue_id):
        path = "1.0/venue/{}".format(venue_id)
        return self._make_request(path)

    def setlists(self, venue_id):
        path = "1.0/venue/{}/setlists".format(venue_id)
        return self._make_request(path)