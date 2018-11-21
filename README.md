# wikiwho_wrapper
A light/simple Python wrapper for the [WikiWho API](https://api.wikiwho.net/)

Requires python >= 3.6


# Installation

    pip install wikiwho_wrapper


# How to use it?

First, you need an instance of the WikiWho. 

    from wikiwho_wrapper import WikiWho
    ww = WikiWhoAPI()

You can either use work with the JSON (raw format from api.wikiwho.net)

    response = ww.api.all_content("Bioglass")

Or you can use the querier to obtain a pandas DataFrame representation of the data

    dataView = ww.dv.all_content("Bioglass")

# Follown the tutorial

There is a tutorial in the form of jupyter notebooks, the are located in the [wikiwho_tutorial repository](https://github.com/gesiscss/wikiwho_tutorial). 

***Note that all the methods, and classes can receive parameters. All the parameters of the API are currently supported, for now you can check them directly in the code***
