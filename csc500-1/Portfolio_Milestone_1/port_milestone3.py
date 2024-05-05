# @author sabath rodriguez
# @date 04/20/2024

# Build the ShoppingCart class with 
# the following data attributes and 
# related methods. Note: Some can be 
# method stubs (empty methods) initially,
# to be completed in later steps

# @author sabath rodriguez
# @date 04/05/2024

class ItemToPurchase:

    # Default constructor
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"
    
    # class method
    # prints item total cost when multiplited by quantity
    def print_item_cost(self):
        print("{:s} {:d} @ ${:.2f} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))
print("portfolio milestone 1----------------")

if (input("Want to run portfolio milestone 1? (y/n):") == "y"):
    # In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
    try:
        item1 = ItemToPurchase()
        item2 = ItemToPurchase()

        # Item 1 input
        item1.item_name = input("Please enter item 1 name(such as \"apple\"):")
        item1.item_price = float(input("Please enter item 1 price(such as 2):"))
        item1.item_quantity = int(input("Please enter item 1 quantity(such as 3):"))
        print()

        # Item 2 input
        item2.item_name = input("Please enter item 2 name(such as \"banana\"):")
        item2.item_price = float(input("Please enter item 2 price(such as 1):")) 
        item2.item_quantity = int(input("Please enter item 2 quantity(such as 5):"))
        print()

        # Total Cost
        item1.print_item_cost()
        item2.print_item_cost()

        total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

        print("Total: ${}".format(total_cost))
    except:
        print("Please enter correct format for item price and quantity")

    if (input("Want to run test cases? (y/n):") == "y"):
        print("\nRunning test cases...")
        # test cases
        # ints
        item3 = ItemToPurchase()
        item3.item_name = "apple"
        item3.item_price = 2
        item3.item_quantity = 3 

        item4 = ItemToPurchase()    
        item4.item_name = "banana"
        item4.item_price = 1
        item4.item_quantity = 5

        item3.print_item_cost()
        item4.print_item_cost()

        total_cost = (item3.item_price * item3.item_quantity) + (item4.item_price * item4.item_quantity)
        print("Total: ${}".format(total_cost))

        # floats
        item5 = ItemToPurchase()
        item5.item_name = "apple"
        item5.item_price = 2.5
        item5.item_quantity = 3

        item6 = ItemToPurchase()
        item6.item_name = "banana"
        item6.item_price = 1.5
        item6.item_quantity = 5

        item5.print_item_cost()
        item6.print_item_cost()

        total_cost = (item5.item_price * item5.item_quantity) + (item6.item_price * item6.item_quantity)
        print("Total: ${}".format(total_cost))

        # error
        try:
            item7 = ItemToPurchase()
            item7.item_name = "apple"
            item7.item_price = "2"
            item7.item_quantity = 3

            item8 = ItemToPurchase()
            item8.item_name = "banana"
            item8.item_price = 1
            item8.item_quantity = 5

            #should produce an error message regarding different types
            item7.print_item_cost()
            item8.print_item_cost()
        except ValueError as e:
            print("Error: Different types")

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
                if itemToPurchase.item_name != "none" and itemToPurchase.item_quantity != 0:
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
print("portfolio milestone 3----------------")

try:
    # create shopping cart
    username = input("Enter your name: (such as \"John\")")
    todaysDate = input("Enter the current date: (such as \"April 1, 2020\")")

    print("Customer name: " + username)
    print("Today's date: " + todaysDate)

    # if username or todaysDate is empty, create shopping cart with default values
    if len(username) > 0 and len(todaysDate) > 0:
        shoppingCart = ShoppingCart(username, todaysDate)        
    else:
        shoppingCart = ShoppingCart()

    print_menu(shoppingCart)
except:
    print("Error, please try again.")


