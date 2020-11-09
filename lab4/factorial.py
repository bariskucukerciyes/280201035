number = int(input("Enter number:"))
total = 1
if number ==0:
    print(1)
else:
    while number >= 1:
        total = number*total
        number-=1
    print(total)