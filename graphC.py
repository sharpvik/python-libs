class Graph:
    def __init__(self):
        self.nodes_counter = 0
        self.nodes_dict = dict()

    def node_add(self, name):
        self.nodes_dict.update( { name : list() } )
        self.nodes_counter += 1
        return name

    def node_del(self, name):
        self.nodes_dict.pop(name, None)
        for each in self.nodes_dict:
            self.nodes_dict[each].remove(name)
        self.nodes_counter -= 1
        return name

    def connection_add(self, one, two):
        self.nodes_dict[one].append(two)
        self.nodes_dict[two].append(one)
        return [one, two]

    def connection_del(self, one, two):
        self.nodes_dict[one].remove(two)
        self.nodes_dict[two].remove(one)
        return [one, two]

    def nodes_count(self):
        return self.nodes_counter

    def nodes_return(self):
        return self.nodes_dict

    def node_return(self, name):
        return self.nodes_dict[name]
