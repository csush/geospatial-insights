from geologic.compute import ComputeItem
from .fixtures import generate_compute_item_ndvi_parameters


def test_compute_item(generate_compute_item_ndvi_parameters):
    test_input = generate_compute_item_ndvi_parameters[0]
    test_output = generate_compute_item_ndvi_parameters[1]

    item, vector = test_input
    item_computation = ComputeItem(item, vector)
    mean_ndvi = item_computation.mean_ndvi

    assert test_output == mean_ndvi
