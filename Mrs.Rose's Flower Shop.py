A# Name: Jerry Che
# Assignment Number: 2
# Date: 2/5/18
# Section: 3:30-5:00
# Description: A program for Mrs. Rose's flower shop where it displays the menu then ask the customer for hwo much red and yellow they want. Then it goes through and ask if they 
# 			   want to make another transaction. Finally, it asks whether they want to run the program all over again.

def main ():
	#Constant variables for rose prices
	RED_ROSE_PRICE = 2.00
	YELLOW_ROSE_PRICE = 1.50

	#Constant variables for rates
	DISCOUNT_RATE = 0.05
	TAX_RATE = 0.075

	#Sets the variable program to Y so the first outer loop will run
	program = 'Y'

	#Checks to see if the variable program is set to yes
	while (program =="Y" or program == 'y'):
		#Sets the transaction to yes so the next loop will execute
		transaction = 'Y'

		#Intiatlizes variables that will be used to keep track of the toal flowers
		total_red = 0
		total_yellow = 0
		#Intiatlizes variables that will keep track of total sales for each flower
		total_sales_price_red = 0
		total_sales_price_yellow = 0
		#Intitalizes a variable to keep track of the total sales before tax
		total_sales = 0
		#Intitalizes a variable to keep track of tax,discount,and the final amount
		tax_amount = 0
		discount_amount = 0
		final_amount = 0

		#The start of loop 2 that checks to see if a customer wants to do another transaction
		while (transaction == 'Y' or transaction == 'y'):

			#Prints the menu for Mrs.Rose's flower shop
			print('''Welcome to Mrs.Rose's Flower Shop
*********************************
Menu:
Red rose - $2.00 per stem
Yellow rose - $	1.50 per stem''')

			#Prints a blank line
			print()

			#Asks the user for the rose type
			flower = input("Please select the rose type:")

			#Prints a blank line
			print()

			#A loop that will continue asking the user for rose type until the input the correct parameters
			while(flower != 'R' and flower != 'r' and flower !="Y" and flower != "y"):
			#Prints an error statement if the rose type is invalid
				print("You have entered an invalid type. Please try again!")
				#Prompts the user to enter another rose type
				flower = input("Please select the rose type:")
				#Prints a blank line
				print()

			#Decision structure for user who want red roses
			if (flower == 'r' or flower == 'R'):
				#Prompts the user for how many red roses they want
				quantity_red = int(input("How many roses would you like?"))
				#If the number is negative it prints an error statement and ask for the user for another answer
				if (quantity_red < 0):
					print("Invalid number")
					print()
					quantity_red = int(input("How many roses would you like?"))
				#If the number is valid it calculates the transaction amount and adds it to the correct variables
				else:
					transaction_red = quantity_red * RED_ROSE_PRICE
					total_sales_price_red = total_sales_price_red + transaction_red
					total_red = total_red + quantity_red
					#Prints the number of roses and price for the single transaction 
					print("You have selected ",quantity_red," "," red roses. The price is $", format(transaction_red,".2f"),sep='')
					#Prints a blank line
					print()


			else:
				#Prompts the user for how many yellow roses they want
				quantity_yellow = int(input("How many roses would you like?"))
				#If the quantity is negative it displays an error message and prompts the user again
				if (quantity_yellow < 0):
					print("Invalid number")
					quantity_yellow = int(input("How many roses would you like?"))				

				#If the quantity is valid then it calculates the transaction totals and adds it to the right variable
				else:
					transaction_yellow = quantity_yellow * YELLOW_ROSE_PRICE
					total_sales_price_yellow = total_sales_price_yellow + transaction_yellow
					total_yellow = total_yellow + quantity_yellow

					#Prints a statement with how many roses and the transaction amount
					print("You have selected ",quantity_yellow," yellow roses. The price is $", format(transaction_yellow,".2f"),sep ='')
					#Prints blank line
					print()

		
			#Prompts the user if they want to complete another transaction
			transaction = input("Do you want to make another purhcase?(Y or y for yes):")
			print()

		#Calculates the total sales of ALL the transactions
		total_sales = total_sales_price_yellow + total_sales_price_red

		#Begins to print out the transaction reports
		print()
		print("Transaction Report")
		print("******************")
		print("You have purchased",total_red,"red rose(s)")
		print("The price for red roses is $",format(total_sales_price_red,".2f"),sep = '')
		print("You have purchased",total_yellow,"yellow rose(s)")
		print("The price for red roses is $",format(total_sales_price_yellow,".2f"),sep = '')
		print("The total amount of sales before the discount is $",format(total_sales,".2f"),sep='')

		#Determines if the customer deserves a discount and then calculates everything else
		if(total_sales > 20 ):
			#Calculates the discount amount
			discount_amount = total_sales * DISCOUNT_RATE
			print("The discount amount is $",format(discount_amount,".2f"),sep = '')
		else:
			#Prints out a statement if the sales don't exceed 20
			print("The sales is less than $20.00, no discount is given")

		#Calculates the tax amount and the final transaction amount
		tax_amount = (total_sales - discount_amount) * TAX_RATE 
		final_amount = (total_sales - discount_amount) + tax_amount

		#Prints out the tax and the final amount
		print("The tax amount is $",format(tax_amount,".2f"),sep ='')
		print("The final total of the sales plus tax is $",format(final_amount,".2f"),sep='')

		#Prints a blank line
		print()

		#Prompts the user and asks if they want to run the program again
		program = input("Do you want to run the program again?")
		#Prints a blank line
		print()
main()
