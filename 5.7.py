def itre_dfs(G,s):
    t=0
    q,mark,a,f,S=[],[],dict(),dict(),set()
    q.append(s)
    S.add(s)
    a[s]=0
    print(a)
    while q:
      u=q.pop()
      print(u)
      for v in G[u]:
           print(v)
           if v in S:
              continue
           else:
             S.add(v)
             t+=1
             a[v]=t
             q.append(v)
             print(q)
      mark.append(u)
      print(mark)

    n=len(mark)
    for i in range(n-1,-1,-1):
        t+=1
        f[mark[i]]=t
        print(f)
    print(a,f)











G={'a':{'b','c'},
   'b':{'a','e'},
   'c':{'a','d'},
   'd':{'b','c'},
   'e':{'b','d'}}
itre_dfs(G,'a')