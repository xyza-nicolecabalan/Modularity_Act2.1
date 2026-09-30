from diner_functions import display_menu, get_order, calculate_total, print_receipt

# MAIN PROGRAM
print("==========================================")
print("       WELCOME TO NIKYUUU'S DINER")
print("==========================================")

display_menu()

choice = input("\nDo you want to order? (yes/no): ").lower()

if choice == "yes":
    orders = get_order()

    total = calculate_total(orders)

    print_receipt(orders, total)

else:
    print("\nThank you for dining with us!")
    print("Enjoy!")

if __name__ == "__main__":
    main()