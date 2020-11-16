password = "abc123"

while True:
  p = input("Enter password: ")
  if (p == password):
    print("Welcome")
    break
  elif(p == "help"):
    print(password[0])
  else:
    print("Wrong")    
