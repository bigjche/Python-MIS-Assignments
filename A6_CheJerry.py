# Name: Jerry Che
# Assignment Number: 6
# Date: 3/21/18
# Section: 3:30-5:00
# Description: This program displays a text file with the two derived values of: profit and
#              and revenue. It demonstrates our knowledge on how to use lists

def main():
	#Intitalizes a global constant called NUMFIELD
	global NUMFIELD
	#Sets the variable NUMFIELD to 5
	NUMFIELD = 5
	#Intitalizes an empty list called twoDim
	twoDim = []
	#Intitalizes a variable called maxRow
	maxRow = 0

	#Starts a try and exception loop
	try:
		#Reads in a file called HW6_PROD.txr
		in_file = open('HW6_PROD.txt','r')

		#Reads in the first line of the text file
		product_id = in_file.readline().rstrip('\n')
		#Starts a while loop with a condition that will stop when the file is empty
		while (product_id != ""):
			#Intializes an empty list called prodList
			prodList = []
			#Reads in the next 4 variables and assigns it to the correct variable
			name = in_file.readline().rstrip('\n')
			price = float(in_file.readline().rstrip('\n'))
			profit_margin = float(in_file.readline().rstrip('\n'))
			quantity = int(in_file.readline().rstrip('\n'))
			#Appends all the variables into the list prodList
			prodList.append(product_id)
			prodList.append(name)
			prodList.append(price)
			prodList.append(profit_margin)
			prodList.append(quantity)

			#Appends the entire list to a 2-D array
			twoDim.append(prodList)
			maxRow +=1
			#Passes in the variable prodList into the prodReport function
			prodReport(prodList)
			#Retrives the next productid to go back through the loop
			product_id = in_file.readline().rstrip('\n')
		#Passes in the variable twoDim and maxRow into the function named printTwoDim
		printTwoDim(twoDim,maxRow)

	#Prints this statement if there is a problem above
	except Exception as err:
		print("Sorry something went wrong with your file")

#Function called prodReport
def prodReport(product_list):
	#A loop that will go through product_list and print all the contents
	for item in product_list:
		print(item)
	#Calculates revenue and profit_amount
	revenue = (product_list[4]) * (product_list[2])
	profit_amount = revenue * product_list[3]
	#Prints revenue and profit
	print("Revenue :$",format(revenue,".2f"),sep ='')
	print("Profit Amount: $",format(profit_amount,".2f"),sep = '')
	print()

#Function called printTwoDim
def printTwoDim(twoDimList, max_Rows):
	#For loop that will iterate over the max_Rows
	for row in range (max_Rows):
		#A nested loop that will 
		for column in range (NUMFIELD):
			#Prints the item in the two dimensional list
			print(twoDimList[row][column])
		print()

main()