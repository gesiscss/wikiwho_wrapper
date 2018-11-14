# wikiwho_wrapper
A light/simple Python wrapper for the [WikiWho API](https://api.wikiwho.net/)

Requires python >= 3.6


# Installation

    pip install wikiwho_wrapper


# How to use it?

First, you need an instance of the WikiWhoAPI. 

    from wikiwho_wrapper import WikiWhoAPI
    api = WikiWhoAPI()

You can either use work with the JSON (raw format from api.wikiwho.net)

    response = api.all_content("Bioglass")

Or you can use the querier to obtain a pandas DataFrame representation of the data

    from wikiwho_wrapper import APIQuerier
    querier = APIQuerier(api)

# Run the tutorial

There are jupyter notebooks in the `tutorial` folder of the repository that serve as a tutorial.

1. Install jupyter

        pip install jupyter

2. Run jupyter

        jupyter notebook

3. Browse `localhost:8888`

4. Go to the `tutorial` directory, and follow the examples


***Note that all the methods, and classes can receive parameters. All the parameters of the API are currently supported, for now you can check them directly in the code***
