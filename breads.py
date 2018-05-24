class Breads:
    #Intialization method to create the bread object
    def __init__(self, price, bread_type, inventory):
        self.__price = price
        self.__bread_type = bread_type
        self.__inventory = inventory

    #Changes the object price
    def set_price(self, new_price):
        self.__price = new_price

    #Returns the object's price
    def get_price(self):
        return self.__price

    #Sets a new bread type
    def set_bread_type(self, new_bread_type):
        self.__bread_type = new_bread_type

    #Returns the object's bread type
    def get_bread_type(self):
        return self.__bread_type

    #Sets a new inventory for the object
    def set_inventory(self, new_inventory):
        self.__inventory = new_inventory

    #Return the inventory for the object
    def get_inventory(self):
        return self.__inventory

    #A print statement
    def __str__(self):
        return "Price is " + str(self.__price) + "\n" + "Bread type is " + self.__bread_type + "\n" + "Inventory is " + str(self.__inventory) + '\n'


class breadWithStuffing(Breads):

    #Intialization method that inherits it from the bread class
    def __init__(self,price,bread_type,inventory,stuffing):
        Breads.__init__(self,price,bread_type,inventory)
        self.__stuffing = stuffing

    #Return the object's stuffing
    def get_stuffing(self):
        return self.__stuffing

    #Sets a new stuffing for an object
    def set_stuffing(self,new_stuffing):
        self.__stuffing = new_stuffing
        
    #A print statement for the object
    def __str__(self):
        return Breads.__str__(self) + "Stuffing is " + self.__stuffing 


    
