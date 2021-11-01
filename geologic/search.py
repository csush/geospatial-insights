import satsearch
from satstac import Item
import geopandas as gpd

import logging


logger = logging.getLogger(__name__)


def get_stac_item(
    url: str,
    collections: list,
    datefilter: str,
    vector: str,
) -> Item:
    """Query given STAC-compliant API `url` /search endpoint.
    If results found, fetch the first item from that list.

    Args:
        url (str): URL of STAC-compliant API
        collections (list): list of collections to filter from
        datetime (str): Specific datetime like YYYY-MM-DD or
                        range like YYYY-MM-DD/YYYY-MM-DD
        aoi (str): vector file path or URL
        bbox (list): coordinates of bounds

    Raises:
        Exception: check either `geometry` or `bbox` exists

    Returns:
        Item: first STAC `Item` object returned from API
    """
    bounds = gpd.read_file(vector).bounds.values.tolist()[0]

    search = satsearch.Search.search(
        bbox=bounds,
        url=url,
        collections=collections,
        datetime=datefilter,
        sortby="-properties.eo:cloud_cover",
        **{"eo:cloud_cover": "0/5"},
    )

    items = search.items()

    if len(items) < 1:
        logger.warning("No items found for this query. Exiting program.")
        exit()
    else:
        logger.info(f"Found {len(items)} items...")

    # returns the first element of query result
    return items[0]
