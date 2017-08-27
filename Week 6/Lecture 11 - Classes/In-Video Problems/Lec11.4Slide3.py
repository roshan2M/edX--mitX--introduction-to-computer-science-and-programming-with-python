# Lecture 11.4, slide 3
import math

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print c.x, origin.x
print c
print c.distance(origin)