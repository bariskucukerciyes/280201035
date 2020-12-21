def harmonic(x):
    h_sum = 0
    if x == 1:
        return 1
    h_sum = (1 / x) + harmonic(x - 1)
    
    return h_sum
    
print(harmonic(5))