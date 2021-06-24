class BankAccount:
    nextId = 10000

    def __init__(self, name="Domyślny Użytkownik", balance=600):
        """Constructor
        """
        print("Użytkownik zainicjalizowany")
        self.name = name
        self.balance = balance
        self.id = BankAccount.nextId
        BankAccount.nextId += 1

    def addMoneyToBalance(self, amount):
        self.balance += amount
        print("Wpłacono: " + str(amount) + "zł")
        print("Na koncie jest teraz: " + str(self.balance) + "zł")

    def tryDeductMoneyFromBalance(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return {"isSuccess": True, "Message1": "Wypłacono: " + str(amount) + "zł", "Message2": "Pozostało: " + str(self.balance) + "zł"}
        else:
            return {"isSuccess": False, "Message": "Za mało pieniędzy na koncie"}

    def checkAccountBalance(self):
        print("Stan konta to: " + str(self.balance) + "zł")

    def __str__(self):
        return "Początkowy stan konta to: " + str(self.balance) + "zł"
