total= 0
num= 7
print(f"Enter {num} product entries (product number and quantity sold):")
for i in range(num):
    user = input(f"Entry {i+1}: ")
    parts = user.split()
    if len(parts) == 2:
        product = int(parts[0])
        quantity = int(parts[1])
        if product == 1:
            price = 2.98
        elif product == 2:
            price = 4.50
        elif product == 3:
            price = 9.98
        elif product == 4:
            price = 4.49
        elif product == 5:
            price = 6.87
        else:
            print("Invalid product number. Skipping entry.")
            continue
        total += price * quantity
    else:
        print("Invalid input format. Skipping entry.")
print(f"\nTotal retail value of all products sold: ${total:.2f}")
