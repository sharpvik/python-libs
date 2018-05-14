# imports
from graphD import Graph
from stackD import Stack
from queueD import Queue

# initialize node
g = Graph()
for n in range(97, 115):          # create nodes 'a' to 'g'
    g.node_add( chr(n) )
g.connection_add('a', 'b')
g.connection_add('a', 'c')
g.connection_add('a', 'e')
g.connection_add('a', 'h')
g.connection_add('c', 'b')
g.connection_add('c', 'd')
g.connection_add('h', 'i')
g.connection_add('h', 'j')
g.connection_add('e', 'f')
g.connection_add('e', 'g')
g.connection_add('g', 'f')

g.connection_add('q', 'p')
g.connection_add('q', 'o')
g.connection_add('q', 'r')
g.connection_add('q', 'k')
g.connection_add('q', 'n')
g.connection_add('n', 'm')
g.connection_add('n', 'l')
g.connection_add('k', 'l')

# check node
print( g.nodes_return() )

# search testing
print("BFS for a and c --> True")
print( g.bfs( 'c', Queue('a') ), end="\n\n" )

print("BFS for a and d --> True")
print( g.bfs( 'd', Queue('a') ), end="\n\n" )

print("BFS for i and d --> True")
print( g.bfs( 'd', Queue('i') ), end="\n\n" )

print("BFS for i and g --> True")
print( g.bfs( 'g', Queue('i') ), end="\n\n" )

print("bFS for m and h --> False")
print( g.bfs( 'h', Queue('m') ), end="\n\n" )


print("DFS for a and c --> True")
print( g.dfs( 'c', Stack('a') ), end="\n\n" )

print("DFS for a and d --> True")
print( g.dfs( 'd', Stack('a') ), end="\n\n" )

print("DFS for i and d --> True")
print( g.dfs( 'd', Stack('i') ), end="\n\n" )

print("DFS for i and g --> True")
print( g.dfs( 'g', Stack('i') ), end="\n\n" )

print("DFS for m and h --> False")
print( g.dfs( 'h', Stack('m') ), end="\n\n" )
