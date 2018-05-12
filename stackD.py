class Stack:
    def __init__(self):
        self.storage = list()
        
    def add(self, element):
        self.storage.append(element)
        return element

    def pop(self):
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def length(self):
        return len(self.storage)