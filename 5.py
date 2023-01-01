# Напишите реализацию reversed_


def reversed_(array):
    array = array.copy()
    rv = []
    while array:
        rv.append(array.pop())
    return rv
if reversed_(reversed_([1, 2, 3])) == [1, 2, 3]:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")

arr = [1, 2, 3]
if reversed_(reversed_(arr)) == arr:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")