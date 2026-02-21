from storage import load_data, save_data

PRODUCTS_FILE = "products.json"


class ProductCatalog:

    def __init__(self):
        self.products = load_data(PRODUCTS_FILE, [])

        
        if not self.products:
            self.products = [
                {"product_id": "P1001", "name": "USB-C Cable", "price": 9.99, "stock": 30},
                {"product_id": "P1002", "name": "Wireless Mouse", "price": 19.99, "stock": 15}
            ]
            self.save()

    def save(self):
        save_data(PRODUCTS_FILE, self.products)

    def list_products(self):
        return self.products

    def search(self, keyword):
        keyword = keyword.lower()
        return [p for p in self.products if keyword in p["name"].lower()]

    def get_product(self, pid):
        for p in self.products:
            if p["product_id"] == pid:
                return p
        return None

    def reduce_stock(self, pid, qty):
        product = self.get_product(pid)
        if product:
            product["stock"] -= qty
            self.save()
