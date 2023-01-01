# В этом задании потребуется написать функцию process_string, которая приводит строку[1:] к нижнему регистру
# и заменяет все слова 'intern' на 'junior'


def process_string(some_str):
    return some_str[1:].lower().replace('intern', 'junior')