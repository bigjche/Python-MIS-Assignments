# Name: Jerry Che
# Assignment Number: 1
# Date: 1/31/18
# Section: 3:30-5:00
#Description: This program displays a menu for Delicious Cookies and asks the customer how many cookies and toppings they want then displays a busiess rpeort with all the cost


def main():

	#Constant price of cookies and toppings 

	VANILLA_PRICE = 1.20
	CHOCOLATE_PRICE = 1.30
	SC_PRICE = 0.50
	CC_PRICE = 0.20
	CA_PRICE = 0.40

	#Constant tax rate
	TAX_RATE = 1.0725

	#Constant rate of profit
	PROFIT_PERCENTAGE = 0.30

	#Constant start inventory at the beginning of the day
	VANILLA_STARTINVENTORY = 70
	CHOCOLATE_STARTINVENTORY = 70
	SC_STARTINVENTORY = 60
	CC_STARTINVENTORY = 50
	CA_STARTINVENTORY = 40

	#Prints the menu for the company
	print('''Welcome to Delcious Cookies
****************************
Types of Cookies:
Vanilla - $1.20
Chocolate - $1.30

Toppings:
1 scoop of strawberry cream - $0.50
1 ounce of choclate chips - $0.20
1 ounce of crushed almonds - $0.40
''')
	#Asks the customer how much of each thing she wants
	vanilla_cookie = int(input("How many vanilla cookies do you want?"))
	chocolate_cookie = int(input("How many chocolate cookies do you want?"))
	sc_topping = int(input("How many scoops of strawberry cream do you want?"))
	cc_topping = int(input("How many ounces of chocolate chip do you want?"))
	ca_topping = int(input("How many ounces of crushed almonds do you want?"))

	#Calcualtes the cost of each item that the customer wants
	vanilla_cost = vanilla_cookie * VANILLA_PRICE
	chocolate_cost = chocolate_cookie * CHOCOLATE_PRICE
	sc_cost = sc_topping * SC_PRICE
	cc_cost = cc_topping * CC_PRICE
	ca_cost = ca_topping * CA_PRICE

	#The cost of the total order before tax
	nontax_cost = vanilla_cost + chocolate_cost + sc_cost + cc_cost + ca_cost

	#The total cost after tax is added in
	total_cost = round((nontax_cost * TAX_RATE),2)

	#The toatl profit from the order 
	profit = nontax_cost * PROFIT_PERCENTAGE

	#The inventory of each item after the order is placed
	vanilla_endInventory = VANILLA_STARTINVENTORY  - vanilla_cookie
	chocolate_endInventory = CHOCOLATE_STARTINVENTORY  - chocolate_cookie
	sc_endInventory = SC_STARTINVENTORY  - sc_topping
	cc_endInventory = CC_STARTINVENTORY - cc_topping
	ca_endInventory = CA_STARTINVENTORY - ca_topping

	#Prints the introduction for the report
	print()
	print("Delcious Cookie Business Report")
	print("*******************************")

	#Prints the price and number of each item 
	print('The cost of',vanilla_cookie,'vanilla cookie(s) is',format(vanilla_cost,'.2f'))
	print('The cost of',chocolate_cookie,'chocolate cookie(s) is',format(chocolate_cost,'.2f'))
	print('The cost of',sc_topping,'scoop(s) of strawberry cream is',format(sc_cost,'.2f'))
	print('The cost of',cc_topping,'ounce(s) of chocolate chip is',format(cc_cost,'.2f'))
	print('The cost of',ca_topping,'ounce(s) of crushed almonds is',format(ca_cost,'.2f'))
	print('The total cost is',format(total_cost,'.2f'))
	print("The total profit for this order is",format(profit,'.2f'))

	#Prints the ending inventory after the order
	print("The remaining vanilla cookies in inventory is",vanilla_endInventory)
	print("The remaining chocolate cookies in inventory is",chocolate_endInventory)
	print("The remaining ounces of strawberry cream in inventory is",sc_endInventory)
	print("The remaining ounces of chocolate chip in inventory is",cc_endInventory)
	print("The remaining ounces of crushed almonds in inventory is",ca_endInventory)


main()
	



