# Напишите функцию sum_as_ints, которая принимает на вход список из строк, пытается привести их
# к целому числу через int(element) и считает сумму. Список может содержать любые данные,
# но если они не приводятся через int(element), то программа должна их отбросить.


def sum_as_ints(list_str):
    sum = 0
    try:
        for elem in list_str:
            sum += int(elem)
    except:
        pass
    return sum
