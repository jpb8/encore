from api import API


class Search(API):
    def __int__(self, api_key, content="json", timeout=5, sleep_time=1.5):
        super().__init__(api_key, content, timeout, sleep_time)

    def _build_params(self, page=1, **kwargs):
        """ build search parameters dictionary """
        params = {
            "p": page
        }
        for k, v in kwargs.items():
            if v:
                params[k] = v
        return params

    def artists(self, artist_mbid=None, artist_name=None, artist_tmid=None, page=1, sort="sortName"):
        """
        Search for artists, Returns in pages of 30 artists
        :param artist_mbid: MusicBrainz ID  (String)
        :param artist_name: Artist Name or part of Artist Name (String)
        :param artist_tmid: Artist Ticketmaster ID (int)
        :param page: Page number (results come in pages of 30) (int)
        :param sort: How to sort the returned data (String)
        :return: HTTP response with artist search results
        """
        path = "1.0/search/artists"
        params = self._build_params(page=page,
                                    artistMbid=artist_mbid,
                                    artistName=artist_name,
                                    artistTmid=artist_tmid,
                                    sort=sort)
        return self._make_request(path, params=params)

    def cities(self, country=None, name=None, state=None, state_code=None, page=1):
        """
        Serach for supported Cities
        :param country: Country or part of a country (String)
        :param name: City name or part of city name (String)
        :param state: Start or part of state (String)
        :param state_code: State Code (String)
        :param page: page number you want to return (int)
        :return: HTTP with City search results
        """""
        path = "1.0/search/cities"
        params = self._build_params(page=page,
                                    country=country,
                                    name=name,
                                    state=state,
                                    stateCode=state_code)
        return self._make_request(path=path, params=params)

    def countries(self):
        """ Get a complete list of supported countries """
        path = "1.0/search/countries"
        return self._make_request(path)

    def setlists(self, page=1, **kwargs):
        """

        :param page:
        :param kwargs: args must be in ["artistMbid", "artistName", "artistTmid", "cityId",
                         "cityName", "countryCode", "date", "lastUpdated", "state",
                         "stateCode", "tourName", "venueId", "venueName", "year"]
        :return: HTTP request with Setlist search results
        """
        setlist_items = ["artistMbid", "artistName", "artistTmid", "cityId",
                         "cityName", "countryCode", "date", "lastUpdated", "state",
                         "stateCode", "tourName", "venueId", "venueName", "year"]
        for k, v in kwargs.items():
            assert k in setlist_items
        params = self._build_params(page=page,kwargs=kwargs)
        path = "1.0/search/setlists"
        return self._make_request(path=path, params=params)

    def venues(self, page=1, **kwargs):
        """
        Search for venues
        :param page:
        :param kwargs: args must be in ["cityId", "cityName", "country", "name", "state", "stateCode"]
        :return: HTTP request with Venue search results
        """
        venue_items = ["cityId", "cityName", "country", "name", "state", "stateCode"]
        for k, v in kwargs.items():
            assert k in venue_items
        path = "1.0/search/cities"
        params = self._build_params(page=page, kwargs=kwargs)
        return self._make_request(path=path, params=params)
