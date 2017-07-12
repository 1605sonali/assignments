def itredfs_with_timestamp(G,s,t):
    q=[]
    q.append(s)
    S.add(s)
    a_time[s]=t
    while q:
      u=q.pop()
      print(u)
      visited.append(u)
      if G[u]:
       if G[u] not in S:
        for v in G[u]:
          #print(v)
          if v in S:
            continue
          S.add(v)
          t+=1
          a_time[v]=t

          q.append(v)
          #print(q)

      else:
       visited.pop()
       print(visited)
       t+=1
       f_time[u]=t
       print(f_time)
    n=len(visited)
    for i in range(n-1,-1,-1):
        t+=1
        f_time[visited[i]]=t
    print(a_time,f_time)


a_time,f_time,S,visited=dict(),dict(),set(),[]
G={'a':{'b'},
   'b':{'c','l'},
   'c':{'i','b'},
   'i':{'c','j','k'},
   'j':{'i'},
   'k':{'i'},
   'l':{'b'}}


t=0
itredfs_with_timestamp(G,'a',t)