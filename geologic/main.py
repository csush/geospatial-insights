import pprint

E84_API_URL = "https://earth-search.aws.element84.com/v0"

import requests


def get_response(url, params={}):
    headers = {"Accept": "application/geo+json"}

    r = requests.get(
        "https://earth-search.aws.element84.com/v0/search",
        params=params,
        headers=headers,
    )

    print(r.json())


if __name__ == "__main__":
    get_response(
        "https://earth-search.aws.element84.com/v0/search",
    )
