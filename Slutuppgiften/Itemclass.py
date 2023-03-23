#A class that describes an Item:
#   code - The items bar-code or in this case the id(int)
#   name - The name of the item (str)
#   price - The price of the item (int)
#   amount - How many of the item that is in store (int)
#   buying - How many of the item the user has 'scanned' (int)
#   totalPrice - The price of the product * buying (int)

class Item:
    """ Represents an item """
    def __init__(self, code, name, price, amount):
        """ Creates an item
        Arguments: self(Item), code(int), price(int) and amount(int) 
        Returns: nothing"""
        self.code = code
        self.name = name
        self.price = price
        self.amount = amount
        self.buying = 0
        self.totalPrice = self.price

    def getCode(self):
        """ Returns the attribute code
        Arguments: self(Item)
        Returns: self.code(int) """
        return self.code

    def getName(self):
        """ Returns the name attribute
        Arguments: self(Item)
        Returns: self.name(str) """
        return self.name

    def getPrice(self):
        """ Returns the price attribute
        Arguments: self(Item)
        Returns: self.price(int) """
        return self.price

    def getAmount(self):
        """ Returns the amount attribute
        Arguments: self(Item)
        Returns: self.amount(int) """
        return self.amount
    
    def getBuying(self):
        """ Returns the buying attribute
        Arguments: self(Item)
        Returns: self.buying(int) """
        return self.buying

    def getTotalPrice(self):
        """ Returns the attribute totalPrice
        Arguments: self(Item)
        Returns: self.totalPrice(int) """
        return self.totalPrice

    def setName(self, name):
        """ Setter for name
        Arguments: self(Item) and name(str)
        Returns: nothing """
        self.name = name

    def __str__(self):
        """ Returns a string reprentation of the item
        Arguments: self(Item)
        Returns: str """
        return f"{self.code:<10} {self.name:<20} {self.amount:>10} \n"

    def __gt__(self, other):
        """ Compares which code value is greater between self and other.
        Arguments: self(Item) and other(Item)
        Returns: True or False (boolean)"""
        if self.code > other.getCode():
            return True

        return False
    
    def buy(self, amount):
        """ Changes the buying attribute depending on the argument amount
        Arguments: self(Item) and amount(int)
        Returns: self.buying(int) """
        self.amount -= amount
        self.buying += amount
        self.updateTotal()

        return self.buying
    
    def updateTotal(self):
        """ Updates the atribute totalPrice
        Arguments: self(Item)
        Returns: nothing """
        self.totalPrice = self.price * self.buying
