# Optional Problem Set, Question 1
# This function calculates the sum of the area of a regular polygon and the square of its perimeter.
# The given inputs are n, the number of sides, and s, the length of each side.

import math

def polysum (n, s):
    area = (0.25 * n * s ** 2) / math.tan (math.pi / n)
    perimeter = n * s
    return round (area + perimeter ** 2, 4) # Rounds the sum to 4 decimal places.