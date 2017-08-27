# Lecture 4.7, slide 1
# This is a module containing functions pertaining to circles and spheres.

pi = 3.14159

def circleArea (radius):
    return pi * (radius ** 2)

def circleCircumference (radius):
    return 2 * pi * radius

def sphereSurfaceArea (radius):
    return 4.0 * pi * (radius ** 2)

def sphereVolume (radius):
    return (4.0 / 3.0) * pi * (radius ** 3)