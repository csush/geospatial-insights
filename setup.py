import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geologic",
    version="0.0.1",
    author="Sushant Chaudhary",
    author_email="csush.95@gmail.com",
    description="Helps compute statistical measurements from from STAC-compliant geospatial data sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csush/geospatial-insights.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "setuptools==44.0.0",
        "pytest==6.2.5",
        "sat-search==0.3.0",
        "sat-stac==0.4.1",
        "geopandas==0.10.2",
        "numpy==1.21.3",
        "click==8.0.3",
        "rasterio==1.2.10",
        "wheel==0.34.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["geologic = geologic.__main__:main"]},
)
