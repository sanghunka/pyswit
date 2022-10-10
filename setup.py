from setuptools import setup


with open("README.md") as f:
    readme = f.read()


setup(
    name="pyswit",
    version="0.0.1",
    packages=["pyswit"],
    description="Swit.io API client",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Sanghun Kang",
    author_email="sanghunka@gmail.com",
    url="https://github.com/sanghunka/pyswit/",
    install_requires=["requests >= 2.28.1"],
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Office/Business",
    ],
    keywords="swit swit.io api",
)
