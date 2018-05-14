class Queue:                                # standard queue datatype;
    def __init__(self, element=None):
        if isinstance(element, list):
            self.storage = element
        else:
            self.storage = [element]

    def ins(self, element):                 # element(int / str) -- element you want to insert into the Queue;
                                            # --> function returns name of the inserted elment;
        self.storage.append(element)
        return element

    def pop(self):                          # --> function pops the first element you put into the Queue and returns its name;
        temp = self.storage[0]
        self.storage.pop(0)
        return temp
    
    def length(self):                       # --> function returns number of elements in the Queue;
        return len(self.storage)

    def inside(self, element):              # element(int / str) -- name of element you want to check for;
                                            # --> function returs True if element is in the Queue, otherwise, returns False;
        return element in self.storage
