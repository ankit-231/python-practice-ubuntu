shopping_cart = []

product_list = ['Salad Server Set', 'Party Serviette Holder', 'Tea Set', 'Mixing Bowl Set', 'Knife Block Set', 'Coffee Capsule Holder', 'Plastic Sensor Soap Pump', 'Storage Bucket', 'Oven Glove', 'Apron', 'Biscuit Barrel', 'Chopping Board', 'Carioca Cups', 'Soup Bowls', 'Elevate Wood Turner', 'Pasta Machine', 'Teapot', 'Cake Pop Scoop', 'Cookbook Stand', 'Chocolate Station', 'Coffee Maker', 'Pepper Mill', 'Salt Mill', 'Glass Storage Jar', 'Measuring jug', 'Kitchen Scale', 'Tenderiser', 'Pizza Docker', 'Knife Sharpener', 'Steel Cork Opener', 'Steel Garlic Press', 'Steel Can Opener', 'Stainless Steel Crank Flour Sifter', 'Mineral Stone Mortar and Pestle', 'Citrus Cather', 'Cherry & Olive Pitter', 'Multi Grater-Detachable', 'Stainless Steel Colander', 'Steel Pizza Pan', 'Pop Container']
price_list = [18.70, 11.95, 39.95, 49.95, 99.95, 29.95, 79.95, 24.95, 9.95, 29.95, 39.95, 12.95, 54.95, 43.00, 19.95, 144.95, 29.95, 9.95, 29.95, 34.95, 29.00, 84.94, 84.95, 4.95, 19.95, 39.95, 34.95, 19.95, 79.95, 36.95, 34.95, 36.95, 33.95, 74.95, 19.95, 27.95, 26.95, 44.95, 12.95, 22.95]
product_codes = list(range(1, len(product_list) + 1))


shop_record_list = []

def add_record():
    while True:
        pro_code = input("Enter Product Code: ")
        if pro_code == 'END':
            break
        try:
            pro_code = int(pro_code)
            if is_valid_code(pro_code):
                pro_name = product_list[pro_code % len(product_list)]
                price = price_list[pro_code % len(price_list)]
                quantity = int(input("Enter Quantity: "))
                if is_valid_quantity(quantity):
                    ship_method = input("Pick-up / Delivery: ").strip().lower()
                    if ship_method in ['pick-up', 'delivery']:
                        value = "High" if price >= 30 else "Low"
                        ship_cost = price * 0.1 if ship_method == "delivery" else 0
                        pack_fee = 3 if ship_method == "delivery" and value == "High" else 0
                        record = [pro_code, pro_name, quantity, value, price, ship_method, ship_cost, pack_fee]
                        shop_record_list.append(record)
                    else:
                        print("Invalid shipping method.")
                else:
                    print("Invalid Quantity")
            else:
                print("Invalid product code.")
        except ValueError:
            print("Invalid Input")

def is_valid_code(pro_code):
    return isinstance(pro_code, int) and 0 <= pro_code < len(product_list)

def is_valid_quantity(quantity):
    return isinstance(quantity, int) and 0 <= quantity <= 49

def show_records():
    print("Catalogue: ")
    for record in shop_record_list:
        print(record)

def total_cost():
    total = 0.00
    for record in shop_record_list:
        pro_code, product_name, quantity, value, price, ship_method, ship_cost, pack_fee = record
        cost = price * quantity
        if ship_method == "delivery":
            cost += ship_cost * quantity + pack_fee * quantity
        total += cost
    print(f"TOTAL COST: ${total:.2f}")

def search_record():
    keyword = input("Enter search keyword: ").strip().lower()
    if keyword:
        results = [record for record in shop_record_list if keyword in record[1].lower()]
        print("Search Results:")
        for record in results:
            print(record)
    else:
        print("Invalid keyword.")

def main_menu():
    while True:
        print("\nHomewareCity Shopping Cart System")
        print("1. Add Record")
        print("2. Show Records")
        print("3. Calculate Total Cost")
        print("4. Search Record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_record()
        elif choice == '2':
            show_records()
        elif choice == '3':
            total_cost()
        elif choice == '4':
            search_record()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main_menu()