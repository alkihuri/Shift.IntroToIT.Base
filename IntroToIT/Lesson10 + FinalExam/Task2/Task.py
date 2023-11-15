#INTRO TO IT 2nd COURSE / Final Exam / TASK 2

#Ктото обратно сломал банковское ПО! Помогите разобраться в чем дело и исправить ошибки. Для теста используйте класс BankAccountTest в файле TestBankAccount.py 


class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # Позволяем вносить отрицательные суммы
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # Позволяем снимать средства даже при недостаточном балансе
        self.balance -= amount
        return self.balance

    def get_balance(self):
        # Возвращаем баланс, уменьшенный на 100
        return self.balance - 100

    def set_balance(self, balance):
        self.balance = balance



def main():
    accounts = {}

    while True:
        print("\nБанковская Система")
        print("1. Создать новый счет")
        print("2. Проверить баланс")
        print("3. Депозит")
        print("4. Снятие")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Введите имя владельца счета: ")
            account_number = input("Введите номер счета: ")
            accounts[account_number] = BankAccount(account_number, name)
            print(f"Счет {account_number} создан для {name}.")

        elif choice == "2":
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                print(f"Баланс счета: {accounts[account_number].get_balance()}")
            else:
                print("Счет не найден.")

        elif choice == "3":
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                amount = float(input("Введите сумму для депозита: "))
                accounts[account_number].deposit(amount)
                print(f"Депозит выполнен. Новый баланс: {accounts[account_number].get_balance()}")
            else:
                print("Счет не найден.")

        elif choice == "4":
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                amount = float(input("Введите сумму для снятия: "))
                result = accounts[account_number].withdraw(amount)
                if result == "Недостаточно средств":
                    print(result)
                else:
                    print(f"Снятие выполнено. Остаток на счете: {result}")
            else:
                print("Счет не найден.")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
