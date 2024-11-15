from setuptools import setup, find_packages

setup(
    name = "country_state_city",
    version = "0.1.0",
    author = "0x747",
    description = "A simple Python API wrapper for the Country State City API.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    license="MIT",
    platforms=["Windows", "Linux", "MacOS"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["requests>=2.31.0"],
    packages = find_packages(
        include="country_state_city", 
        exclude=["tests*", "example.py"]
        ),
    python_requires = ">=3.7",
    url="https://github.com/0x747/country-state-city"
)