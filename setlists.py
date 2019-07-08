from api import API
import math


class Setlists(API):
    def __int__(self, api_key, content="json", timeout=5, sleep_time=1.5):
        super().__init__(api_key, content, timeout, sleep_time)

    def get_setlists(self, mbid, page=1):
        """" Get 20 set lists for the supplied artist and page """
        path = "1.0/artist/{}/setlists?p={}".format(mbid, page)
        return self._make_request(path)

    def get_all_setlists(self, mbid):
        """ Get all of an Artist's setlists """
        first_set = self.get_setlists(mbid, 1)
        data = self._json_loads(first_set)
        pages = math.ceil(data["total"] / 20) - 1
        print("{} total pages".format(pages))
        for i in range(pages):
            set = self.get_setlists(mbid, i + 2)
            set_data = self._json_loads(set)
            data["setlist"] = data["setlist"] + set_data["setlist"]
        return data
