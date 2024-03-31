# @written by Sabath Rodriguez
# @date 03/31/2024

# Part 1:
# Write a program that calculates the total 
# amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the 
# charge for the food and then calculate the 
# amounts with an 18 percent tip and 7 percent 
# sales tax. Display each of these amounts and 
# the total price.

print("------Part 1 -------------------------------")

# get total amount for meal from user
total_amount = float(input("How much was the total amount for the food?"))

# amount with tip and tax
total_amount_tip = (total_amount * 0.18)
total_amount_tax = (total_amount * 0.07)

print("Total amount below:")
print("Tax: ${:.2f}, Tip: ${:.2f}, Total: ${:.2f}".format(total_amount_tax, total_amount_tip, (total_amount_tip+total_amount_tax+total_amount)))

print("------Part 2 -------------------------------")

# Part 2:
# Many people keep time using a 24-hour 
# clock (11 is 11am and 23 is 11pm, 0 is 
# midnight). If it is currently 13 and you
# set your alarm to go off in 50 hours, it 
# will be 15 (3pm). Write a Python program 
# to solve the general version of the above 
# problem. Ask the user for the time now (in hours) 
# and then ask for the number of hours to wait 
# for the alarm. Your program should output 
# what the time will be on a 24-hour clock when 
# the alarm goes off.

# get time and time for alarm from users
time_hours = int(input("What's the time in hours?"))
time_til_alarm = int(input("How many hours until alarm?"))

# time alarm will go off
time_diff = (time_hours + time_til_alarm) % 24

print("The alarm will go off at: {:d}".format(time_diff))