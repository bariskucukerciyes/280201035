a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a <= b and a <= c:
    minimum = a

elif b <= a and b <= c:
    minimum = b

elif c <= a and c <= b:
    minimum = c
print(minimum) 