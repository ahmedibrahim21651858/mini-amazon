from storage import load_data, save_data

CART_FILE = "carts.json"


class CartSystem:

    def __init__(self):
        self.carts = load_data(CART_FILE, {})

    def save(self):
        save_data(CART_FILE, self.carts)

    def get_cart(self, username):
        return self.carts.setdefault(username, {})

    def add_item(self, username, product, qty):
        if qty <= 0:
            return False

        cart = self.get_cart(username)

        if qty > product["stock"]:
            return False

        pid = product["product_id"]

        cart[pid] = cart.get(pid, 0) + qty
        self.save()
        return True

    def remove_item(self, username, pid):
        cart = self.get_cart(username)
        if pid in cart:
            del cart[pid]
            self.save()

    def clear_cart(self, username):
        self.carts[username] = {}
        self.save()
