import unittest
from base import Bank, Account
#Напишіть тест для класу Bank, який ми написали в 14 уроці. 
#Ви повинні написати тест для методу open_account. Переконайтеся, що рахунок відкривається і має баланс.


class TestBank(unittest.TestCase):
    def test_open_account(self):
        bank = Bank() # Bank Instance

        account_number = 1001  # New acc.
        initial_balance = 1000
        new_account = Account(initial_balance, account_number)

       
        bank.add_account(new_account)
        
        account = bank.get_account(account_number)
       
        self.assertIsNotNone(account) # Checking with IsnotNone
        
        

if __name__ == '__main__':
    unittest.main()

#Тестовий метод оновлення. Потрібно перевірити, що код додав відсотки і відправив повідомлення (була викликана функція print).
class TestBank(unittest.TestCase):
    def test_update(self):
        bank = Bank() # Bank Instance

        
        savings_account = SavingsAccount(1000, 2001, 5) # New acc.
        bank.add_account(savings_account)

        
        current_account = CurrentAccount(500, 3001, 100)
        bank.add_account(current_account)

        
        self.assertEqual(savings_account.get_balance(), 1000) # Checking with AssertEqual
        self.assertEqual(current_account.get_balance(), 500)  # Checking with AssertEqual

        
        bank.update()

        
        self.assertEqual(savings_account.get_balance(), 1050) # Checking for added %

        
        with io.StringIO() as buffer, redirect_stdout(buffer):
            bank.update()
            output = buffer.getvalue().strip()
            self.assertIn("Sorry! Account number - 3001: Overdrafted!", output) # Checking for print message 

if __name__ == '__main__':
    unittest.main()    