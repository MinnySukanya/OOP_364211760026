"""
Name: {นางสาวสุกัญญา ขุนทนะ}
SID: {364211760026}
Group: {MIT221}
"""

# display
def display_my_laptop():
    if len(my_laptop) ==0:
        print("You had laptop data")
    else:
        print(f"f you had {len(my_laptop)}follwing:')
    for x in my_laptop:

#option
def display_option():
    select = 0
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add laptop ")
    print("2.Display all laptop")
    print("3.exit")
    select = int(input("select(1-3)? : ) "
    if select == 1:
        input_my_laptop()
    elif select == 2:
        display_my_laptop()
    elif select == 3:
        print("thank you.")
        exit(0)
    else:
        print("Please, elect number 1-3.")

#input_data
def input_my_laptop():
    Brand = input("Enter my_laptop Bran : ")
    Model = input("Enter my_laptop Model : ")
    CPU = input("Enter my_laptop CPU : ")
    RAM = input ("Enter my_laptop RAM : ")
    Display = input ("Enter my_laptop Display : ")
    Storage = input ("Enter my_laptop Storage : ")
    Price = input ("Enter my_laptop Price : ")
    return (Brand,Model,CPU,RAM,Display,Storage,Price) # return as tuple
    my_laptop.append(my_laptop(Brand,Model,CPU,RAM,Display,Storage,Price))
    print("\n---------------------------")
    print("Already app laptop to store.")
    print("\n---------------------------")

my_laptop = []
s = 0
while s == 0:
    display_my_laptop()