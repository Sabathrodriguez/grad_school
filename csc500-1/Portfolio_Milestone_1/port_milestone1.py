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
