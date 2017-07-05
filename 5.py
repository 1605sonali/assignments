import sys;
def path(G,n1,n2):
    #n1=set(input('enter starting point'))
    #n2=set(input('enter ending point'))
  if n1!=n2:


    q=set()
    d=[]
    q.add(n1)
    while q:
        u=q.pop()
        d.append(u)
        for v in G[u]:

            if v==n2:
               d.append(v)

               print(d)
               sys.exit()
            if v in d:
              print(d)
              print('there is no such path bcoz of cycle in graph')

              sys.exit()

            else:
                q.add(v)
                print(q)

  else:
      print('enter valid statring and ending nodes')





















d=set()
G={'c':{'a','d'},
   'a':{'b','e'},
   'd':{'e'},
   'e':{'f'},
   'b':{'e'},
   'f':{'b'}
   }
#n1=input('enter path starting')
#n2=input('enter ending point')
path(G,'f','a')
