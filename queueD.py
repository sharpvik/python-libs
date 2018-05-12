class Queue:
    def __init__(self):
        self.storage = list()

    def ins(self, element):
        self.storage.insert(0, element)
        return element

    def pop(self):
        temp = self.storage[0]
        self.storage.pop(0)
        return temp
    
    def length(self):
        return len(self.storage)
