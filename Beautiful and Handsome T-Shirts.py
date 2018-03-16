# Name: Jerry Che
# Assignment Number: 4
# Date: 2/23/18
# Section: 3:30-5:00
# Description: A program for Beautiful and Handosme T-shirts that will aks the customer
#			   for the type of shirt they want and comput the total cost

def main():
	#Constant for t-shirt prices
	RED_PRICE = 8.00
	YELLOW_PRICE = 8.00
	BLUE_PRICE = 18.00

	#Constant for max number of t-shirts
	MAX_RED = 8
	MAX_YELLOW = 8
	MAX_BLUE = 19

	#Constant for tax and donation rate
	TAX_RATE = 0.0725
	DONATION = 0.01

	#Accumulators for total amounts of each t-shirt
	total_red = 0
	total_blue = 0
	total_yellow = 0

	#Accumulators for total cost of each t-shirt
	total_red_cost = 0
	total_yellow_cost = 0
	total_blue_cost = 0

	#Variables to keep track of the total order cost and total t-shirts
	total_order_cost = 0
	total_shirts = 0

	#Variable to keep track of donation amount
	donation = 0

	#Variable to start the loop
	continue_order = 'Y'

	while(continue_order == 'Y' or continue_order == 'y'):
		#Local variable intialization 
		t_shirt_choice = ''
		t_shirt_quantity = 0

		#Calls the method dispLayMenu
		displayMenu()

		#sets local variable to the value returned by the method getCustomerChoice
		t_shirt_choice = getCustomerChoice()

		#Decision making structure based on t-shirt choice selection
		if (t_shirt_choice == 'A' or t_shirt_choice == 'a'):
			#Sets the local variable to value returned by the method getTshirtNumber
			t_shirt_quantity = getTshirtNumber(MAX_RED)

			#Accumulates the quantity and cost in correct variables
			total_red += t_shirt_quantity
			total_red_cost += calculateCharge(RED_PRICE,t_shirt_quantity,TAX_RATE)

		elif (t_shirt_choice == 'C' or t_shirt_choice == 'c'):
			#Sets the local variable to value returned by the method getTshirtNumber
			t_shirt_quantity = getTshirtNumber(MAX_YELLOW)

			#Accumulates the quantity and cost in correct variables
			total_yellow += t_shirt_quantity
			total_yellow_cost += calculateCharge(YELLOW_PRICE,t_shirt_quantity,TAX_RATE)
		else:
			#Sets the local variable to value returned by the method getTshirtNumber
			t_shirt_quantity = getTshirtNumber(MAX_BLUE)

			#Accumulates the quantity and cost in correct variables
			total_blue += t_shirt_quantity
			total_blue_cost += calculateCharge(BLUE_PRICE,t_shirt_quantity,TAX_RATE)

		#Adds up the total amount of shirts
		total_shirts = total_red + total_yellow + total_blue

		#Calls the method buyMore and passes in total_shirts as the parameter
		buyMore(total_shirts)

		#Asks the user if he or she wants to make another transaction
		continue_order = input("Do you want to continue shopping? (y of Y for yes)")
		print()

	#Prints out the sales report
	print("T-shirt Sales Report:")
	print("*********************************")
	print("*********************************")
	print(format(total_red,"4d"),"red T-shirt(s)     :$",format(total_red_cost,"6.2f"))
	print(format(total_blue,"4d"),"blue T-shirt(s)    :$",format(total_blue_cost,"6.2f"))
	print(format(total_yellow,"4d"),"yellow T-shirt(s)  :$",format(total_yellow_cost,"6.2f"))
	
	#Calculates the total cost
	total_order_cost = total_red_cost + total_yellow_cost + total_blue_cost

	print(format(total_shirts,"4d"),"total T-shirts     :$",format(total_order_cost,"6.2f"))
	print()

	#Calcuates the donation amount
	donation_amount = ((total_red * RED_PRICE) + (total_yellow * YELLOW_PRICE)+ (total_blue * BLUE_PRICE)) * DONATION
	print("Thank you for your purchase! We will donate $",format(donation_amount,".2f"),"to United Way")

	#Prints out the following statement if they ordered more than 3 shirts
	if (total_shirts >=3):
		print("You will also receive a free green T-shirt!")



#Method to displat the menu
def displayMenu():
	print('''Welcome to B&H T-shirt Store
****************************
****************************
(A) - Red T-shirt ($8.00)
(B) - Blue T-shirt ($18.00)
(C) - Yellow T-shirt ($8.00)''')

#Method to get the customer's choice of t-shirts
def getCustomerChoice():

	#Prints a blank line
	print()

	#Prompts the user to select a choice
	t_shirt = input("Please select a choice:")

	#Validation loop to see if the customer's choice is valid
	while (t_shirt!='A' and t_shirt!='a' and t_shirt!='b' and t_shirt!='B' and t_shirt!='C' and t_shirt!='c'):
		t_shirt = input("Invalid choice!Please select again:")

	#Returns the customer's choice
	return t_shirt

#Method to get the quantity of t-shirts with the parameter max_shirts
def getTshirtNumber(max_shirts):

	#Prompts the user for how many t-shirts they want
	quantity = int(input("How many t-shirts do you want?"))

	#Validation loop to check if the quantity falls out of range
	while (quantity > max_shirts or quantity < 0):
		print()

		#Prints this statement if it does fall out of range
		print("Invalid Number!")

		#Prints out the following statement if the quantity is over the max amount
		if(quantity > max_shirts):
			print(" The maximum number you can buy at one time is",max_shirts)
			print()
			quantity = int(input("How many t-shirts do you want?"))

		#Prints out the following statement if thhe quantity is negative
		else:
			print(" You have to enter zero or a positive number!")
			print()
			quantity = int(input("How many t-shirts do you want?"))

	#Returns a valid number for qunatity
	return quantity

#Method to calculate the total charge of one transaction
def calculateCharge(shirt_price,t_shirt_num,tax):

	#Calcualtes the pre-tax price
	total_cost_pretax = shirt_price * t_shirt_num

	#Calculates the post-tax price
	total_cost = total_cost_pretax * (1 + tax)

	#Returns the post-tax price
	return total_cost
	
#Method to print out statements regarding their total amount of t-shirts
def buyMore(total_shirt_quantity):

	#Prints a statement with the total amount of t-shirts they have purchased
	print("You have purchased a total of",total_shirt_quantity,"T-shirt(s)")

	#Prints out the following statements if the t-shirt quantity is between 1 and 3
	if (total_shirt_quantity >= 1 and total_shirt_quantity < 3):
		#Calculates the number of shirts needed to get a free one
		difference = 3 - total_shirt_quantity
		print("If you buy",difference,"more shirt(s), you will qualify for a free Green T-shirt")
		print()

	#Prints out the following statement if the customer has already purchased 3 or mroe shirts
	else:
		print("Yay, you will receive a free Green t-shirt!")
		print()




main()

