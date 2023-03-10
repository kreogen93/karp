# В этом задании необходимо написать функцию check_string, которая сначала проверят наличие лишних
# символов пробела слева и справа. Если есть лишние пробелы, то тогда мы считаем строку неверной.
# Затем проверяет, что только первое слово начинается с большой буквы, а остальные с маленькой,
# и в конце проводит проверку, что последний символ последнего элемента является точкой.


def check_string(some_str):
    return not (some_str[0] == ' ' or some_str[-1] == ' ') and some_str[1:] == some_str[1:].lower() and \
           some_str != some_str.lower() and some_str[-1] == '.'