from storage import load_data, save_data
from datetime import datetime

ORDERS_FILE = "orders.json"


class OrderSystem:

    def __init__(self):
        self.orders = load_data(ORDERS_FILE, [])

    def save(self):
        save_data(ORDERS_FILE, self.orders)

    def create_order(self, username, items, total):
        order_id = f"O{len(self.orders)+1:04d}"

        order = {
            "order_id": order_id,
            "username": username,
            "items": items,
            "total": total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.orders.append(order)
        self.save()

        return order

    def get_user_orders(self, username):
        return [o for o in self.orders if o["username"] == username]
