import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="mediascraper",
    version="0.0.2",
    author="Tim232",
    author_email="author@example.com",
    description="A small package for scraping medias.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonPb/mediascraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)