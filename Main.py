from users import UserSystem
from products import ProductCatalog
from cart import CartSystem
from orders import OrderSystem

users = UserSystem()
products = ProductCatalog()
cart = CartSystem()
orders = OrderSystem()


def show_products(items):
    for p in items:
        print(f"{p['product_id']} | {p['name']} | €{p['price']} | Stock:{p['stock']}")


def view_cart(username):
    user_cart = cart.get_cart(username)

    if not user_cart:
        print("Cart is empty.")
        return

    total = 0
    for pid, qty in user_cart.items():
        product = products.get_product(pid)
        subtotal = qty * product["price"]
        total += subtotal
        print(f"{product['name']} x{qty} = €{subtotal:.2f}")

    print("Total:", round(total, 2))


def checkout(username):
    user_cart = cart.get_cart(username)
    if not user_cart:
        print("Cart empty.")
        return

    items = []
    total = 0

    
    for pid, qty in user_cart.items():
        product = products.get_product(pid)
        if qty > product["stock"]:
            print("Stock changed. Checkout cancelled.")
            return

    for pid, qty in user_cart.items():
        product = products.get_product(pid)
        subtotal = qty * product["price"]
        total += subtotal

        products.reduce_stock(pid, qty)

        items.append({
            "product_id": pid,
            "qty": qty,
            "unit_price": product["price"]
        })

    order = orders.create_order(username, items, total)
    cart.clear_cart(username)

    print("\nOrder placed successfully!")
    print("Order ID:", order["order_id"])
    print("Total:", total)



def store_menu(username):
    while True:
        print("\nSTORE MENU")
        print("1. Browse products")
        print("2. Search products")
        print("3. View cart")
        print("4. Checkout")
        print("5. Order history")
        print("6. Logout")

        choice = input("> ")

        if choice == "1":
            show_products(products.list_products())

            pid = input("Enter product ID to add (or blank): ")
            if pid:
                product = products.get_product(pid)
                if product:
                    qty = int(input("Quantity: "))
                    if cart.add_item(username, product, qty):
                        print("Added to cart.")
                    else:
                        print("Invalid quantity.")

        elif choice == "2":
            keyword = input("Search keyword: ")
            show_products(products.search(keyword))

        elif choice == "3":
            view_cart(username)

        elif choice == "4":
            checkout(username)

        elif choice == "5":
            user_orders = orders.get_user_orders(username)
            for o in user_orders:
                print(o)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def welcome_menu():
    while True:
        print("\nWELCOME")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            success, msg = users.register(u, p)
            print(msg)

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            if users.login(u, p):
                print("Login successful.")
                store_menu(u)
            else:
                print("Invalid login.")

        elif choice == "3":
            break

        else:
            print("Invalid input.")


if __name__ == "__main__":
    welcome_menu()
