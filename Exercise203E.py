from Exercise203S1 import BankAccount, MinimumBalanceAccount

accounts = [MinimumBalanceAccount() for _ in range(10)]

print(accounts[0])
accounts[0].addMoneyToBalance(2205)
accounts[0].checkAccountBalance()

""" for account in accounts:
    print(account.id)
    print(account.balance) """
# print(result.isSuccess)
result = accounts[0].tryDeductMoneyFromBalance(600)

print(result.isOK())
print(result.message1)
print(result.message2)
