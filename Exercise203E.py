from Exercise203S import BankAccount

accounts = [BankAccount() for _ in range(10)]

print(accounts[0])
accounts[0].deductMoneyFromBalance(200)
accounts[0].addMoneyToBalance(2205)
accounts[0].checkAccountBalance()

""" for account in accounts:
    print(account.id)
    print(account.balance) """
