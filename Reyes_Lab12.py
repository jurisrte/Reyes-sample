def display_menu():  # Function for displaying menu
    print("Menu:")
    print("1. Burger - P45.00")
    print("2. Pizza - P125.00")
    print("3. Soda - P20.00")

def get_item_price(choice):  # get the item price
    menu_prices = {1: 45.00, 2: 125.00, 3: 20.00}
    return menu_prices.get(choice, 0)

def calculate_change(total, cash):
    return cash - total

display_menu() # Main function
choice = int(input("Enter the number of the item you'd like to order: "))
price = get_item_price(choice)

if price == 0:
    print("Invalid choice.")
else:
    print(f"Your total is P{price:.2f}")
    while True:
        cash = float(input("Enter cash amount: "))
        if cash >= price:
            change = calculate_change(price, cash)
            print(f"Payment successful. Your change is P{change:.2f}")
            break
        else:
            print("Insufficient amount. Please provide enough cash.")
