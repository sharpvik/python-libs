class PriorQ:
    def __init__(self, element=None):
        if isinstance(element, None):       # ???
            self.storage = list()
        elif isinstance(element, list):     # ???
            self.storage = list( sorted(element) )
        else:
            self.storage = [element]

    def push(self, element):
        done = False
        for i in range( self.length() ):
            if element < self.storage[i]:
                self.storage.insert(i, element)
                done = True
                break
        if not done:
            self.storage.append(element)
        return element

    def pop(self):
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def peek(self):
        return self.storage[-1]

    def length(self):
        return len(self.storage)

    def is_empty(self):
        return self.length() == 0

    def inside(self, element):
        return element in self.storage