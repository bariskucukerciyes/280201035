number = int(input("Enter number:"))
if number < 10:
  total = number
else:
  ones = number % 10
  tens = (number//10)%10
  total = ones + tens
print(total)    