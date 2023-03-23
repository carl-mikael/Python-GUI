from tkinter import *
from tkinter import ttk

#A class that takes care of the graphical user interface

class GUI(Tk):
    """ Handles all the graphical user interface """
    def __init__(self, itemMngr, extraReceiptHeight = 0):
        """ Creates a GUI instance
        Arguments: self(GUI), itemMngr(ItemManager) and extraReceiptHeight(int, deafualt 0) 
        Returns: nothing"""
        super().__init__()
        self.itemMngr = itemMngr
        self.extraReceiptHeight = extraReceiptHeight
        self.initFirstFrame()
        self.initSecondFrame()

    def initFirstFrame(self):
        """ Calls the Initialization methods for frame one, also grids frame one
        Arguments: self(GUI)
        Returns: nothing """
        self.initFontAndColor()
        self.initWindow()
        self.initMenuBar()

        self.frameOne = Frame(self, bg=self.COLORONE)
        self.frameOne.grid()

        self.fillGrids(self.frameOne)
        self.initId()
        self.initAmount()
        self.initItem()
        self.initErrorMessage()
        self.initButtons()
        self.initTreeView()

    def initSecondFrame(self):
        """ Calls the Initialization methods for frame two, also grids frame two
        Arguments: self(GUI)
        Returns: nothing """
        self.frameTwo = Frame(self, bg=self.COLORONE)
        self.option_add("*Font", "Roboto 10")
        self.fillGrids(self.frameTwo)
        self.initReceipt()

    def initFontAndColor(self):
        """ Initializes the font and color
        Arguments: self(GUI)
        Returns: nothing """
        self.option_add("*Font", "Roboto 12")
        self.COLORONE = "lightgrey"
        self.COLORTWO = "grey"

    def initWindow(self):
        """ Initializes the window
        Arguments: self(GUI)
        Returns: nothing """
        self.resizable(width=False, height=False)
        self.winHeight = IntVar(value=370)
        self.resizeWindow("Scan Items")
    
    def initMenuBar(self):
        """ Initializes the menu bar
        Arguments: self(GUI)
        Returns: nothing """
        self.helpWinOpen = BooleanVar(value=False)
        self.itemWinOpen = BooleanVar(value=False)
        self.menuBar = Menu(self)
        self.menuBar.add_command(label="Help", command=self.showHelpWindow)
        self.menuBar.add_command(label="Items", command=self.showItemWindow)
        self.config(menu=self.menuBar)

    def initId(self):
        """ Initializes the id entry and label part of the gui
        Arguments: self(GUI)
        Returns: nothing """
        self.itemId = IntVar(value=0)
        valID = self.register(self.validateIdEntry)
        self.idLabel = Label(self.frameOne, text="ID", bg=self.COLORONE)
        self.idEntry = Entry(self.frameOne, width=3, borderwidth=0, highlightthickness=1, highlightbackground="black", validate="key", validatecommand=(valID, "%P"))
        self.idLabel.grid(row=2, column=2, sticky=W)
        self.idEntry.grid(row=3, column=2, sticky=W)

    def initAmount(self):
        """ Initializes the amount entry and label part of the gui
        Arguments: self(GUI)
        Returns: nothing """
        self.itemAmount = IntVar(value=0)
        valAmount = self.register(self.checkAmount)
        self.amountLabel = Label(self.frameOne, text="Qty", bg=self.COLORONE)
        self.amountEntry = Entry(self.frameOne, width=3, borderwidth=0, highlightthickness=1, highlightbackground="black", validate="key", validatecommand=(valAmount, "%P"))
        self.amountLabel.grid(row=2, column=3, sticky=W)
        self.amountEntry.grid(row=3, column=3, sticky=W)

    def initItem(self):
        """ Initializes the item label and entry part of the gui
        Arguments: self(GUI)
        Returns: nothing"""
        self.itemName = StringVar(value="")
        self.nameLabel = Label(self.frameOne, text="Item", bg=self.COLORONE)
        self.itemNameLabel = Label(self.frameOne, width=10, textvariable=self.itemName, anchor=W, bg="darkgrey", borderwidth=1, relief=SOLID)
        self.nameLabel.grid(row=2, column=4, ipadx=1, sticky=W)
        self.itemNameLabel.grid(row=3, column=4, sticky=W)

    def initErrorMessage(self):
        """ Initializes the error message part of the gui
        Arguments: self(GUI)
        Returns: nothing """
        self.idErrorMessage = StringVar(value="X")
        self.idErrorLabel = Label(self.frameOne, textvariable=self.idErrorMessage, bg=self.COLORONE, fg="red")
        self.idErrorLabel.grid(row=4, column=2)

        self.amountErrorMessage = StringVar(value="X")
        self.amountErrorLabel = Label(self.frameOne, textvariable=self.amountErrorMessage, bg=self.COLORONE, fg="red")
        self.amountErrorLabel.grid(row=4, column=3)

    def initButtons(self):
        """ Initializes the button part of the gui
        Arguments: self(GUI)
        Returns: nothing """
        self.option_add("*Button.Font", "Roboto 10")

        self.enterButton = Button(self.frameOne, text="Enter", command=self.addItem)
        self.enterButton.grid(row=3, column=5)

        self.printButton = Button(self.frameOne, text="Print", command=self.changeFrame)
        self.printButton.grid(row=6, column=7)

    def initTreeView(self):
        """ Initializes the Treeview part of the gui
        Arguments: self(GUI)
        Returns: nothing """
        font = ttk.Style().configure("Treeview", rowheight=15)
        self.treeTitle = Label(self.frameOne, text="Shopping cart", style=font, anchor=S, bg=self.COLORONE)
        self.treeTitle.grid(row=5, column=2, columnspan=4)

        self.tree = ttk.Treeview(self.frameOne, columns=(0, 1, 2, 3), show="headings", height=10, style=font)
        self.tree.column(0, anchor=W, width=31)
        self.tree.heading(0, text="ID       ")
        self.tree.column(1, anchor=W, width=31)
        self.tree.heading(1, text="Qty      ")
        self.tree.column(2, anchor=W, width=97)
        self.tree.heading(2, text="Item                    ")
        self.tree.column(3, anchor=W, width=44)
        self.tree.heading(3, text="Price    ")
        self.tree.grid(row=6, column=2, columnspan=4)

        self.scrollBar = ttk.Scrollbar(self.frameOne, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollBar.set)
        self.scrollBar.grid(row=6, column=6, sticky=NS)

    def initReceipt(self):
        """ Initializes the receipt part of the gui 
        Arguments: self(GUI)
        Returns: nohting"""
        self.receiptFrame = Frame(self.frameTwo, background=self.COLORONE, border=3, highlightthickness=3, highlightcolor=self.COLORTWO, highlightbackground=self.COLORTWO)
        self.receiptFrame.grid(row=1, rowspan=4, column=2, columnspan=4)
        Label(self.receiptFrame, width=1, height=1, bg=self.COLORONE).grid(row=0, column=0)
        Label(self.receiptFrame, width=1, height=1, bg=self.COLORONE).grid(row=4, column=4)

        self.receiptHeaderLabel = Label(self.receiptFrame, text="RECEIPT", font=(None, 18, "italic bold"), background=self.COLORONE)
        self.receiptHeaderLabel.grid(row=0, column=1, columnspan=3)

        self.receiptHeight = IntVar()
        self.receiptName = StringVar()
        self.receiptAmount = IntVar()
        self.receiptPrice = StringVar()
        self.receiptAmountBox = Listbox(self.receiptFrame, listvariable=self.receiptAmount, justify=RIGHT, width=5, height=self.receiptHeight.get(), border=0, highlightthickness=0, background=self.COLORONE)
        self.receiptNameBox = Listbox(self.receiptFrame, listvariable=self.receiptName, justify=LEFT, width=15, border=0, height=self.receiptHeight.get(), highlightthickness=0, background=self.COLORONE)
        self.receiptPriceBox = Listbox(self.receiptFrame, listvariable=self.receiptPrice, justify=RIGHT, width=10, border=0, height=self.receiptHeight.get(), highlightthickness=0, background=self.COLORONE)
        self.receiptAmountBox.grid(row=1, column=1)
        self.receiptNameBox.grid(row=1, column=2)
        self.receiptPriceBox.grid(row=1, column=3, sticky=NW)

        self.receiptTotal = StringVar()
        self.receiptTotalLabel = Label(self.receiptFrame, textvariable=self.receiptTotal, anchor=E, width=10, border=0, highlightthickness=0, background=self.COLORONE)
        self.receiptTotalLabel.grid(row=2, column=1, columnspan=3, sticky=EW)

    def makeReceipt(self):
        """ Shows the receipt
        Arguments: self(GUI)
        Returns: nothing """
        receipt, total, receiptLenght = self.itemMngr.makeReceiptDict()
        self.receiptHeight.set(receiptLenght)
        self.receiptTotal.set("\nTotal: {:>35.2f}".format(total))

        if self.receiptHeight.get() != 0:
            self.winHeight.set((self.receiptHeight.get() + 1) * 17 + 193 + self.extraReceiptHeight)
        else:
            self.winHeight.set(230 + self.extraReceiptHeight)

        self.receiptName.set(receipt["name"])
        self.receiptAmount.set(receipt["amount"])
        self.receiptPrice.set(receipt["price"])

    def fillGrids(self, frame):
        """ Makes 18 empty labels to make the gui look a bit nicer
        Arguments: self(GUI) and frame(Frame)
        Returns: nothing"""
        for i in range(9):
            Label(frame, width=2, height=1, bg=self.COLORONE).grid(row=0, column=i, sticky=NSEW)
            Label(frame, width=2, height=1, bg=self.COLORONE).grid(row=i, column=0, sticky=NSEW)

    def setNameAndID(self, inp, items):
        """ Sets the itemName, itemId and idErrorMessage variable classes depending on the inp argument.
        Arguments: self(GUI), inp(int) and items(dict)
        Returns: item(Item)"""
        item = items[inp]
        self.itemName.set(item.getName())
        self.amountErrorMessage.set("")
        self.idErrorMessage.set("")
        self.itemId.set(inp)

        return item

    def checkId(self, inp):
        """ Checks the id input. If the input is bad, an error message (a red X) will show under the Entry.
        Arguments: self(GUI) and inp(any)s
        Returns: nothing"""
        items = self.itemMngr.getItems()
        try:
            inp = int(inp)
            if inp in items.keys():
                item = self.setNameAndID(inp, items)
                if item.getAmount() == 0:
                    self.amountErrorMessage.set("X")
            else:
                self.amountErrorMessage.set("")
                self.idErrorMessage.set("X")
                self.itemName.set("")

        except ValueError:
            self.amountErrorMessage.set("")
            self.idErrorMessage.set("X")
            self.itemName.set("")

    def validateIdEntry(self, inp):
        """ Takes care of the id input. If it's accepted the method returns True.
        Arguments: self(GUI) and inp(any)
        Returns: True or False (boolean)"""
        self.itemId.set(0)
        if inp == "0":
            return False

        self.checkId(inp)
        self.amountEntry.delete(0, END)
        self.amountEntry.insert(0, 1)

        return True

    def validateAmountEntry(self, inp):
        """ Validates the amount input. If the input is bad, an error message (a red X) will show under the Entry.
        Arguments: self(GUI) and inp(any)
        Returns: nothing"""
        items = self.itemMngr.getItems()
        try:
            inp = int(inp)
            if self.itemId.get() != 0:
                if inp <= items[self.itemId.get()].getAmount() and inp > 0:
                    self.amountErrorMessage.set("")
                    self.itemAmount.set(inp)
                elif abs(inp) <= items[self.itemId.get()].getBuying() and inp < 0:
                    self.amountErrorMessage.set("")
                    self.itemAmount.set(inp)
                else:
                    self.itemAmount.set(0)
                    self.amountErrorMessage.set("X")

        except ValueError:
            self.itemAmount.set(0)
            self.amountErrorMessage.set("X")

    def checkAmount(self, inp):
        """ Validates the amount input. If accepted the method returns True.
        Arguments: self(GUI) and inp(any)
        Returns: True or False (boolean) """
        if inp == "0":
            return False

        self.validateAmountEntry(inp)

        return True

    def changeFrame(self):
        """ Removes frameOne(Frame) and shows frameTwo(Frame).
        Shows the receipt.
        Saves the items inside of the itemMngr-object to the file.
        Arguments: self(GUI)
        Returns: nothing"""
        self.frameOne.destroy()
        self.frameTwo.grid()
        self.makeReceipt()
        self.resizeWindow("Receipt")
        self.itemMngr.writeToDataBase()
  
    def resizeWindow(self, title):
        """ Rezizes the gui window size and sets the title to the title argument
        Arguments: self(GUI) and title(str)
        Returns: nothing """
        self.title(title)
        self.geometry("{}x{}".format(340, self.winHeight.get()))

    def updateTree(self):
        """ Shows the scannedItems in Treeview.
        Arguments: self(GUI)
        Returns: nothing"""
        scannedItems = self.itemMngr.getScannedItems()
        total = 0
        scannedItems.sort()
        self.tree.delete(*self.tree.get_children())
        for item in scannedItems:
            total += item.getTotalPrice()
            self.tree.insert("", "end", values=(str(item.getCode()), str(item.getBuying()), item.getName(), str(item.getTotalPrice())))

    def addItem(self):
        """ Takes the input from the user.
        Updates the scannedItems list.
        Arguments: self(GUI)
        Returns: nothing """
        items = self.itemMngr.getItems()
        scannedItems = self.itemMngr.getScannedItems()

        code = self.itemId.get()
        amount = self.itemAmount.get()
        code = int(code)
        amount = int(amount)
        if code != 0 and amount != 0:
            item = items[code]
            if item not in scannedItems:
                scannedItems.append(item)
            self.itemMngr.buy(amount, self, item)
            self.itemMngr.setScannedItems(scannedItems)
            self.amountEntry.delete(0, END)
            self.amountEntry.insert(0, 1)
            self.itemAmount.set(1)
            self.updateTree()

    def showHelpWindow(self):
        """ Shows a help window with instructions.
        Arguments: self(GUI)
        Returns: nothing """
        if not self.helpWinOpen.get():
            self.helpWinOpen.set(True)
            self.helpWindow = Toplevel(self)
            self.helpWindow.title("Help")
            self.helpWindow.geometry("{}x{}".format(530, 200))
            self.helpWindow.resizable(False, False)
            self.helpWindow.protocol("WM_DELETE_WINDOW", lambda: (self.helpWindow.destroy(), self.helpWinOpen.set(False)))
            self.helpWindow.grid()

            helpMessage = "\
            ID is row number in the database.\n\
            'Qty' for how many.\n\
            Use negative 'Qty' to remove that many items of that ID from your cart\n\
            'X' for error.\n\
            If the ID doesn't exist the program an 'X' will appear under ID\n\
            If the Qty is more than in stock an 'X' will appear under the Qty\n\
            If you try to remove more items than you have an 'X' will appear under Qty"
            helpMessageLabel = Label(self.helpWindow, text=helpMessage, justify=LEFT)
            helpMessageLabel.grid()

    def showItemWindow(self):
        """ Shows a window with all the items with their id, name and nr in stock
        Arguments: self(GUI)
        Returns: nothing """
        if not self.itemWinOpen.get():
            self.itemWinOpen.set(True)
            self.itemWindow = Toplevel(self)
            self.itemWindow.title("Items")
            self.itemWindow.geometry("{}x{}".format(530, 400))
            self.itemWindow.protocol("WM_DELETE_WINDOW", lambda: (self.itemWindow.destroy(), self.itemWinOpen.set(False)))
            self.itemWindow.grid()

            itemsStr = self.itemMngr.getStrOfItems()
            itemsStrLabel = Label(self.itemWindow, text=itemsStr, justify=LEFT)
            itemsStrLabel.grid()
