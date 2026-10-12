
products = {
    "Apple": {"price": 100, "quantity": 100},
    "Banana": {"price": 200, "quantity": 200},
    "Mango": {"price": 300, "quantity": 100},
    "Grapes": {"price": 400, "quantity": 200},
    "Pineapple": {"price": 100, "quantity": 100},
    "Peach": {"price": 200, "quantity": 200}
}

cart = {}

def add_to_cart():
    name = input("Enter product name: ").title()

    try:
        product = products[name]
    except KeyError:
        print("Product does not exist!")
        return

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    available = product["quantity"] - cart.get(name, 0)

    if quantity > available:
        print("Not enough stock available!")
        print("Available quantity:", available)
        return

    if name in cart:
        cart[name] = cart[name] + quantity
    else:
        cart[name] = quantity

    print(name, "added to cart successfully!")

def calculate_total():
    total = 0

    for name in cart:
        price = products[name]["price"]
        quantity = cart[name]
        total = total + price * quantity

    return total

def display_cart():
    if not cart:
        print("Your cart is empty!")
        return

    print("\n========== SHOPPING CART ==========")

    for name in cart:
        price = products[name]["price"]
        quantity = cart[name]
        subtotal = price * quantity

        print("Product:", name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Subtotal:", subtotal)
        print("-----------------------------------")

    print("Total Bill:", calculate_total())

while True:
    print("\n===== SHOPPING MENU =====")
    print("1. Add product to cart")
    print("2. Display cart")
    print("3. Calculate total bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_to_cart()
    elif choice == "2":
        display_cart()
    elif choice == "3":
        print("Total Bill:", calculate_total())
    elif choice == "4":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid option. Please try again.")
  
    