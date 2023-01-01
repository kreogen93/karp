# Напишите функцию final_balance, которая на вход принимает начальную сумму init_sum, процентную ставку
# interest_rate, количество лет years и округление round_num. Функция должна возвращать сумму по истечении этого срока.
# Аргумент функции round_num должен задавать, сколько значащих чисел после запятой оставлять. Так, при round_num = 2
# сумма будет выводиться с точностью до копеек, при round_num = 0 - с точностью до рублей. При этом round_num
# может быть отрицательным! В таком случае округление будет грубее: round_num = -1 будет округлять до десятков рублей,
# round_num = -2 до сотен и т. д.
# Поставьте значение по умолчанию round_num, равное 2. Это соответствует округлению до копеек.


def final_balance(init_sum, interest_rate, years, round_num = 2):
    return round(init_sum * interest_rate * years, round_num)