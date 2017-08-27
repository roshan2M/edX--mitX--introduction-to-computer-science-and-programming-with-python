# Lecture 11, Problem 6

class Queue(object):
    elements = []
    def __init__(self):
        self.elements = []
    
    def insert(self, x):
        self.elements.append(x)
    
    def remove(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            raise ValueError()