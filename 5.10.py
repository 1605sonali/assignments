def bipartition(G,s):
    q=set()
    q.add(s)

    while q:
        u=q.pop()
        if u in p2:
            continue
        p1.add(u)
        for v in G[u]:
            p_node[u].append(v)
            p2.add(v)
            q.add(v)

    return




from collections import defaultdict;
p_node=defaultdict(list)

p1,p2=set(),set()
"""G={'a':{'b','c','d'},
   'b':{'a','d','e'},
   'c':{'a','d'},
   'd':{'c','a','b'},
   'e':{'b','d'}}"""

G={'a':{'b'},
   'b':{'c','l'},
   'c':{'i','b'},
   'i':{'c','j','k'},
   'j':{'i'},
   'k':{'i'},
   'l':{'b'}}

for u in G:
    bipartition(G,u)
print('p1','p2','p_node',p1,p2,p_node)
