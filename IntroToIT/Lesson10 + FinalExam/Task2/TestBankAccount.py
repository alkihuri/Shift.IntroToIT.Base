import unittest
from Task import BankAccount 
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("12345", "Test User", 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_withdraw_not_enough_funds(self):
        result = self.account.withdraw(1500)
        self.assertEqual(result, "Недостаточно средств")

    def test_deposit_negative_amount(self):
        result = self.account.deposit(-100)
        self.assertEqual(result, "Сумма депозита должна быть положительной")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

if __name__ == '__main__':
    unittest.main()
