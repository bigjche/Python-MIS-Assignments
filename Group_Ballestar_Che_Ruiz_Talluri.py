import breads

def main():
    
    #Creates three bread objects
    bread1 = breads.Breads(3.00,'quinoa',20)
    bread2 = breads.Breads(2.50,'wheat',20)
    bread3 = breads.Breads(2.00,'white',20)

    #Creates two breadWithStuffing objecys
    breadStaff1 = breads.breadWithStuffing(5.00,'brioche',20,'chocolate cream')
    breadStaff2 = breads.breadWithStuffing(4.50,'whole grain',20,'strawberry cream')

    #Creates an empty list
    list1 = []

    #Adds all the objects into a list
    list1.append(bread1)
    list1.append(bread2)
    list1.append(bread3)
    list1.append(breadStaff1)
    list1.append(breadStaff2)

    #Creates a variable 
    start = 'YES'
    #Converts start to lowercase
    start = start.lower()
    
    #Creates a validation loop 
    while start == 'yes':
        #Calls the displyMenu function
        choice = displayMenu()

        #Decisions structure if choice a is chosen
        if choice == 'a':
            #Calls the retrieveBread function and stores it in bread_object
            bread_object = retrieveBread(list1)
            print()
            #Makes sure the bread_object exists
            if bread_object != -1:
                #Prompts the user for the price
                price = float(input('Please enter the price for this bread type:'))
                #Decision structure if the price is negative
                if price < 0:
                    print('New price cannot be negative!')
                    print()
                #If the number is not negative goes 
                else:
                    print("The price has been updated")
                    print()
                    bread_object.set_price(price)

        #Decision structure if choice b is chosen
        elif choice == 'b':
             #Calls the retrive bread function and stores it in bread_object
             bread_object = retrieveBread(list1)
             #Checks to see if the bread object exists
             if bread_object != -1:
                print()
                new_stuffing = input("Please enter the new stuffing for this bread: ")

                #Checks to see if the object is an instance of the breadWithStuffing class
                if isinstance(bread_object,breads.breadWithStuffing) == True:
                    bread_object.set_stuffing(new_stuffing)
                    print("The stuffing has been updated!")
                    print()

                #If the object isn't part of the breadWithStuffing class
                else:
                    print("This bread does not have a stuffing!")
                    print()

        #Decision structure if choice c is chosen
        elif choice == 'c':
            #Calls the retrive bread function
            bread_object = retrieveBread(list1)
            #Checks to see if the object exists and stores it in bread_objecy
            if bread_object != -1:
                new_inventory = int(input('Please enter the new inventory for this bread: '))

                #Checks to see if the new inventory is between 0 and 100
                if new_inventory < 0 or new_inventory > 100:
                    print('The inventory should be between 0 and 100')
                    print()

                #If the new inventory is between 0 and 100
                else:
                    bread_object.set_inventory(new_inventory)
                    print()

        #Decision structure if choice D is chosen
        else:
            print("Bread Report")
            print("============")
            #Iterates through the list of objects and calls the __str__ function
            for item in list1:
                print(item)
                print()




                   


        #Prompts the user if they want to continue using the program
        start = input("Do you want to continue (yes or no)?")
        #Converts it to lowercase
        start = start.lower()
        print()
    

def displayMenu():
    #Prints out a choice menu
    print("Welcome to Mr.Bread's Gourmet Bread Shop")
    print("========================================")
    print("A - Set Price")
    print("B - Set Stuffing")
    print("C - Set Inventory")
    print("D - Print Report")

    #Prompts the user for their choice
    user_choice = input("Please enter your selection: ")
    #Converts the choice into lowercase
    user_choice = user_choice.lower()
    #Validation loop to check if the choice is either a,b,c,d
    while (user_choice != 'a' and user_choice !='b' and user_choice!='c' and user_choice !='d'):
            #Prompts the user to re-enter the choice
            user_choice = input("Invalid choice! Please re-enter your selection: ")
            user_choice = user_choice.lower()

    #Returns the user choice
    return user_choice

def retrieveBread(bread_list):
    #Creates a flag variable
    flag = 0

    #Prompts the user for their choice of bread
    user_bread_choice = input("Which type of bread: ")
    #Converts it to lowercase
    user_bread_choice = user_bread_choice.lower()

    #Loop that will go through the list of bread
    for item in bread_list:
        #Checks to see if the user input matches up with one of the breads in the lost
        if(item.get_bread_type() == user_bread_choice):
            #Prints that it has been found
            print("The bread has been found!")
            print()
            #Prints all the attributes of the object
            print(item)
            return item
            #Stops the loop
            break
        #sets the flag to -1
        else:
            flag = -1
    #IF the object does not exists returns these statements
    if flag == -1:
        print("The bread is not on the list!")
        print()
    return flag




main()