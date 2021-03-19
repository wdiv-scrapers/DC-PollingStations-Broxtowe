from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v3/datasets?q=polling&filter%5Bowner%5D=Broxtowe_GIS&fields[datasets]=name,url"
stations_url = "https://opendata.arcgis.com/datasets/a3da8ff112a647fe857a45c9996488fd_3.geojson"
districts_url = "https://opendata.arcgis.com/datasets/ace0ecbc348a41b5b804557f6a68f575_1.geojson"
council_id = 'BRT'


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape(exclude_keys=['meta'])
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
