# Name: Jerry Che
# Assignment Number: 2
# Date: 2/5/18
# Section: 3:30-5:00
# Description: This program creates and generates a business report for Gourmet foods. It takes in account whether the customer is a Premimum or Ordinary customers and caluclates
#              it based on their respective membership types. 




def main():
	#Constant price of the meals
	ORDINARY_MEALPRICE = 5.95
	PREMIUM_MEALPRICE = 5.20

	#Constant variable for Tax, membership fee, and flag variable
	TAX_RATE = 0.075
	MEMBERSHIP_FEE = 9
	FLAG_VARIABLE = 0

	# Prints a welcome statement
	print('''Welcome to Gourmet Foods!
*************************''')

	#Prompts the user for their name
	customer_name = input("Please enter your name:")

	#Prompts the user for their membership type
	membership = input("Please enter your membership type (O - ordinary P - premium):")

	#Intiatizes the variables that will store free_packages and price
	free_packages = 0
	price = 0

	#Starts the decision structure and if you are an ordinary customer you enter these statements
	if(membership == 'O' or membership == 'o'):
		#Prompts the user for the number of packages they wanty
		packages = int(input("How many packages do you want?"))

		#Sets price to the constant variable for ordinary member pricing
		price = ORDINARY_MEALPRICE

		#Goes through the decision strucure to decide how many free packages a ordinary customer will receive
		if(packages < 6):
			free_packages = 0
		elif(packages >=6 and packages <= 12):
			free_packages = 1
			
		elif(packages > 12 and packages <= 200):
			free_packages = 2

		#If it doesn't fall within the above ranges the flag is set to 99 and an error statement displays
		else:
			FLAG_VARIABLE = 99
			print("You can't order more than 200 packages. No transaction will be recorded")


	#Second part of decision structure and is for premium customers
	elif(membership == 'P' or membership == 'p'):

		#Prompts the user for how many packages they want
		packages = int(input("How many packages do you want to order?"))

		#sets the price to the constant variable that contains the premium meal pricing
		price = PREMIUM_MEALPRICE

		#Goes through decision structure to decide how many free packages a premium customer will receive
		if(packages < 4):
			free_packages = 0
		elif(packages >=4 and packages <= 8):
			free_packages = 1
			
		elif(packages > 8 and packages <=200):
			free_packages = 2

		#if the user enters anything up 200 the flag variable gets set to 200 and an error statement is displayed
		else:
			FLAG_VARIABLE = 99
			print("You can't order more than 200 packages. No transaction will be recorded")
			
	#if the customer enters anything besides o,O,p,or P the flag will be set to 99 and an error will display
	else:
		FLAG_VARIABLE = 99
		print("You have entered an incorrect membership type! No transaction will be conducted.")




	#Intializes the variables for sales price, the sales tax, and the total cost
	sales_price = 0
	sales_tax = 0
	total_cost = 0

	#If there are no errors in the above code it will go through this code
	if(FLAG_VARIABLE == 0):

		#Calculates the variables
		sales_price = packages * price
		sales_tax = sales_price * TAX_RATE
		total_cost = sales_price + sales_tax

		#Nested loop to determine if you are an ordinary member
		if(membership == 'O' or membership == 'o'):

			#Prints the total cost before upgrading
			print("Your current charge is $",format(total_cost,".2f"),sep='')
			print("You can save more money if you upgrade your membership!")

			#asks the user if they want an upgrade
			upgrade = input("Would you like to upgrade? (Y for yes)")

			#if the customer wants the upgrade it recalcualtes the costs
			if(upgrade =='Y' or upgrade == 'y'):

				#sets the price to premium pricing
				price = PREMIUM_MEALPRICE

				#Recalculates all the previous costs
				sales_price = packages * price
				sales_tax = sales_price * TAX_RATE
				total_cost = sales_price + sales_tax

				#the total cost with membership fee included
				total_cost_with_fee = total_cost + MEMBERSHIP_FEE

				#Recalculates the amount of free packages based on a premium membership
				if(packages < 4):
					free_packages = 0
				elif(packages >=4 and packages <= 8):
					free_packages = 1
			
				elif(packages > 8 and packages <=200):
					free_packages = 2

				#Sets membership to premium
				membership = 'P'

			#Sets upgrade to No 
			else:
				upgrade = 'N'

		#Prints out the business report			
		print()
		print("Customer Receipt")
		print("****************")
		print("Customer name:", customer_name)
		print("Membership type:", membership)
		print("Total packages ordered:",packages)
		print("Total free packages:",free_packages)
		print("Total sales price: $",format(sales_price,".2f"),sep = '')
		print("Sales tax: $",format(sales_tax,".2f"),sep = '')

		#if the user is now a premium customer that upgraded it enters this set of statements
		if(membership == 'P' and upgrade =='Y'):
			print("New membership fee: $",format(MEMBERSHIP_FEE,".2F"),sep = '')
			print("Total amount due: $",format(total_cost_with_fee,".2f"),sep = '')

		#any other case it would just print out the total cost
		else:
			print("Total amount due: $",format(total_cost,".2f"),sep='')

main()
