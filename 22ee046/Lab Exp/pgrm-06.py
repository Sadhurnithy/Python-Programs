# Grocery dictionary
Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}

# Display the grocery dictionary
print("Item details before updating:\n")
print(Grocery)

# User input for stock update
print("\nWhat do you want to do?")
print("1. Add additional quantity of the cereals")
print("2. Update the price of the grocery")
print("3. Add new item")
choice = int(input("Enter your choice: "))

# Add additional quantity of cereals
if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity = int(input("Enter the quantity of item to be added: "))
    if item_name in Grocery:
        Grocery[item_name]["quantity"] += quantity
        print("\nItem details after updating:\n")
        print(Grocery)
    else:
        print("Item does not exist in the grocery list.")

# Update the price of the grocery
elif choice == 2:
    item_name = input("Enter the grocery item name: ")
    price = float(input("Enter the new price of the item: "))
    if item_name in Grocery:
        Grocery[item_name]["price"] = price
        print("\nItem details after updating:\n")
        print(Grocery)
    else:
        print("Item does not exist in the grocery list.")

# Add new item
elif choice == 3:
    item_name = input("Enter the new grocery item name: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price = float(input("Enter the price of the new item: "))
    Grocery[item_name] = {"quantity": quantity, "price": price}
    print("\nItem details after updating:\n")
    print(Grocery)

else:
    print("Invalid choice.")
