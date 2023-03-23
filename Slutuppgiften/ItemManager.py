from Itemclass import Item

#A class that takes care of the data structure:
#   items - The items that the user can 'scan' in a dict (dict)
#   scannedItems - Represents the shopping cart. A list of all the scanned items (list)
#   fileName - The file name where the items will be stored

class ItemManager:
    """ Takes care of the data structor for the items """
    def __init__(self, fileName):
        """ Creates an ItemManager-object
        Arguments: self(ItemManager) and fileName(str)
        Returns: nothing """
        self.fileName = fileName
        self.items = self.readFromDataBase()
        self.scannedItems = []

    def getItems(self):
        """ Returns the dict of items
        Arguments: self(ItemManager)
        Returns: items(dict) """
        return self.items

    def getScannedItems(self):
        """ Returns the list scannedItems
        Arguments: self(ItemManager)
        Returns: scannedItems(list) """
        return self.scannedItems

    def setItems(self, items):
        """ Sets the items dict to the argument items
        Arguments: self(ItemManager) and items(dict)
        Returns: nothing """
        self.items = items
    
    def setScannedItems(self, scannedItems):
        """ Sets the scannedItems list to the argument scannedItems
        Arguments: self(ItemManager) and scannedItems(list)
        Returns: nothing"""
        self.scannedItems = scannedItems

    def buy(self, amount, window, item):
        """ Changes the buying atribute of the item argument, depending on the amount argument.
        Updates the scannedItems atribute.
        Updates the GUI
        Arguments: self(Item), amount(int), window(GUI) and item(Item)
        Returns: nothing"""
        itemBuying = item.getBuying()
        itemAmount = item.getAmount()

        # if itemAmount < 1:
        #     if itemBuying < abs(itemAmount):              //Useless code prob
        #         window.updateTree()
        #         return

        if itemAmount >= amount:
            itemBuying = item.buy(amount)
            if itemBuying == 0:
                self.scannedItems.remove(item)
            window.updateTree()
        else:
            window.updateTree()
            item.updateTotal()

    def getStrOfItems(self):
        """ Returns a string of the items
        Arguments: self(ItemManager)
        Returns: itemsStr(str) """
        itemsStr = f"{'ID':<10} {'ITEM':<20} {'STOCK':>10}\n"
        for item in self.items:
            itemsStr += self.items[item].__str__()
        
        return itemsStr

    def makeReceiptDict(self):
        """ Creates a dict from the scanned items to represent three rows: name, amount and price
        Arguments: self(GUI)
        Returns: receipt(dict), total(int) and receiptLenght(int)"""
        scannedItems = self.getScannedItems()
        receipt = {
            "name": [],
            "amount": [],
            "price": [],
        }

        total = 0
        receiptLenght = 0
        for item in scannedItems:
            itemBuying = item.getBuying()
            itemName = item.getName()
            itemTotalPrice = item.getTotalPrice()
            receipt["amount"].append(str(itemBuying) + "x ")
            receipt["name"].append(itemName)
            receipt["price"].append("{:.2f}".format(itemTotalPrice))
            receiptLenght += 1
            total += itemTotalPrice

        return receipt, total, receiptLenght

    def readFromDataBase(self):
        """ Creates Item-objects from the file and saves them in a dict.
        The number count is the key in the items(dict) and the value for the Item-instance atribute code.
        The items dict saves Items like this; code(lineCount): Item
        Arguments: self(ItemManager)
        Returns: items(dict)"""
        items = {}
        with open(self.fileName, "r", encoding="utf8") as file:
            lineCount = 0
            for line in file:
                lineCount += 1
                name, price, amount = line.replace("\n", "").split(" ")
                name = name.replace("_", " ")
                items[lineCount] = Item(lineCount, name, int(price), int(amount))

            return items

    def writeToDataBase(self):
        """ Saves all the Items in items in the file fileName like this:
        "itemName itemPrice itemAmount" 
        Arguments: self(ItemManager)
        Returns: nothing"""
        with open(self.fileName, "w", encoding="utf8") as file:
            for item in self.items.values():
                itemName = item.getName()
                itemPrice = item.getPrice()
                itemAmount = item.getAmount()
                item.setName(itemName.replace(" ", "_"))
                itemName = item.getName()
                itemAttributes = itemName + " " + str(itemPrice) + " " + str(itemAmount) + "\n"
                file.writelines(itemAttributes)
