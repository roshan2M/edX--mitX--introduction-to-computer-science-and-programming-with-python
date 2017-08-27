# Optional Problem Set, Question 1

def nfruits(fruits, eaten):
    '''
    assumes fruits is a dictionary of the fruits Python had at start of journey
    assumes eaten is a string of the fruits Python ate on the journey
    '''
    assert type(fruits) == dict and len(fruits) <= 10, 'must be dictionary of less than 10 elements'
    assert type(eaten) == str, 'must be a string of fruits eaten'
    
    for letter in range(len(eaten)):
        for key in fruits:
            if key == eaten[letter]:
                fruits[key] -= 1
            elif key != letter and letter != len(eaten) - 1:
                fruits[key] += 1
    
    return max(fruits.values())