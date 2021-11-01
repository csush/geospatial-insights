from multiprocessing import Pool
from satstac import Item
import numpy as np

from .utils import clip_raster_using_vector

import logging


logger = logging.getLogger(__name__)


class ComputeItem:
    def __init__(self, item: Item, vector: str) -> None:
        """Given a STAC `Item`, helps compute NDVI

        Args:
            item (Item): a STAC Item object
        """
        self.item = item
        self.vector = vector

    @property
    def ndvi(self):
        """Clips red and nir band rasters using input AOI vector.
        Uses standard formula for NDVI using ndarrays of those bands.

        Returns:
            [type]: [description]
        """
        red_url = self.item.asset("red")["href"]
        nir_url = self.item.asset("nir")["href"]

        # Clip raster bands using a vector
        # Uses python `Pool` to apply parallel clipping
        with Pool(2) as p:
            red_data, nir_data = p.starmap(
                clip_raster_using_vector,
                [(red_url, self.vector), (nir_url, self.vector)],
            )
        red, _ = red_data
        nir, _ = nir_data

        # Calculate ndvi
        logger.info("Generating NDVI ndarray from clipped Red and NIR band rasters")
        ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)

        return ndvi

    @property
    def mean_ndvi(self):
        ndvi = self.ndvi
        logger.info("Computing mean NDVI...")
        return np.nanmean(ndvi)
