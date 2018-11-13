# wikiwho_wrapper
A light/simple Python wrapper for the [WikiWho API](https://api.wikiwho.net/)

Requires python >= 3.6


# Installation

    pip install wikiwho_wrapper


# How to use it?

First, you need and instance of the WikiWhoAPI. 

    from wikiwho_wrapper import WikiWhoAPI
    api = WikiWhoAPI()

You can either use work with the JSON (raw format from api.wikiwho.net)

    response = api.all_content("Bioglass")

Or you can use the querier to obtain a pandas DataFrame representation of the data

    from wikiwho_wrapper import APIQuerier
    querier = APIQuerier(api)


***Note that all the methods, and classes can receive parameters. All the parameters of the API are currently supported, for now you can check them directly in the code***