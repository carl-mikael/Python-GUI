#Titel: Varuprisdatabas
#Uppgifts nr.: 145
#Författare: Carl-Mikael Bergbom
#Kurskod: DD100NHT211
#Datum: 2022-01-14
#
#The program pepresents a scanner where the bar-code is an id instead.
#The items that can be 'scanned' is stored in a seperate txt-file.
#When the user is done scanning the items is shown on a receipt.

from ItemManager import ItemManager
from GUIClass import GUI

def program():
    """ Starts the program by creating instances of the different classes.
    Starts the graphical user interface by calling the method mainloop
    Arguments: None
    Returns: nothiing"""
    FILENAME = "DataBase.txt"
    itemMngr = ItemManager(FILENAME)
    window = GUI(itemMngr)
    window.mainloop()


if __name__ == "__main__":
    program()
