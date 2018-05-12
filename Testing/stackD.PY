class Stack:
    def __init__(self, element):
        if isinstance(element, list):
            self.storage = element
        else:
            self.storage = [element]
        
    def add(self, element):
        self.storage.append(element)
        return element

    def pop(self):
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def length(self):
        return len(self.storage)