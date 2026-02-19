from storage import JsonHandler
from products import ProductManager

class CartManager:
    #manages users shopping cart persisit data to carts.json structure username: ...
    def __init__(self):
        self.filename = "carts.json"
        self.carts = JsonHandler.load_data(self.filename)
        #if the file is new or empty returns a list[]
        if isinstance(self.carts, list):
            self.carts = {}

    def add_to_cart(self, username, product_id, quantity):
        #adds items to users cart validates stocks before using
        # 1. Initialize ProductManager to check stock
        pm = ProductManager()
        product = pm.get_product_by_id(product_id)
        
        if not product:
            print("Error: Product not found.")
            return
        
        # 2. Check if requested quantity is available in stock
        if product['stock'] < quantity:
            print(f"Error: Not enough stock! Only {product['stock']} left.")
            return

        # 3. Get user's cart (create if not exists)
        if username not in self.carts:
            self.carts[username] = []
        
        user_cart = self.carts[username]

        # 4. Check if item is already in cart (if so, just update quantity)
        item_found = False
        for item in user_cart:
            if item['product_id'] == product_id:
                # Check total stock limit again (current cart qty + new qty)
                if product['stock'] < (item['quantity'] + quantity):
                    print(f"Error: Stock limit reached.")
                    return
                item['quantity'] += quantity
                item_found = True
                break
        
        # 5. If not in cart, add as new item
        if not item_found:
            user_cart.append({
                "product_id": product_id,
                "quantity": quantity
            })
            
        # 6. Save changes to file
        if JsonHandler.save_data(self.filename, self.carts):
            print(f"Item added to cart successfully!")
        else:
            print("Error saving cart.")

    def view_cart(self, username):
        #displays the users cart with details name price total returns the total cost of the cart needed for checout
        # 1. Check if cart is empty
        if username not in self.carts or not self.carts[username]:
            print("Your cart is empty.")
            return 0.0

        print(f"\n--- SHOPPING CART ({username}) ---")
        print(f"{'Name':<25} {'Qty':<5} {'Unit Price':<12} {'Subtotal'}")
        print("-" * 55)

        pm = ProductManager()
        total_cost = 0.0

        # 2. Loop through items and calculate costs
        for item in self.carts[username]:
            product = pm.get_product_by_id(item['product_id'])
            if product:
                subtotal = product['price'] * item['quantity']
                total_cost += subtotal
                print(f"{product['name']:<25} {item['quantity']:<5} ${product['price']:<11} ${subtotal:.2f}")
            else:
                # Handle case if product was deleted from DB but remains in cart
                print(f"{'Unknown Product':<25} {item['quantity']:<5} {'-':<12} {'-'}")

        print("-" * 55)
        print(f"TOTAL PAYABLE: ${total_cost:.2f}")
        return total_cost

    def remove_from_cart(self, username, product_id):
        """
        Removes an item completely from the user's cart.
        """
        if username in self.carts:
            # Filter out the item with the given product_id
            original_length = len(self.carts[username])
            self.carts[username] = [item for item in self.carts[username] if item['product_id'] != product_id]
            
            # If length changed, it means we removed something
            if len(self.carts[username]) < original_length:
                JsonHandler.save_data(self.filename, self.carts)
                print("Item removed from cart.")
            else:
                print("Item not found in cart.")

    def clear_cart(self, username):
        """
        Empties the user's cart (used after checkout).
        """
        if username in self.carts:
            self.carts[username] = []
            JsonHandler.save_data(self.filename, self.carts)