a = int(input("Enter first number:")) 
b = int(input("Enter second number:"))
power = 1
while b > 0:
    b-=1
    power = power*a
print(power)