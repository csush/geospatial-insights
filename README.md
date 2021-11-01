# GEOLOGIC : Geospatial insights

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
Helps compute statistical measurements from STAC-compliant geospatial data sources. Currently supports computation of: Average NDVI.
	
## Technologies
Project is created with:
* Python >= 3.8
	
## Setup
To run this project, install it locally using pip (ideally in a virtual environment):

```
$ pip install https://github.com/csush/geospatial-insights.git
```

## Usage
```
$ geologic --help       # check out available CLI options
$ geologic --vector tests/data/mini_dh.geojson --datefilter 2021-01-01
$ geologic --vector some_url_to_your_vector.geojson --datefilter 2021-01-01/2021-10-10
```