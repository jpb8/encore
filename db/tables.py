from .conection import Connection


class ArtistsData(Connection):
    TABLE_NAME = "artists"
    SQL_ADD = "INSERT INTO artists (mbid, tmid, name, sortName, disambiguation, url) VALUES (?,?,?,?,?,?)"
    PK = "mbid"
    COLUMNS = ["mbid", "tmid", "name", "sortName", "disambiguation", "url"]


class SetlistData(Connection):
    TABLE_NAME = "setlists"
    SQL_ADD = "INSERT INTO setlists (id, info, url, versionId, eventDate, lastUpdated, mbid, venueId, tourId) VALUES (?,?,?,?,?,?,?,?,?)"
    PK = "id"
    COLUMNS = ["id", "info", "url", "versionId", "eventDate", "lastUpdated", "lastUpdated", "mbid", "venueId", "tourId"]


class CityData(Connection):
    TABLE_NAME = "cities"
    SQL_ADD = "INSERT INTO cities (cityId, name, stateCode, state, long, lat, country) VALUES (?,?,?,?,?,?,?)"
    PK = "cityId"
    COLUMNS = ["cityId", "name", "stateCode", "state", "long", "lat", "country"]


class VenueData(Connection):
    TABLE_NAME = "venues"
    SQL_ADD = "INSERT INTO venues (venueId, name, url, cityId) VALUES (?,?,?,?)"
    PK = "venueId"
    COLUMNS = ["venueId", "name", "url", "cityId"]
