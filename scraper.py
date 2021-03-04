from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "https://opendata.arcgis.com/datasets/a3da8ff112a647fe857a45c9996488fd_3.geojson"
districts_url = "https://opendata.arcgis.com/datasets/ace0ecbc348a41b5b804557f6a68f575_1.geojson"
council_id = 'BRT'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
