from stackD import Stack
from queueD import Queue

class Graph:                                            # undirected graph; no values for the edges;
    def __init__(self):
        self.nodes_counter = 0
        self.nodes_dict = dict()

    def node_add(self, name):                           # name(int / str) -- name of the node;
        self.nodes_dict.update( { name : list() } )
        self.nodes_counter += 1
        return name

    def node_del(self, name):                           # name(int / str) -- name of the node;
        self.nodes_dict.pop(name, None)
        for each in self.nodes_dict:
            self.nodes_dict[each].remove(name)
        self.nodes_counter -= 1
        return name

    def connection_add(self, one, two):                 # one(int / str) and two(int / str) -- two nodes you want to connect;
        self.nodes_dict[one].append(two)
        self.nodes_dict[two].append(one)
        return [one, two]

    def connection_del(self, one, two):                 # one(int / str) and two(int / str) -- two nodes you want to disconnect;
        self.nodes_dict[one].remove(two)
        self.nodes_dict[two].remove(one)
        return [one, two]

    def nodes_count(self):                              # --> function returns the number of nodes in the graph;
        return self.nodes_counter

    def nodes_return(self):                             # --> function returns the whole dict containing nodes and their connections;
        return self.nodes_dict

    def node_return(self, name):                        # name(int / str) -- name of the node you're checking;
                                                        # --> function returns connections of the given node;
        return self.nodes_dict[name]

    # search

    ## --> breadth first search using class Queue
    def bfs( self, final, queue=Queue(None), checked=list() ):      # final(int / str) -- name of the node you're trying to establish connection with;
                                                                    # queue(class Queue) -- Queue containing the element you are beginning with (format: element);
                                                                    # checked(list) -- leave empty unless you want to specifically prevent certain nodes from being checked *** internal use ***;
                                                                    # --> function returns True if the two nodes are connected, otherwise it returns False;
        if queue.length() == 0:
            return False
        temp = queue.pop()
        if temp == final:
            return True
        else: 
            checked.append(temp)
            for child in self.node_return(temp):
                if child not in checked:
                    queue.ins(child)
            return self.bfs( final, queue, list(checked) )
    ## breadth first search using class Queue <--

    ## --> depth first serach using class Stack
    def dfs( self, final, stack=Stack(None), checked=list() ):      # final(int / str) -- name of the node you're trying to establish connection with;
                                                                    # stack(class Stack) -- Stack containing the element you are beginning with (format: element);
                                                                    # checked(list) -- leave empty unless you want to specifically prevent certain nodes from being checked *** internal use ***;
                                                                    # --> function returns True if the two nodes are connected, otherwise it returns False;
        if stack.length() == 0:
            return False
        temp = stack.pop()
        if temp == final:
            return True
        else:
            checked.append(temp)
            for child in self.node_return(temp):
                if child not in checked:
                    stack.add(child)
            return self.dfs( final, stack, list(checked) )
    ## depth first serach using class Stack <--
