import satsearch
import intake
import requests
import json
import numpy as np
import rasterio as rio
from multiprocessing import Pool
from rasterio.plot import show
from matplotlib import pyplot

import logging

from handlers.parsers import GeojsonParser


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class STAC_API_URL:
    ELEMENT84 = "https://earth-search.aws.element84.com/v0"


class STAC_COLLECTION:
    SENTINEL_2_COG = "sentinel-s2-l2a-cogs"


BBOX = [
    12.969017028808594,
    52.45946123411788,
    13.10068130493164,
    52.53460237630518,
]


def get_response(url, params={}):
    headers = {"Accept": "application/geo+json"}
    r = requests.post(
        url + "/search",
        params=params,
        headers=headers,
    )
    return r.json()


def read_raster_from_url(url, band=""):
    with rio.open(url) as src:
        logger.info(f"Reading {band} band url: {url}")
        red = src.read()
    return red


def get_cogs(
    bbox,
    collections,
):

    search = satsearch.Search.search(
        bbox=bbox,
        url=STAC_API_URL.ELEMENT84,
        collections=collections,
        datetime="2021-01-01",
        sortby="-properties.eo:cloud_cover",
        **{"eo:cloud_cover": "0/5"},
    )

    items = search.items()
    # catalog = intake.open_stac_item_collection(items)
    red_url = items[0].asset("red")["href"]
    nir_url = items[0].asset("nir")["href"]
    with Pool(5) as p:
        red, nir = p.map(read_raster_from_url, [red_url, nir_url])

    # with rio.open(red_url) as src:
    #     print(f"reading red band url: {red_url}")
    #     red = src.read()

    # with rio.open(nir_url) as src:
    #     print(f"reading nir band url: {nir_url}")
    #     nir = src.read()

    # Calculate ndvi
    print("calculating ndvi")
    ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)
    print("DONE")
    # fig, ax = pyplot.subplots(figsize=(12,10))
    # show(ndvi[0, 2000:6000, 4000:8000], cmap="RdYlGn", ax=ax)
    # pyplot.show()
    # fig, ax = pyplot.subplots(figsize=(12,10))
    # show(ndvi[0, 2000:6000, 4000:8000], cmap="RdYlGn", ax=ax)
    # pyplot.show()
    # print(ndvi)

    # for cog_num in range(0, np.shape(list(catalog))[0]):
    #     pprint(c)
    # print(f"ASSETS \n {items[0].assets}")
    # with open("items.json", "w") as f:
    #     json.dump(items, f, indent=2)
    # print(items[0].asset("thumbnail")["href"])
    # print('%s items' % results.found())
    # items = results.items()
    # # Save this locally for use later
    # items.save('my-s2-l2a-cogs.json')
    # type(items)
    # catalog = intake.open_stac_item_collection(items)


if __name__ == "__main__":
    boundary = GeojsonParser().parse(path="tests/data/mini_dh.geojson").bounds
    # json_response = get_response(
    #     STAC_API_URL.ELEMENT84,
    #     params={
    #         "bbox": BBOX,
    #         "collections": [STAC_COLLECTION.SENTINEL_2_COG],
    #         "query": {"eo:cloud_cover": "0/5"},
    #         "datetime": "2021-01-01",
    #         "sort": [{"field": "eo:cloud_cover", "direction": "desc"}],
    #     },
    # )

    # with open("all_1.json", "w") as f:
    #     json.dump(json_response, f, indent=2)
    get_cogs(boundary, [STAC_COLLECTION.SENTINEL_2_COG])
