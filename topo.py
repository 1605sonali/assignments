


a=['p','q','r','s','x','y','z']
g=[{'q','s'},
   {'r'},
   (),
   {'r'},
   {'y','z'},
   {'p','q'},
   {'q'}]
indegree_count=[]  #to keep an indegree_count of each node of a graph
c=[]               #an auxiliary list
d=[]               #for stroing final result

for i in range(len(g)):
        indegree_count.append(len(g[i]))
print(indegree_count)

for i in range(len(indegree_count)):
    if indegree_count[i] == 0:
        c.append(a[i])
print(c)

while len(c) > 0:
    k = c.pop()
    d.append(k)
    for i in range(len(g)):
        if k in g[i]:
            indegree_count[i]=indegree_count[i]-1
            if indegree_count[i]== 0:
                c.append(a[i])
print(d)




