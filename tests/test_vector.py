from .fixtures import (
    generate_get_bbox_from_vector_file_parameters,
    generate_get_bbox_from_vector_url_parameters,
)

from geologic.handlers.parsers import GeojsonParser


def test_get_bbox_from_vector_file(generate_get_bbox_from_vector_file_parameters):
    test_input = generate_get_bbox_from_vector_file_parameters[0]
    expected_output = generate_get_bbox_from_vector_file_parameters[1]
    bounds = GeojsonParser().parse(path=test_input).bounds
    assert expected_output == bounds


def test_get_bbox_from_vector_url(generate_get_bbox_from_vector_url_parameters):
    test_input = generate_get_bbox_from_vector_url_parameters[0]
    expected_output = generate_get_bbox_from_vector_url_parameters[1]
    bounds = GeojsonParser().parse(url=test_input).bounds
    assert expected_output == bounds
