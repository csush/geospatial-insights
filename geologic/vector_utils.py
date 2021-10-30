from shapely.geometry import shape, GeometryCollection


def get_geom_collection_from_features(features):
    # NOTE: buffer(0) is a trick for fixing scenarios where polygons have overlapping coordinates
    return GeometryCollection(
        [shape(feature["geometry"]).buffer(0) for feature in features]
    )


# def get_bbox_from_vector()
