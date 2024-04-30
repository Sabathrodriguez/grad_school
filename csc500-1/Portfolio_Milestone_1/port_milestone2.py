# @author sabath rodriguez
# @date 04/20/2024

# Build the ShoppingCart class with 
# the following data attributes and 
# related methods. Note: Some can be 
# method stubs (empty methods) initially,
# to be completed in later steps

from port_milestone1 import ItemToPurchase

# shopping cart class
class ShoppingCart:
    # constructor
    def __init__(self, name="none", date="January 1, 2020"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    
    # add item to cart
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)
    
    # remove item from cart
    def remove_item(self, itemName):
        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    # modify item
    def modify_item(self, itemToPurchase):
        for item in self.cart_items:
            if item.item_name == itemToPurchase.item_name:
                # check if itemtopurchase has default values    
                if itemToPurchase.item_price != 0.0 and itemToPurchase.item_name != "none" and itemToPurchase.quantity != 0:
                    item.item_price = itemToPurchase.item_price
                    item.item_quantity = itemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    # get number of items in cart
    def get_num_items_in_cart(self):
        num = 0
        for item in self.cart_items:
            num += item.item_quantity
        return num

    # get total cost of all items in cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

     # print cart total cost
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: " + str(self.get_num_items_in_cart()))
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print("Total: ${}".format(self.get_cost_of_cart()))
    
    # print cart description(s)
    def print_descriptions(self):        
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)
    
def print_menu(shoppingCart):
    # user input
    user_input = ""

    while user_input != "q":
        # print menu
        print('''MENU
              a - Add item to cart
              r - Remove item from cart
              c - Change item quantity
              i - Output items' descriptions
              o - Output shopping cart
              q - Quit
              ''')
        user_input = input("Choose an option:")
        
        # check user input
        if user_input != "a" and user_input != "r" and user_input != "c" and user_input != "i" and user_input != "o" and user_input != "q":
            print("Please enter a valid option")
            continue
        else:
            if user_input == "a":
                # add item
                item = ItemToPurchase()
                item.item_name = input("Enter the item name:")
                item.item_description = input("Enter the item description:")
                item.item_price = float(input("Enter the item price:"))
                item.item_quantity = int(input("Enter the item quantity:"))
                shoppingCart.add_item(item)
            elif user_input == "r":
                # remove item
                item_name = input("Enter the name of the item to remove:")
                shoppingCart.remove_item(item_name)
            elif user_input == "c":
                # modify item
                item = ItemToPurchase()
                item.item_name = input("Enter the item name:")
                item.item_price = float(input("Enter the new price:"))
                item.item_quantity = int(input("Enter the new quantity:"))
                shoppingCart.modify_item(item)
            elif user_input == "i":
                # print descriptions
                print("\nOUTPUT ITEMS' DESCRIPTIONS")
                shoppingCart.print_descriptions()
                print()
            elif user_input == "o":
                # print cart
                print("\nOUTPUT SHOPPING CART")
                shoppingCart.print_total()
                print()
            elif user_input == "q":
                break
print("portfolio milestone 2----------------")

try:
    # create shopping cart
    username = input("Enter your name: (such as \"John\")")
    todaysDate = input("Enter the current date: (such as \"April 1, 2020\")")

    # if username or todaysDate is empty, create shopping cart with default values
    if len(username) > 0 and len(todaysDate) > 0:
        shoppingCart = ShoppingCart(username, todaysDate)        
    else:
        shoppingCart = ShoppingCart()

    print_menu(shoppingCart)
except:
    print("Error, please try again.")