from wikiwho_wrapper import WikiWhoAPI, APIQuerier

api = WikiWhoAPI()

# nice example: bioglass
# response = api.all_content("Cologne")
# response = api.range_rev_content_by_article_title("bioglass", 18064039, 79583319)
# response = api.rev_ids_of_article(2161298)
querier = APIQuerier(api)



df0 = querier.all_content(article="bioglass")
df1 = querier.all_content(2161298)

df2 = querier.last_rev_content(article="bioglass")
df3 = querier.last_rev_content(2161298)
df4 = querier.specific_rev_content_by_rev_id(rev_id=189370281)
df5 = querier.specific_rev_content_by_article_title(article_title="bioglass", rev_id=189370281)
df6 = querier.range_rev_content_by_article_title(article_title="bioglass",  start_rev=18064039,  end_rev=207995408)

df7 = querier.rev_ids_of_article(article="bioglass")
df8 = querier.rev_ids_of_article(2161298)



import ipdb
ipdb.set_trace()
