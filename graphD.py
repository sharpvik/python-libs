#
# ===============================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE             =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===>      Graph class      <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =        (10.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ===============================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



from stackD import Stack
from queueD import Queue

class Graph:                                            # undirected graph; no values for the edges;
    def __init__(self):
        self.nodes_dict = dict()

    def node_add(self, name):                           # name(int / str) -- name of the node;
        if name not in self.nodes_dict:
            self.nodes_dict.update( { name : list() } )
        return name

    def node_del(self, name):                           # name(int / str) -- name of the node;
        self.nodes_dict.pop(name, None)
        for each in self.nodes_dict:
            try:
                self.nodes_dict[each].remove(name)
            except ValueError:
                print( "WARNING: {} does not exist!".format(name) )
        return name

    def connection_add(self, one, two):                 # one(int / str) and two(int / str) -- two nodes you want to connect;
        if two not in self.nodes_dict[one]:
            self.nodes_dict[one].append(two)
        if one not in self.nodes_dict[two]:
            self.nodes_dict[two].append(one)
        return [one, two]

    def connection_del(self, one, two):                 # one(int / str) and two(int / str) -- two nodes you want to disconnect;
        try:
            self.nodes_dict[one].remove(two)
        except ValueError:
            print( "WARNING: {} does not have a connection to {}!".format(two, one) )
        try:
            self.nodes_dict[two].remove(one)
        except ValueError:
            print( "WARNING: {} does not have a connection to {}!".format(one, two) )
        return [one, two]

    def nodes_count(self):                              # --> function returns the number of nodes in the graph;
        return len(self.nodes_dict)

    def nodes_return(self):                             # --> function returns the whole dict containing nodes and their connections;
        return self.nodes_dict

    def node_con_return(self, name):                    # name(int / str) -- name of the node you're checking;
                                                        # --> function returns connections of the given node;
        return self.nodes_dict[name]

    # search

    ## --> breadth first search using class Queue
    def bfs( self, final, queue=Queue(None), checked=list() ):      # final(int / str) -- name of the node you're trying to establish connection with;
                                                                    # queue(class Queue) -- Queue containing the element you are beginning with (format: element);
                                                                    # checked(list) -- leave empty *** internal use ***;
                                                                    # --> function returns True if the two nodes are connected, otherwise it returns False;
        _checked = list(checked)
        if queue.is_empty():
            return False
        temp = queue.pop()
        if temp == final:
            return True
        else: 
            _checked.append(temp)
            for child in self.node_con_return(temp):
                if child not in _checked and not queue.inside(child):
                    queue.push(child)
            return self.bfs(final, queue, _checked)
    ## breadth first search using class Queue <--

    ## --> depth first serach using class Stack
    def dfs( self, final, stack=Stack(None), checked=list() ):      # final(int / str) -- name of the node you're trying to establish connection with;
                                                                    # stack(class Stack) -- Stack containing the element you are beginning with (format: element);
                                                                    # checked(list) -- leave empty *** internal use ***;
                                                                    # --> function returns True if the two nodes are connected, otherwise it returns False;
        _checked = list(checked)
        if stack.is_empty():
            return False
        temp = stack.pop()
        if temp == final:
            return True
        else:
            _checked.append(temp)
            for child in self.node_con_return(temp):
                if child not in _checked and not stack.inside(child):
                    stack.push(child)
            return self.dfs(final, stack, _checked)
    ## depth first serach using class Stack <--
