# @author Sabath Rodriguez
# @date 04/29/2024

# classes dictionary
# dictionary will contain dictionaries of teacher, classroom, and time
classes = {}

classes["CS101"] = {"room number" : 3004, "instructor" : "Haynes", "time" : "8:00 a.m."}
classes["CS102"] = {"room number" : 4501, "instructor" : "Alvarado", "time" : "9:00 a.m."}
classes["CS103"] = {"room number" : 6755, "instructor" : "Rich", "time" : "10:00 a.m."}
classes["NET110"] = {"room number" : 1244, "instructor" : "Burke", "time" : "11:00 a.m."}
classes["COM241"] = {"room number" : 1411, "instructor" : "Lee", "time" : "1:00 p.m."}

# print classes from classes dictionary
def print_classes():
    for key in classes:
        print(key)

user_choice = ""

# loop until user quits
# print class from user input
while user_choice != "q":
    print("Here are your classes:")
    print_classes()
    user_choice = input("Enter the class you are looking for (q to quit): ")
    if user_choice in classes:
        print("Class: " + user_choice)
        print("Room Number: " + str(classes[user_choice]["room number"]))
        print("Instructor: " + classes[user_choice]["instructor"])
        print("Time: " + classes[user_choice]["time"])
    elif user_choice != "q":
        print("Class not found.")

