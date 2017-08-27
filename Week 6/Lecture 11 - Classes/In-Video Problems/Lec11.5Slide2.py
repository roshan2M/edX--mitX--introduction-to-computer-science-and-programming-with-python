# Lecture 11.5, slide 2

class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """

    def __init__(self):
        """
        Create an empty set of integers
        """
        self.vals = []

    def insert(self, e):
        """
        Assumes e is an integer and inserts e into self
        """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """
        Assumes e is an integer
        Returns True if e is in self, and False otherwise
        """
        return e in self.vals

    def remove(self, e):
        """
        Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """
        Returns a string representation of self
        """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

"""
Some simple commands to manipulate the set of integers
"""
s = intSet()
print s
s.insert(10)
s.insert(4)
s.insert(7)
s.insert(7)
print s
s.member(10)
s.member(5)
s.insert(6)
print s
s.remove(4)
print s
s.remove(4)