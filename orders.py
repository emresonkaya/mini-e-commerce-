import datetime
import random
from storage import JsonHandler
from products import ProductManager
from cart import CartManager

class OrderManager:
    #this one ill handle checkout process stock updates and orders history
    def __init__(self):
        self.filename = "orders.json"
        self.orders = JsonHandler.load_data(self.filename)

    def checkout(self, username):
        """
        Processes the checkout for a user.
        1. Validates stock
        2. Deducts stock
        3. Saves order
        4. Clears cart
        """
        #initialize managers
        cart_mgr = CartManager()
        product_mgr = ProductManager()

        #get users cart
        if username not in cart_mgr.carts or not cart_mgr.carts[username]:
            print("Checkout failed:Cart is empty.")
            return False
        
        user_cart = cart_mgr.carts[username]
        total_cost = 0.0
        order_items= []

        #final stock checks and calculations 
        for item in user_cart:
            product = product_mgr.get_product_by_id(item['product_id'])

            if not product:
                print(f"Error: Product {item['product_id']} no longer exists.")
                return False
            
            if product['stock'] < item['quantity']:
                print(f"Error: Not enough stock for {product['name']}. Available: {product['stock']}")
                return False
            
            # Calculate cost for this item
            item_total = product['price'] * item['quantity']
            total_cost += item_total
            
            # Prepare item data for the receipt
            order_items.append({
                "product_id": item['product_id'],
                "name": product['name'],
                "quantity": item['quantity'],
                "unit_price": product['price'],
                "subtotal": item_total
            })

        # Payment and stock change
        print("Processing payment...")
        
        for item in user_cart:
            # Deduct from actual stock using ProductManager
            success = product_mgr.update_stock(item['product_id'], item['quantity'])
            if not success:
                print("Critical Error: Stock update failed during checkout.")
                return False

        #  Create order record (Receipt)
        new_order = {
            "order_id": str(random.randint(10000, 99999)),
            "username": username,
            "items": order_items,
            "total_price": total_cost,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        #  Save order & clear cart
        self.orders.append(new_order)
        JsonHandler.save_data(self.filename, self.orders)
        
        cart_mgr.clear_cart(username)
        
        # Print Receipt
        print("\n" + "="*30)
        print(f"ORDER SUCCESSFUL! (ID: {new_order['order_id']})")
        print("="*30)
        for item in order_items:
            print(f"- {item['name']} (x{item['quantity']}): ${item['subtotal']:.2f}")
        print("-" * 30)
        print(f"TOTAL PAID: ${total_cost:.2f}")
        print("="*30 + "\n")
        
        return True

    def view_order_history(self, username):
        # Displays the old orders for the logged user 
        self.orders = JsonHandler.load_data(self.filename)
        print(f"\n--- ORDER HISTORY ({username}) ---")
        found = False
        for order in self.orders:
            if order['username'] == username:
                print(f"Order ID: {order['order_id']} | Date: {order['timestamp']}")
                print(f"Total: ${order['total_price']:.2f}")
                print("Items:")
                for item in order['items']:
                    print(f"  * {item['name']} (x{item['quantity']})")
                print("-" * 30)
                found = True
        
        if not found:
            print("No previous orders found.")