import pytest

from . import constants


@pytest.fixture()
def generate_get_bbox_from_vector_file_parameters(request):
    test_input = constants.TEST_VECTOR_PATH
    test_output = constants.TEST_BOUNDS
    return test_input, test_output


@pytest.fixture()
def generate_get_bbox_from_vector_url_parameters(request):
    test_input = constants.TEST_VECTOR_URL
    test_output = constants.TEST_BOUNDS
    return test_input, test_output
