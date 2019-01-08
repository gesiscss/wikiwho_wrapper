from wikiwho_wrapper import WikiWho

ww = WikiWho()

#df = ww.dv.all_content(article='bioglass', editor=False)
df = ww.dv.rev_ids_of_article(6197, editor=False)

import ipdb; ipdb.set_trace()  # breakpoint da45b82e //
