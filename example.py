from wikiwho_wrapper import WikiWho

ww = WikiWho()

page = ww.api.actions(page_id=2161298)
editor = ww.api.actions(editor_id=28481209)
page_editor = ww.api.actions(page_id=2161298, editor_id=286968)

actions_by_page_id_df = ww.dv.actions(page_id=2161298)
actions_by_editor_id_df = ww.dv.actions(editor_id=28481209)
actions_by_page_id_and_editor_id_df = ww.dv.actions(
    page_id=2161298, editor_id=286968)

page_as_table = ww.api.actions_as_table(page_id=2161298)
editor_as_table = ww.api.actions_as_table(editor_id=28481209)
page_editor_as_table = ww.api.actions_as_table(
    page_id=2161298, editor_id=286968)

actions_by_page_id_as_table_df = ww.dv.actions_as_table(
    page_id=2161298)
actions_by_editor_id_as_table_df = ww.dv.actions_as_table(
    editor_id=28481209)
actions_by_page_id_and_editor_id_as_table_df = ww.dv.actions_as_table(
    page_id=2161298, editor_id=286968)


import ipdb
ipdb.set_trace()  # breakpoint a89f256b //
