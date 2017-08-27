# Lecture 6, slide 2

# Making Tuples
t1 = (1, 'two', 3)
print(t1)

# Putting Tuples Together
t2 = (t1, 'four')
print(t2)

# Concatenation on Tuples
print(t1 + t2)

# Indexing on Tuples
print((t1 + t2)[3])

# Slicing on Tuples
print((t1 + t2)[2:5])

# Singleton
t3 = ('five',)
print(t1 + t2 + t3)