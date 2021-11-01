from geologic.utils import clip_raster_using_vector
from .fixtures import generate_clip_raster_using_vector_parameters


def test_clip_raster_using_vector(generate_clip_raster_using_vector_parameters):
    test_input = generate_clip_raster_using_vector_parameters[0]
    expected_output = generate_clip_raster_using_vector_parameters[1]

    raster, vector = test_input
    _, out_meta = clip_raster_using_vector(raster, vector)

    actual_output = {"width": out_meta.get("width"), "height": out_meta.get("height")}
    assert expected_output == actual_output
