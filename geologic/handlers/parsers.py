import json
import requests

from ..vector_utils import get_geom_collection_from_features


class GeojsonParser:
    def parse(self, path=None, url=None):
        """Takes Geojson FeatureCollection as input, returns a shapely Geometry Collection

        Args:
            path ([str], optional): file path of geojson. Defaults to None.
            url ([str], optional): URL of geojson. Defaults to None.

        Raises:
            Exception: raised when neither path nor url is provided

        Returns:
            [GeometryCollection]: shapely object
        """
        if path:
            with open(path) as f:
                features = json.load(f)["features"]
            return get_geom_collection_from_features(features)
        elif url:
            features = requests.get(url).json()["features"]
            return get_geom_collection_from_features(features)
        else:
            raise Exception("Needs one of file path or URL")
