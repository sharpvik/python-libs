# imports
from graphC import Graph

# initialize node
g = Graph()
for n in range(5):          # create 5 nodes
    g.node_add(n + 1)
g.connection_add(1, 2)
g.connection_add(1, 3)
g.connection_add(2, 3)
g.connection_add(1, 4)      # connect nodes 1 to 4 but leave ...
                            # ... node 5 as a single standing node

# search testing
print("BFS for 1 and 4 # --> True")
print( g.bfs(4, [1]) )

print("BFS for 1 and 5 # --> False")
print( g.bfs(5, [1]) )

print("DFS for 1 and 4 # --> True")
print( g.dfs(4, [1]) )

print("DFS for 1 and 5 --> False")
print( g.dfs(5, [1]) )
