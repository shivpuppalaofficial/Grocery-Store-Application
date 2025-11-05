import csv

PRODUCTS_FILE = 'products.csv'

def load_products():
    products = []
    try:
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        print("⚠️ No product file found. Starting with an empty store.")
    return products

def save_products(products):
    with open(PRODUCTS_FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def view_products(products):
    print("\n📦 Available Products:")
    print("ID | Name | Price | Quantity")
    for p in products:
        print(f"{p['id']} | {p['name']} | ₹{p['price']} | {p['quantity']}")

def add_product(products):
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity: ")

    products.append({'id': pid, 'name': name, 'price': price, 'quantity': quantity})
    save_products(products)
    print("✅ Product added successfully!")

def update_stock(products):
    pid = input("Enter Product ID to update: ")
    for p in products:
        if p['id'] == pid:
            new_qty = input("Enter new quantity: ")
            p['quantity'] = new_qty
            save_products(products)
            print("✅ Quantity updated successfully!")
            return
    print("❌ Product not found.")

def generate_bill(products):
    bill_items = []
    total = 0

    while True:
        pid = input("Enter product ID (or 'done' to finish): ")
        if pid.lower() == 'done':
            break
        for p in products:
            if p['id'] == pid:
                qty = int(input("Enter quantity: "))
                if qty <= int(p['quantity']):
                    amount = int(p['price']) * qty
                    total += amount
                    bill_items.append((p['name'], qty, amount))
                    p['quantity'] = str(int(p['quantity']) - qty)
                else:
                    print("❌ Not enough stock.")
                break
        else:
            print("❌ Product not found.")

    save_products(products)
    print("\n🧾 Bill Summary:")
    for item in bill_items:
        print(f"{item[0]} x {item[1]} = ₹{item[2]}")
    print(f"Total: ₹{total}")
    print("✅ Thank you for shopping with us!")

def main():
    products = load_products()
    while True:
        print("\n=== Grocery Store Management ===")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Generate Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            update_stock(products)
        elif choice == '4':
            generate_bill(products)
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
