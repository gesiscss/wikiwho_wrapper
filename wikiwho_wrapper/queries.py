import pandas as pd
#from .wrapper import all_content

from .api import WikiWhoAPI

api = WikiWhoAPI()

# nice example: bioglass
# response = api.all_content("Cologne")
# response = api.range_rev_content_by_article_title("bioglass", 18064039, 79583319)
#response = api.rev_ids_of_article(2161298)

def all_content():


    # use the wrapper to query the api
    response = api.all_content("bioglass")

    rows = []

    for myVal in response["all_tokens"]:
        each_row = []
        each_row.append(response["article_title"])
        each_row.append(response["page_id"])
        for key, value in myVal.items():
            each_row.append(value)
        rows.append(each_row)

    # import ipdb; ipdb.set_trace()  # breakpoint 12fb971f //

    df = pd.DataFrame(data = rows, columns = ['article_title', 'page_id', 'editor', 'token', 'token_id', 'o_rev_id', 'out', 'in'])

    # df = pd.DataFrame.from_dict(response)

    return df