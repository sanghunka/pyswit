from setuptools import setup
from pyswit import __version__


with open("README.md") as f:
    readme = f.read()


setup(
    name="pyswit",
    version=__version__,
    packages=["pyswit"],
    description="Swit.io API client",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Sanghun Kang",
    author_email="sanghunka@gmail.com",
    url="https://github.com/sanghunka/pyswit/",
    install_requires=["requests >= 2.28.1"],
    license="Apache Software License",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Office/Business",
    ],
    keywords="swit swit.io api messenger",
)
