# Name: Jerry Che
# Assignment Number: 5
# Date: 2/28/18
# Section: 3:30-5:00
# Description: This program helps Mr.Pizza run his business. They are two options: printing and updating.
#			   Printing allows Mr.Pizza to print out a business report and calculates profit per pizza.
#			   Updating allows Mr. Pizza to write his business report into another file specifying how many records he wants.			   

def main():

	#Intializes a variable that will start the loop and keep prompting if they want to continue the program
	run_program = 'Y'

	#Starts the loop 
	while (run_program == 'Y' or run_program == 'y'):
		#Starts the program by printing out the two options
		print('''Welcome to the file program
-----------------------------------------
-----------------------------------------
P/p - Print Report
U/u - Update file''')
		#Calls the getChoice function and stores it into a local variable
		task_choice = getChoice()

		#Enters these statements if p or P was selected
		if (task_choice == 'P' or task_choice =='p'):
			#Enters an exception loop 
			try:
				#Calls the openFile function and sets it to a local variable
				in_file = openFile()
				#Passes the local variable into the printReport function
				printReport(in_file)

			#If an error occurs it prints out the following system
			except Exception as err:
				print("Exception handling section,system message:",err)
	
		#Enters these statements if U or u were selected
		elif(task_choice == 'U' or task_choice == 'u'):
			#Enters an exception decision structure
			try:
				#Prints a statement asking for an input file
				print("Open input file:")
				#Calls the openFile function and sets it to local variable old_file
				old_file = openFile()
				#Prints a statement asking for an output file
				print("Open output file:")
				#Calls the openFile function and sets it to local variable new_file
				new_file = openFile()
				#Calls the updateFile function and passes in old_file and new_file as parameters
				updateFile(old_file,new_file)
			#If an error occurs it prints out the following system
			except Exception as err:
				print("Exception handling section,system message:",err)

		#If neither p or u and P and U were selected it prints out an error message
		else:
			print("Invalid choice!")

		#Prompts the user asking if they want to run another program
		run_program = input("Do you want to run the program again?")
		print()

#method named getChoice
def getChoice():
	print()
	#Prompts the user for a choice 
	choice = input("Please enter your choice:")

	#returns the variable choice
	return choice

#Method named openFile
def openFile():

	#Prompts the user for file name and file_mode
	file_name = input("What is the name of the file?")
	file_mode = input("Please enter file mode:")

	#Pases in file_name and file_mode and creates a file_object
	file_object = open(file_name,file_mode)
	
	#Returns the file object
	return file_object

#Method named printReport
def printReport(file_name):
	#Creates a method variable named pizza_file and sets it to the argument file_name
	pizza_file = file_name

	#Intializes taccumulators for amount of pizzas and total_profit
	number_of_pizzas = 0
	total_profit = 0

	print()
	#Takes the first line of the file and sets it to pizza_name
	pizza_name = pizza_file.readline().rstrip("\n")

	#Creates a conditional loop that will end when pizza_name is empty
	while pizza_name != '':
		#Cast the next two lines as a float into pizza_price and pizza_cost
		pizza_price = float(pizza_file.readline())
		pizza_cost = float(pizza_file.readline())

		#Calculates the profit from each pizza and adds the appropiate amounts into accumulators
		pizza_profit = pizza_price - pizza_cost
		number_of_pizzas +=1
		total_profit+= pizza_profit

		#Prints out each line of the report
		print("Pizza: ",pizza_name)
		print("Price: $",pizza_price,sep='')
		print("Cost: $",pizza_cost,sep='')
		print("Profit: $",format(pizza_profit,".2f"),sep='')
		print()

		#Sets pizza_name to the next name so it doesn't interfere with the loop
		pizza_name = pizza_file.readline().rstrip("\n")

	#Closes pizza_file
	pizza_file.close()

	#Prints the ending statement and the number of pizza processed
	print("End of the file!")
	print("A total of",number_of_pizzas,"have been processed")

	#Calcualtes average profit and prints it into a statement
	average_profit = total_profit / number_of_pizzas
	print("The average profit is $",format(average_profit,".2f"),sep='')


	
#Method that updates files and uses the parameters old_file and new_file
def updateFile(old_file,new_file):
	#Prompts the user for the number of files they want to update
	number_of_records = int(input("How many records?"))

	#Stores arguments into local variables of input_file and output_file
	input_file = old_file
	output_file = new_file

	#Conditional loop that will stop when all records have been printed
	while (number_of_records != 0):
		#Takes the first three lines and stores them into the correct variable
		pizza_name = input_file.readline().rstrip("\n")
		pizza_price = input_file.readline().rstrip("\n")
		pizza_cost = input_file.readline().rstrip("\n")

		#Cast price and cost into a float in order to calculate profit
		float_pizza_price = float(pizza_price)
		float_pizza_cost = float(pizza_cost)

		#Calculates the profit
		pizza_profit = float_pizza_price - float_pizza_cost
		#Casts profit as a string
		string_pizza_profit = str(pizza_profit)

		#Writes the correct variable into the new file
		output_file.write(pizza_name + "\n")
		output_file.write(pizza_price + "\n")
		output_file.write(pizza_cost + "\n")
		output_file.write(string_pizza_profit + "\n")



		#decreases the number_of_records so they loop will stop when necessary
		number_of_records -=1

	#Closes both the input file and output file
	input_file.close()
	output_file.close()


main()