from storage import JsonHandler

class ProductManager:
    #manages product catalog operation:listing loading and searching products
    def __init__(self):
        #when the class start load products from file
        self.filename = "products.json"
        self.products = JsonHandler.load_data(self.filename)
    def load_products(self):
        #reloads the product list from json file gets stock update
        self.products = JsonHandler.load_data(self.filename)
        
    def list_products(self):
        #display availabile products 
        self.load_products()
        print("\n--- PRODUCT CATALOG ---")
        if not self.products:
            print("no products available in the store")
            return
        #print table headers
        print(f"{'ID' :<10} {'Name' :<25} {'price' :<10} {'stock'}")
        print("-" * 55)

        #loop through products and print details
        for product in self.products:
            print(f"{product['id']:<10} {product['name']:<25} ${product['price']:<9} {product['stock']}")
        print("-" * 55)

    def search_products(self, keyword):
        #search for produccts contain the keyword 
        print(f"\nSearching for '{keyword}'...")
        found = False
        
        print(f"{'ID':<10} {'Name':<25} {'Price':<10} {'Stock'}")
        print("-" * 55)

        for product in self.products:
            #convert both name and keyword to lovercase for easy match:
            if keyword.lower() in product['name'].lower():
                print(f"{product['id']:<10} {product['name']:<25} ${product['price']:<9} {product['stock']}")
                found = True
        
        if not found:
            print("No matching products found.")
        print("-" * 55)

    def get_product_by_id(self, product_id): 
        #helper finds the product by ıd  returns ıf there is no found used by cart system
        self.load_products()
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def update_stock(self, product_id, quantity):
        #reduces the stock of a product after purshcase used by checkout systm
        self.load_products()
        for product in self.products:
            if product['id'] == product_id:
                product['stock'] -= quantity
                # Save the updated list back to file immediately
                JsonHandler.save_data(self.filename, self.products)
                return True
        return False