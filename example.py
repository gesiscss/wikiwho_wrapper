import os
from wikiwho_wrapper import WikiWho, WikiWhoPickleAPI, WikiWhoAPI

# Examples using a a pickle file
ww = WikiWho()

if os.path.isfile(os.path.join('pickles', 'en', '2161298.p')):
    ww_pickle = WikiWho(pickle_path='pickles', lng='en')
    df_pickle = ww_pickle.dv.specific_rev_content_by_rev_id(363901244, article_id=2161298)
    page = ww_pickle.api.all_content(article=2161298)
    last_rev_content_pickle = ww_pickle.dv.last_rev_content(2161298)

# Examples using the api directly
ww = WikiWho()
last_rev_content = ww.dv.last_rev_content(2161298)
df = ww.dv.specific_rev_content_by_rev_id(503680497)

page = ww.api.edit_persistence(page_id=2161298)
editor = ww.api.edit_persistence(editor_id=28481209)
page_editor = ww.api.edit_persistence(page_id=2161298, editor_id=286968)

edit_persistence_by_page_id_df = ww.dv.edit_persistence(page_id=2161298)
edit_persistence_by_editor_id_df = ww.dv.edit_persistence(editor_id=28481209)
edit_persistence_by_page_id_and_editor_id_df = ww.dv.edit_persistence(
    page_id=2161298, editor_id=286968)

import ipdb; ipdb.set_trace()  # breakpoint 67efd4b1 //
