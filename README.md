# GEOLOGIC : Geospatial insights

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
Helps compute statistical measurements from STAC-compliant geospatial data sources. Currently supports computation of: Average NDVI.

## Features
- All computations are in-memory
- No data saved locally
- No need to install GDAL on your system, everything is contained via pip
- Uses multiprocessing to speed up clipping of multiple rasters
	
## Technologies
Project is created with:
- Python >= 3.8
	
## Setup
To run this project, install it locally using pip (ideally in a virtual environment):
```
$ pip install git+https://github.com/csush/geospatial-insights.git
```

## Usage
```
# check out available CLI options
$ geologic --help

# Use a vector file path and a specific date
$ geologic --vector tests/data/mini_dh.geojson --datefilter 2021-01-01

# Use a vector URL and a date range
$ geologic --vector some_url_to_your_vector.geojson --datefilter 2021-01-01/2021-10-10
```

## Todo
- Give user option to save data locally
- Give user option to set log level
- Add more filtering to STAC Search
- Add more statistical measurements