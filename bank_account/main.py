from account import Account

# Action 1: create two accounts
account_01: Account = Account(bank_branch='001', account_number='00001',
                              account_holder='Costumer One',
                              current_balance=5000,
                              investment_balance=10000, limit=20000)
account_02: Account = Account(bank_branch='001', account_number='00002',
                              account_holder='Costumer two',
                              current_balance=8000,
                              investment_balance=20000, limit=20000)

# Action 2: change the bank branch of account 02
account_02.bank_branch = '002'

# Action 3: change account 02 limit
account_02.limit = 30000

# Action 4: deposit $ 5000 into account 01
account_01.deposit(5000)

# Action 5: deposit $ 3000 into account 01
account_02.deposit(3000)

# Action 6: withdraw $ 1000 from account 02
account_02.withdraw(1000)

# Action 7: transfer 500 from current account
# to investment account in account 01
account_01.current_to_investment(500)

# Action 8: transfer 500 from investment account
# to current account in account 02
account_02.investment_to_current(500)

# Action 8: transfer 500 from account 02 to account 01
account_02.transfer(500, account_01)

# Show bank statements of both accounts
print()
account_01.bank_statement()
print()
account_02.bank_statement()
