from wikiwho_wrapper import WikiWho

ww = WikiWho()

#df = ww.dv.all_content(article='bioglass')
df = ww.dv.last_rev_content(article='bioglass')

import ipdb; ipdb.set_trace()  # breakpoint da45b82e //
