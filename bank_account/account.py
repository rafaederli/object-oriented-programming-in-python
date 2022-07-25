from typing import List, Tuple


class Account:

    bank_code: str = '001'
    bank_name: str = 'Bank Tho'

    def __init__(self, bank_branch: str,
                 account_number: str,
                 account_holder: str,
                 current_balance: int,
                 investment_balance: int,
                 limit: int = 1000) -> None:
        self.__bank_branch: str = bank_branch
        self.__account_number: str = account_number
        self.__account_holder: str = account_holder
        self.__current_balance: int = current_balance
        self.__investment_balance: int = investment_balance
        self.__limit: int = limit
        self.__bank_statement: List[Tuple[int, int]] = []

    @property
    def bank_branch(self) -> str:
        return self.__bank_branch

    @bank_branch.setter
    def bank_branch(self, bank_branch: str) -> None:
        self.__bank_branch = bank_branch

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def account_holder(self) -> str:
        return self.__account_holder

    @property
    def current_balance(self) -> int:
        return self.__current_balance

    @property
    def investment_balance(self) -> int:
        return self.__investment_balance

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int) -> None:
        self.__limit = limit

    def bank_statement(self) -> None:
        print('---------------------------------------'
              '-------------------------------------------')
        print(f'Bank Statement - {self.bank_name} - cód. {self.bank_code}')
        print(f'Bank Branch: {self.bank_branch}')
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Number: {self.account_number}')
        print()
        print(f'Investment balance:      $ {self.__investment_balance}')
        print(f'Current balance:         $ {self.__current_balance}')
        print(f'Limit:                   $ {self.__limit}')
        print()
        for transaction in self.__bank_statement:
            if transaction[0] == 1:
                print(f'Current account deposit:      '
                      f'                         $ {transaction[1]}')
            elif transaction[0] == 2:
                print(f'Current account withdraw:     '
                      f'                         $ {transaction[1]}')
            elif transaction[0] == 3:
                print(f'Transfer from current account '
                      f'to investment account:   $ {transaction[1]}')
            elif transaction[0] == 4:
                print(f'Transfer from investment account '
                      f'to current account:   $ {transaction[1]}')
            elif transaction[0] == 5:
                print(f'Transfer between accounts:       '
                      f'                      $ {transaction[1]}')
        print('------------------------------------------'
              '----------------------------------------')

    def __check_balance(self, amount: int) -> bool:
        return amount <= self.__current_balance + self.__limit

    def __check_current(self, amount: int) -> bool:
        return amount <= self.__current_balance

    def __check_investment(self, amount: int) -> bool:
        return amount <= self.__investment_balance

    def deposit(self, amount: int) -> None:
        self.__current_balance += amount
        self.__bank_statement.append((1, amount))

    def withdraw(self, amount: int) -> None:
        if self.__check_balance(amount):
            withdraw_current_balance: int = self.__current_balance - amount
            if withdraw_current_balance >= 0:
                self.__current_balance -= amount
                self.__bank_statement.append((2, amount))
            else:
                self.__limit: int = \
                    self.limit - (amount - self.__current_balance)
                self.__current_balance: int = 0
                self.__bank_statement.append((2, amount))
        else:
            print('The amount exceeded the account limit.')

    def current_to_investment(self, amount: int) -> None:
        if self.__check_current(amount):
            self.__current_balance -= amount
            self.__investment_balance += amount
            self.__bank_statement.append((3, amount))
        else:
            print('The amount exceeded the current account balance.')

    def investment_to_current(self, amount: int) -> None:
        if self.__check_investment(amount):
            self.__current_balance += amount
            self.__investment_balance -= amount
            self.__bank_statement.append((4, amount))
        else:
            print('The amount exceeded the investment account balance.')

    def transfer(self, amount: int, account_number: str) -> None:
        if self.__check_balance(amount):
            self.__current_balance -= amount
            account_number.deposit(amount)
            self.__bank_statement.append((5, amount))
        else:
            print('The amount exceeded the account limit.')
