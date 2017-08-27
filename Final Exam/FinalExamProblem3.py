# Final Exam, Problem 3

def dict_invert(d):
    '''
    Assumes d is a dictionary
    Returns an inverted dictionary with ordered lists
    '''
    inv_dict = {}
    for k, v in d.items():
        inv_dict[v] = inv_dict.get(v, [])
        inv_dict[v].append(k)
        inv_dict[v].sort()
    return inv_dict