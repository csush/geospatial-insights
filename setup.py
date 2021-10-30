import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geologic",
    version="0.0.1",
    author="Sushant Chaudhary",
    author_email="csush.95@gmail.com",
    description="Helps generate insights from geospatial data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csush/geospatial-insights.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "aiodns==3.0.0",
        "aiohttp==3.7.4.post0",
        "cchardet==2.1.7",
        "setuptools==44.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points="""
        [console_scripts]
        geologic=geologic:main
    """,
)
