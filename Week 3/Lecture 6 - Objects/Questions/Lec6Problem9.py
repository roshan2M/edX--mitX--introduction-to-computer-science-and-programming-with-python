# Lecture 6, Problem 9

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a']))
del animals['b']
print(len(animals))
print(animals.values())