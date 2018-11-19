from wikiwho_wrapper import WikiWhoAPI, APIQuerier

api = WikiWhoAPI()

page = api.editor_content(page_id=2161298)
editor = api.editor_content(editor_id=28481209)
page_editor = api.editor_content(page_id=2161298, editor_id=286968)

querier = APIQuerier(api)

editor_content_by_page_id_df = querier.editor_content(page_id=2161298)
editor_content_by_editor_id_df = querier.editor_content(editor_id=28481209)
editor_content_by_page_id_and_editor_id_df = querier.editor_content(
    page_id=2161298, editor_id=286968)


import ipdb
ipdb.set_trace()  # breakpoint a89f256b //
