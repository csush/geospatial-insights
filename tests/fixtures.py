import pytest

from . import constants
from geologic.constants import STAC_API_URL, STAC_COLLECTION
from geologic.search import get_stac_item


@pytest.fixture()
def generate_get_stac_item_parameters(request):
    url = STAC_API_URL.ELEMENT84
    collections = [STAC_COLLECTION.SENTINEL_2_COG]
    datefilter = "2021-01-01"
    vector = constants.TEST_VECTOR_URL

    test_input = (
        url,
        collections,
        datefilter,
        vector,
    )
    test_output = "S2B_33UUU_20210101_0_L2A"
    return test_input, test_output


@pytest.fixture()
def generate_clip_raster_using_vector_parameters(request):
    raster = constants.TEST_RASTER_URL
    vector = constants.TEST_VECTOR_URL

    test_input = (
        raster,
        vector,
    )
    test_output = {"width": 896, "height": 835}
    return test_input, test_output


@pytest.fixture()
def generate_compute_item_ndvi_parameters(request):
    item = get_stac_item(
        STAC_API_URL.ELEMENT84,
        [STAC_COLLECTION.SENTINEL_2_COG],
        "2021-01-01",
        constants.TEST_VECTOR_URL,
    )

    test_input = (
        item,
        constants.TEST_VECTOR_URL,
    )
    test_output = 0.04334591725447628
    return test_input, test_output
