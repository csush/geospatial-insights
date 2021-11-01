from .search import get_stac_item
from .compute import ComputeItem
from .constants import STAC_API_URL, STAC_COLLECTION

import click
import datetime

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--url",
    default=STAC_API_URL.ELEMENT84,
    help="Base URL of STAC-compliant API. If empty, defaults to Element84.",
)
@click.option(
    "--collections",
    default=[STAC_COLLECTION.SENTINEL_2_COG],
    multiple=True,
    help="Space delimited list of STAC collections. If empty, defaults to [sentinel-s2-l2a-cogs].",
)
@click.option(
    "--datefilter",
    default=datetime.date.today,
    help="YYYY-MM-DD for specific date. YYYY-MM-DD/YYYY-MM-DD for date range. If empty, defaults to today's date.",
)
@click.option("--vector", help="Vector file path or URL.", required=True)
def main(url, collections, datefilter, vector):

    item = get_stac_item(url, collections, datefilter, vector)
    item_computation = ComputeItem(item, vector)

    # fancy colour for relevant output
    print(f"\033[1;32mMean NDVI: {item_computation.mean_ndvi}\n")


if __name__ == "__main__":
    main()
