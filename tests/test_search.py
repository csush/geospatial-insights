from geologic.search import get_stac_item
from .fixtures import (
    generate_get_stac_item_parameters,
)


def test_get_stac_item(generate_get_stac_item_parameters):
    test_input = generate_get_stac_item_parameters[0]
    expected_output = generate_get_stac_item_parameters[1]

    url, collections, datefilter, vector = test_input
    item = get_stac_item(url, collections, datefilter, vector)
    item_id = item.id

    assert expected_output == item_id
