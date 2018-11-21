from wikiwho_wrapper import WikiWho

ww = WikiWho()

page = ww.api.editions(page_id=2161298)
editor = ww.api.editions(editor_id=28481209)
page_editor = ww.api.editions(page_id=2161298, editor_id=286968)

editions_by_page_id_df = ww.dv.editions(page_id=2161298)
editions_by_editor_id_df = ww.dv.editions(editor_id=28481209)
editions_by_page_id_and_editor_id_df = ww.dv.editions(
    page_id=2161298, editor_id=286968)

page_as_table = ww.api.editions_as_table(page_id=2161298)
editor_as_table = ww.api.editions_as_table(editor_id=28481209)
page_editor_as_table = ww.api.editions_as_table(
    page_id=2161298, editor_id=286968)

editions_by_page_id_as_table_df = ww.dv.editions_as_table(
    page_id=2161298)
editions_by_editor_id_as_table_df = ww.dv.editions_as_table(
    editor_id=28481209)
editions_by_page_id_and_editor_id_as_table_df = ww.dv.editions_as_table(
    page_id=2161298, editor_id=286968)


import ipdb
ipdb.set_trace()  # breakpoint a89f256b //
