"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wikiwho_wrapper",
    version="1.6.2",
    # Author details
    author="",
    author_email="wikiwho@gesis.org",
    description="A light/simple Python wrapper for the WikiWho API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gesiscss/wikiwho_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # What does your project relate to?
    keywords='wikipedia wikiwho revisions content authorship',
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests', 'pandas', 'deprecation', 'wikiwho_pickle']
)
