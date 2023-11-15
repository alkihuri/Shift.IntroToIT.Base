#INTRO TO IT 2nd COURSE / Final Exam / TASK 3


#Перед вами крутой симулятор кафе который мы хотим показать инвестору, нужно дополнить его функционал.

#1. Сделай так чтобы выводилось итоговое время приготовления заказа.
#2. Сделай так чтобы выводилось итоговое время обслуживания клиента.
#3. Добавь время года в кафе, летом клиенты пьют больше холодных напитков, а зимой горячих.
#4. Добавь в кафе еду, например пироги и сендвичи, сделай так чтобы они готовились в течении 1-3 секунд.
#5. Добавь вывод выручки за все время работы кафе и прогноз выручки на месяц.

import random
import time

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menu = {'кофе': 50, 'чай': 30, 'капучино': 40, 'пирог': 60, 'сендвич': 70}

    def take_order(self, customer):
        order = random.choice(list(self.menu.keys()))
        price = self.menu[order]
        print(f"{customer} заказал {order}, стоимость: {price} рублей.")
        return order, price

    def prepare_order(self, order):
        print(f"Готовим {order}...")
        time.sleep(random.randint(1, 3))  # Имитация времени приготовления
        print(f"{order} готов!")

    def payment(self, price):
        print(f"К оплате: {price} рублей.")
        time.sleep(1)  # Имитация процесса оплаты
        print("Заказ оплачен.")


def main():
    cafe = Cafe("Приятное Кафе")
    customers = ['Анна', 'Михаил', 'Ольга', 'Иван', 'Екатерина']

    for customer in customers:
        print(f"\n{customer} вошел в {cafe.name}.")
        order, price = cafe.take_order(customer)
        cafe.prepare_order(order)
        cafe.payment(price)

if __name__ == "__main__":
    main()
