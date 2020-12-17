def binary_to_dec(b):
    d = 0
    b = str(b)
    b_rev = str(b[::-1])
    for i in range(len(b_rev)):
        if b_rev[i] == "1":
            d += 2**i
    return d

def dec_to_binary(d):
    b = ""
    d = int(d)   
    while d != 0:    
        if d % 2 == 0:
            b += "0"
        elif d % 2 == 1:
            b += "1"
        d = d // 2    
    b_rev = b[::-1]
    return b_rev

def main():
b = "10010"
print(binary_to_dec(b))
d = 18
print(dec_to_binary(d))

main()