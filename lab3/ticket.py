Age = int(input("Enter Age:"))
ticket_price = 3

if Age < 6 or Age > 60 :
    ticket_price *= 0

elif Age >= 6 and Age <= 18:
    ticket_price *= 0.5

print("Ticket price is",ticket_price,"liras.")