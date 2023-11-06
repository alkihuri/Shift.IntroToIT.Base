#INTRO TO IT 2nd COURSE
#Расчет платежа по ипотеке:
#(Используя простую формулу аннуитетного платежа)
# Подсказка в году 12 месяцев, а не 11


def mortgage_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    if monthly_interest_rate == 0:
        return principal / months
    annuity_coefficient = (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)
    return principal * annuity_coefficient