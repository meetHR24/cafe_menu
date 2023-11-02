
menu = {
    "Espresso": 2.50,
    "Cappuccino": 3.00,
    "Latte": 3.25,
    "Mocha": 3.50,
    "Iced Coffee": 3.00,
    "Tea": 2.00,
    "Muffin": 2.50,
    "Croissant": 2.75,
}


def display_menu():
    print("=== Cafe Menu ===")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def take_order():
    order = {}
    while True:
        item = input("Enter the item you want to order (or 'q' to quit): ")
        if item == 'q':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found on the menu. Please try again.")
    return order


def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total


while True:
    display_menu()
    order = take_order()
    total_cost = calculate_total(order)

    print("=== Order Summary ===")
    for item, quantity in order.items():
        print(f"{item}: {quantity} x ${menu[item]:.2f} = ${quantity * menu[item]:.2f}")
    print(f"Total: ${total_cost:.2f}")

    another_order = input("Place another order? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print("Thank you for visiting the cafe!")
