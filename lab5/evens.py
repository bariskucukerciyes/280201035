N = int(input("How many number?"))
evens = 0
for i in range(N):
  number = int(input("Enter integer:"))
  if number % 2 == 0:
    evens += 1

print(evens/N * 100, "%")

