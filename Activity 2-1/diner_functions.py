from menu_data import menu

def display_menu():
    print("\n========== MENU ==========")

    for number, item in menu.items():
        name, price = item
        print(f"{number}. {name:<15} ₱{price:.2f}")

    print("===========================")

#Ask for Order
def get_order():
    orders = {}

    while True:
        display_menu()

        while True:
            try:
                choice = int(input("\nEnter item number: "))

                if choice in menu:
                    break
                else:
                    print("Invalid choice. Please choose 1-5.")

            except ValueError:
                print("Please enter a number.")

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        # Store order
        if choice in orders:
            orders[choice] += quantity
        else:
            orders[choice] = quantity

            # Does costumer want another item?
        another = input(
            "\nDo you want to order another item? (yes/no): "
        ).lower()

        if another != "yes":
            break

    return orders

# Calculate Total
def calculate_total(orders):
    total = 0

    for choice, quantity in orders.items():
        name, price = menu[choice]
        total += price * quantity

    return total

# Print Receipt
def print_receipt(orders, total):
    print("\n")
    print("==========================================")
    print("             NIKYUUU'S DINER")
    print("             OFFICIAL RECEIPT")
    print("==========================================")

    print(f"{'ITEM':<15}{'QTY':<8}{'PRICE':<10}{'TOTAL':<10}")
    print("------------------------------------------")

    for choice, quantity in orders.items():
        name, price = menu[choice]
        item_total = price * quantity

        print(
            f"{name:<15}{quantity:<8}"
            f"₱{price:<9.2f}₱{item_total:<9.2f}"
        )

    print("------------------------------------------")

    # Discount
    discount = 0

    if total >= 500:
        discount = total * 0.10

    final_total = total - discount

    print(f"{'Subtotal:':<33}₱{total:.2f}")
    print(f"{'Discount:':<33}₱{discount:.2f}")
    print(f"{'TOTAL:':<33}₱{final_total:.2f}")

    print("==========================================")
    print("        Thank you for ordering!")
    print("==========================================")