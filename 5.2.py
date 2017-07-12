import sys;
def euler_tour(G,s):
   q=set()
   q.add(s)
   S.add(s)
   u=q.pop()
   for v in G[u]:
       if v in S:
           continue
       visit_neighbour.append(v)
       print(visit_neighbour)
       euler_tour(G,v)
   return



nodes=['a','b','c','d','e','f']
G={'a':{'b','f'},
   'b':{'a','c'},
   'c':{'b','d'},
   'd':{'c','e'},
   'e':{'f','d'},
   'f':{'e','a'}}
for i in range (len(G)):
    if len(G[nodes[i]])%2==0:
       continue
    else:
        sys.exit()
for u in G:
   S,visit_neighbour=set(),[]
   print(u)
   euler_tour(G,u)

   if S==set(nodes):
    if ''.join(S.difference(visit_neighbour))==u:
      print('it is an eularian graph')
