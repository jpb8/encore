import requests
import time
import json


class API:
    """ setlist.fm API wrapper """
    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {'application': 'PythonWrapper'}

    def __init__(self, api_key, content="json", timeout=5, sleep_time=1.25):
        """ JsonODDS API Constructor
        :param api_key: key provided by Sportradar, specific to the sport's API
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests, (free min is 1 second)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.api_key = api_key
        self.content = "application/{}".format(content)
        self.headers = {"x-api-key": api_key, "Accept": self.content}
        self.api_root = 'https://api.setlist.fm/rest/'
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET', params=None):
        """ Make a GET or POST request to the API """
        time.sleep(self._sleep_time)
        full_uri = self.api_root + path
        response = self.session.request(method,
                                        full_uri,
                                        timeout=self.timeout,
                                        headers=self.headers,
                                        params=params)
        return response

    @staticmethod
    def _json_loads(response):
        data = response.content
        return json.loads(data.decode("utf-8"))
