salary = 5000
spend = 6000
months = 10
increase = 0.03

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
while True:
    capital = money_capital
    current_spend = spend
    for r in range(months):
        if capital + salary < current_spend:
            break
        capital = capital + salary - current_spend
        current_spend *= (1 + increase)
    else:
        print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
        break
    money_capital += 1