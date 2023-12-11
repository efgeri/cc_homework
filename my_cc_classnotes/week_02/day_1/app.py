from bank_account import *

# account = {
#     "holder_name": "John",
#     "balance": 500,
#     "type": "business",
# }

# print(get_account_name(account))

johns_bank_account = BankAccount('John', 500, 'business')
adas_bank_account = BankAccount("Ada", 100 ,"personal")

print(johns_bank_account.holder_name)

# johns_bank_account.pay_in(100)
# print(johns_bank_account.balance)

johns_bank_account.recurring_fee()
adas_bank_account.recurring_fee()

print(johns_bank_account.balance)
print(adas_bank_account.balance)