def get_reversed(x):
    if len(x) == 0:
        return []
    return [x.pop()] + get_reversed(x)
    
print(get_reversed([1,2,3,4])) 