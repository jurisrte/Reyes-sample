def my_purchases():

purchase1 = float(input("Enter amount of first purhcase: "))
purchase2 = float(input("Enter amount of second purhcase: "))
purchase3 = float(input("Enter amount of third purhcase: "))

total = (purchase1 + purchase2 + purchase3)

print("Total amount of purchased: ", total)

if total > 100:
    confirmation = input("You are egible to apply 10% discount. Do you want to apply it? Type 'Yes' to confirm. ")
    if confirmation.lower() == "yes":
        print("You have succesfully apply a 10% discount! ")
        new_total = total * 0.9 
        print("Your new total is now ", new_total)
        payment = float(input("Enter your payment: "))
        if payment >= new_total:
            print("You have successfuly purchased the item! ")
            change = payment - new_total
            print("Change: ", change)
        else:
            print("Not enough payment")
    else: 
        print("Invalid input")
else:
    payment = float(input("Enter your payment: "))
    if payment >= total:
            print("You have successfuly purchased the item! ")
            change = payment - total
            print("Change: ", change)
    else:
            print("Not enough payment")

my_purchases()

buy_again = input("Do you want to purchase again?: ")

if buy_again.lower() == "yes":
    my_purchases()
else: 
     print("Thank you for shopping!")