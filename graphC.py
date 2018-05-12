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
    
    ## --> breadth first search
    def bfs(self, initial, final):
        pass
    ## breadth first search <--

    ## --> deapth first search
    def dfs( self, stack, final, checked=list() ):      # stack(list) -- list containing the element you are beginning with (format: [initial]);
                                                        # final(int / str) -- name of the node you're trying to establish connection with;
                                                        # checked(list) -- leave empty *** internal use ***;
                                                        # --> function returns True if the two nodes are connected, otherwise it returns False;
        if len(stack) == 0:
            return False
        if stack[-1] == final:
            return True
        else:
            temp = stack[-1]
            stack.pop(-1)
            checked.append(temp)
            for child in self.node_return(temp):
                if child not in checked:    
                    stack.append(child)
            return self.dfs(final, stack, checked)
    ## deapth first search <--
