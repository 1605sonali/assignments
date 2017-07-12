def bfs_distance(G,s):
    q,S=set(),set()
    q.add(s)
    S.add(s)
    dist[s]=0
    while q:
        u=q.pop()

        for v in G[u]:
            if v in S:
                continue
            S.add(v)
            q.add(v)
            dist[v]=1+dist[u]
    print(S,dist)








dist=dict()
G={'a':{'b'},
   'b':{'c','l'},
   'c':{'i','b'},
   'i':{'c','j','k'},
   'j':{'i'},
   'k':{'i'},
   'l':{'b'}}
bfs_distance(G,'a')
