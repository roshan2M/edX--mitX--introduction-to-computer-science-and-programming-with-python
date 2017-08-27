# Lecture 11.2, slide 10

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print c.x, origin.x