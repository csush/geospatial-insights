import rasterio
import geopandas as gpd
from rasterio.mask import mask

import logging


logger = logging.getLogger(__name__)


def clip_raster_using_vector(raster: str, vector: str) -> tuple:
    """Clips raster data using given vector

    Args:
        raster (str): file path or URL of raster dataset
        vector (str): file path or URL of vector dataset

    Returns:
        tuple: contains clipped ndarray and its metadata
    """
    src = gpd.read_file(vector)
    logger.info(f"Vector CRS: {src.crs}")

    with rasterio.open(raster) as dst:
        logger.info(f"Raster CRS: {dst.crs}")
        if src.crs != dst.crs:
            logger.warning("CRS mismatch: reprojecting vector")
            src = src.to_crs(dst.crs)

        logger.info("Clipping raster using vector")
        shapes = src.geometry
        out_image, out_transform = mask(dst, shapes, crop=True)
        out_meta = dst.meta
        out_meta.update(
            {
                "driver": "GTiff",
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform,
            }
        )

    return (
        out_image,
        out_meta,
    )
