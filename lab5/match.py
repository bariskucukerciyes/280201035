a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

match = 0

while a > 0 and b > 0:
  if a % 10 == b % 10:
    match += 1
  a //= 10
  b //= 10

print(match)

