from users import UserManager
from products import ProductManager
from cart import CartManager
from orders import OrderManager

def main():
    # Initialize all manager classes
    user_mgr = UserManager()
    product_mgr = ProductManager()
    cart_mgr = CartManager()
    order_mgr = OrderManager()

    print("=" * 40)
    print("  WELCOME TO THE E-COMMERCE STORE")
    print("=" * 40)

    # Main application loop
    while True:
       
        # MENU : GUEST MENU this is when not logged in
        
        if not user_mgr.is_logged_in():
            print("\n--- GUEST MENU ---")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            
            choice = input("Select an option (1-3): ")
            
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_mgr.login(username, password)
                
            elif choice == '2':
                username = input("Enter new username: ")
                password = input("Enter new password (min 6 chars): ")
                user_mgr.register(username, password)
                
            elif choice == '3':
                print("Exiting the store. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")
        
       
        # MENU : USER MENu when logged in 
        
        else:
            current_username = user_mgr.current_user['username']
            
            print(f"\n--- STORE MENU ({current_username}) ---")
            print("1. View Products")
            print("2. Search Products")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove Item from Cart")
            print("6. Checkout")
            print("7. View Order History")
            print("8. Logout")
            
            choice = input("Select an option (1-8): ")
            
            if choice == '1':
                product_mgr.list_products()
                
            elif choice == '2':
                keyword = input("Enter product name to search: ")
                product_mgr.search_products(keyword)
                
            elif choice == '3':
                product_mgr.list_products()
                prod_id = input("Enter the Product ID to add: ")
                try:
                    qty = int(input("Enter quantity: "))
                    if qty > 0:
                        cart_mgr.add_to_cart(current_username, prod_id, qty)
                    else:
                        print("Quantity must be greater than zero.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for quantity.")
                    
            elif choice == '4':
                cart_mgr.view_cart(current_username)
                
            elif choice == '5':
                cart_mgr.view_cart(current_username)
                prod_id = input("Enter the Product ID to remove: ")
                cart_mgr.remove_from_cart(current_username, prod_id)
                
            elif choice == '6':
                order_mgr.checkout(current_username)
                
            elif choice == '7':
                order_mgr.view_order_history(current_username)
                
            elif choice == '8':
                user_mgr.logout()
                
            else:
                print("Invalid choice. Please try again.")

# Run th program
if __name__ == "__main__":
    main()