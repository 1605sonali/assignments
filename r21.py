b=[]
d=[]
c=[]
a=['p','q','r','s','x','y','z']
g=[['q','s'],
   ['r'],
   [],
   ['r'],
   ['y','z'],
   ['p','q'],
   ['q']]


for i in range(len(g)):
    if len(g[i])==0:
        c.append(a[i])
        b.append(len(g[i]))

    else:
        b.append(len(g[i]))

while len(c) > 0:

         u = c.pop()
         print(u)
         d.append(u)

         for i in range(len(b)):
             f=set(g[i])

             if u in f :
                b[i]=b[i]-1
                if b[i]==0:
                   c.append(a[i])
print(d)

























