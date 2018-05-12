# imports
from graphC import Graph
from stackD import Stack
from queueD import Queue

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
print("BFS for 1 and 2 # --> True")
print( g.bfs( 2, Queue(1) ), end="\n\n" )

print("BFS for 1 and 4 # --> True")
print( g.bfs( 4, Queue(1) ), end="\n\n" )

print("BFS for 1 and 5 # --> False")
print( g.bfs( 5, Queue(1) ), end="\n\n" )


print("DFS for 1 and 2 # --> True")
print( g.dfs( 2, Stack(1) ), end="\n\n" )

print("DFS for 1 and 4 # --> True")
print( g.dfs( 4, Stack(1) ), end="\n\n" )

print("DFS for 1 and 5 --> False")
print( g.dfs( 5, Stack(1) ), end="\n\n" )
