def is_prime(x):
    prime_check = 1
    for i in range(2,x):
        if x % i == 0 :
            prime_check = 0
    if x < 2:
        return False
    elif prime_check == 1:
        return True
    elif prime_check == 0:
        return False

def print_primes_between(x,y):
    prime_list = []
    if x < y:
        for i in range(x+1,y):
            if is_prime(i) == True:
                prime_list.append(i)
    elif y < x:
        for i in range(y+1,x):
            if is_prime(i) == True:
                prime_list.append(i)
    return prime_list            

def main():
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))

  return print(print_primes_between(num1, num2))

main()

