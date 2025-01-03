from setuptools import find_packages, setup

from app import __version__

setup(
    name="iris_classifier",
    version=__version__,
    packages=find_packages(where="."),
    python_requires=">=3.8 , <4",
    install_requires=[],
    extras_requires={},
)
