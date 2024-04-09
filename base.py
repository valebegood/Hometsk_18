class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'                   
        
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    
    def add_interest(self):
        amount = self._balance * (self.interest / 100)
        new_balance = amount + self._balance
        self._balance = new_balance

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraftlimit):
        super().__init__(balance, account_number)
        self.overdraftlimit = overdraftlimit
       
    def overdraft_letter(self):
        if self._balance < 0:
            print(f"Sorry! Account number - {self._account_number}: Overdrafted!")

        
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
    
    def get_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None    
    
             

    def update(self):
        for acc in self.accounts:
            if isinstance(acc, SavingsAccount):
                acc.add_interest()
            elif isinstance(acc, CurrentAccount):
                acc.overdraft_letter()

    def reset_accounts(self):
         self.accounts = []
                    


#Приклади створення різних типів банковських аккаунтів 
account1 = Account(1000, 1001)
savings_account1 = SavingsAccount(5000, 2001, 5)
current_account1 = CurrentAccount(2000, 3001, 1000)

account2 = Account(1500, 1002)
savings_account2 = SavingsAccount(6000, 2002, 4)
current_account2 = CurrentAccount(2500, 3002, 1500)

#Створення самого банку
bank = Bank()

#Додавання рахунків до нашого банку 
bank.add_account(account1)
bank.add_account(savings_account1)
bank.add_account(current_account1)
bank.add_account(account2)
bank.add_account(savings_account2)
bank.add_account(current_account2)

#Оновлення стану рахунків 
bank.update()

#Поточна інформація про рахунки
#for acc in bank.accounts:
    #print(acc)

#Скидування рахунків для наступного запуску коду
bank.reset_accounts()    
