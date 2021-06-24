from Exercise203S2 import Ok, Error


class BankAccount:
    nextId = 10000

    def __init__(self, name="Domyślny Użytkownik", balance=1500):
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
            return Ok("Wypłacono: " + str(amount) + "zł", "Pozostało: " + str(self.balance) + "zł")
        else:
            return Error("Za mało pieniędzy na koncie")

    def checkAccountBalance(self):
        print("Stan konta to: " + str(self.balance) + "zł")

    def __str__(self):
        return "Początkowy stan konta to: " + str(self.balance) + "zł"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=1500, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def tryDeductMoneyFromBalance(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().tryDeductMoneyFromBalance(amount)
        else:
            return Error("Próba wypłaty poniżej limitu konta")
