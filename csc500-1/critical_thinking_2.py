# @author sabath rodriguez
# @date 04/15/2024

# ask the user if they want to run part 1 or part 2
try:
    part = int(input('Enter 1 to run part 1 or 2 to run part 2 (or 3 for both): '))
except:
    print("Please enter 1 or 2 to run part 1 or part 2.")
    exit()

if part == 1 or part == 3:
    # part 1
    # Write a program that uses nested loops to collect data 
    # and calculate the average rainfall over a period of years.
    # The program should first ask for the number of years. 
    # The outer loop will iterate once for each year. The inner
    # loop will iterate twelve times, once for each month. Each
    # iteration of the inner loop will ask the user
    # for the inches of rainfall for that month. 
    # After all iterations, the program should display the number
    # of months, the total inches of rainfall, and the average rainfall
    # per month for the entire period.

    print("Part 1--------------------------------------------")
    try:
        # Get the number of years.
        years = int(input('Enter the number of years we will use to calculate rainfaull(as a number): '))
    except:
        print("Please enter an integer number for the number of years.")

    # Initialize an accumulator for the total rainfall.
    total_rainfall = 0.0

    # Initialize a 2D list to keep track of the rainfall for each month for each year.
    rainfall = [0] * 12

    # Initialize a var for total number of months
    total_months = years * 12

    for year in range(years):
        for month in range(12):
            try:
                # Get the inches of rainfall for the month.
                inches = float(input(f'Enter the inches of rainfall for year {year + 1} and month {month + 1}: (as a number)'))
            except:
                print("Please enter a number for the inches of rainfall.")
                exit()
            # Add the inches to the total.
            total_rainfall += inches

            # append total number of inches for a given month
            rainfall[month] += inches

    # print total number of months
    print(f'Total number of months: {total_months}')

    # print total inches of rainfall
    print(f'Total inches of rainfall: {total_rainfall}')

    # used to represent the month
    i = 1
    # print average rainfall per month
    for rain in rainfall:
        print(f'Average rainfall for month: {i} : {rain / years}')
        i += 1

if part == 2 or part == 3:
    # part 2
    # The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

    # If a customer purchases 0 books, they earn 0 points.
    # If a customer purchases 2 books, they earn 5 points.
    # If a customer purchases 4 books, they earn 15 points.
    # If a customer purchases 6 books, they earn 30 points.
    # If a customer purchases 8 or more books, they earn 60 points.
    # Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
    print("Part 2--------------------------------------------")

    # function used to calculate points
    # parameters: books - number of books purchased
    # returns: points - number of points awarded
    def calculate_points(books):
        if books == 0:
            return 0
        elif books == 2:
            return 5
        elif books == 4:
            return 15
        elif books == 6:
            return 30
        elif books >= 8:
            return 60

    try:
        # Get the number of books purchased.
        books = int(input('Enter the number of books you have purchased this month: '))
    except:
        print("Please enter an integer number for the number of books purchased.")

    # calculate points
    points = calculate_points(books)

    # print points
    print(f'Number of points awarded: {points}')