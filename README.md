# wikiwho_wrapper

A light/simple Python wrapper for the [WikiWho API](https://api.wikiwho.net/).

The [WikiWho API](https://api.wikiwho.net/) provides the first editor (author) of Wikipedia words (tokens). It also provides the history of each of the tokens, i.e. in which revisions (and which editors) was the token (re)inserted or removed. The API is based on the [WikiWho algorithm](https://github.com/wikiwho) (~95% acc.). 

Find full information and how to cite this work in [api.wikiwho.net](https://api.wikiwho.net/).

# Installation

Requires python >= 3.6

    pip install wikiwho_wrapper

# How to use it?

First, you need an instance of the WikiWho. 

    from wikiwho_wrapper import WikiWho
    ww = WikiWhoAPI()

You can either use api with the JSON (raw format from api.wikiwho.net)

    response = ww.api.all_content("Bioglass")

Or you can use the dataview to obtain a pandas DataFrame representation of the data

    dataView = ww.dv.all_content("Bioglass")

# Tutorial

There is a tutorial in the form of jupyter notebooks, the are located in the [wikiwho_tutorial repository](https://github.com/gesiscss/wikiwho_tutorial). 

***Note that all the methods, and classes can receive parameters. All the parameters of the API are currently supported. For now, you can check them directly in the code.***
