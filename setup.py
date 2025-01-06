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

### run local :

# uvicorn app.main:app
# streamlit run app/app.py


### Run in docker buid
## IMAGE_NAME - viewzen-classify-image1
## CONTAINER_NAME - viewzen-container
## CONATINER_ID - 1d5c214cca1a113a75e21d54087a08621e8ea6354315a2a66d01887ba4de5a2d


## COMMANDS --

# docker build -t IMAGE_NAME .
# docker run -d --name CONTAINER_NAME -p 80:80 IMAGE_NAME
