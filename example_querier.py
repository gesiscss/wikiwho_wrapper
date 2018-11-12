from wikiwho_wrapper import WikiWhoAPI, APIQuerier

api = WikiWhoAPI()

# nice example: bioglass
# response = api.all_content("Cologne")
# response = api.range_rev_content_by_article_title("bioglass", 18064039, 79583319)
# response = api.rev_ids_of_article(2161298)
querier = APIQuerier(api)

all_content_by_given_article_title_df = querier.all_content(article="bioglass")
all_content_by_given_page_id_df = querier.all_content(2161298)

last_revision_by_given_article_title_df = querier.last_rev_content(article="bioglass")
last_revision_by_given_page_id_df = querier.last_rev_content(2161298)

specific_revision_by_given_article_title_df = querier.specific_rev_content_by_rev_id(rev_id=189370281)
specific_revision_by_given_revision_id_df = querier.specific_rev_content_by_article_title(article_title="bioglass", rev_id=189370281)

range_revisions_by_given_start_to_end_revision_ids_df = querier.range_rev_content_by_article_title(article_title="bioglass",  start_rev=18064039,  end_rev=207995408)

revision_ids_of_article_by_given_article_title_df = querier.rev_ids_of_article(article="bioglass")
revision_ids_of_article_by_given_page_id_df = querier.rev_ids_of_article(2161298)

import ipdb
ipdb.set_trace()
