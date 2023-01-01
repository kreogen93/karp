# Попробуем использовать функцию для сокращения количества кода. Для этого смоделируем ситуацию из практики.
# Ваш коллега придумал свой способ «генерации» данных. Для этого он предложил брать набор чисел, возводить их в куб,
# потом брать остаток от деления на 7, прибавлять к этому изначальный массив — и выдавать результат как «сгенерированные» данные.
# Исправьте код коллеги


# много другого кода, который тоже печатает
# ...
# Код коллеги

def math_task(data):
    answer = []
    # возводим в третью степень
    for elem in data:
        answer += [elem ** 3]
    # берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    # прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    # возвращаем результат
    return answer


#math_task(test_data)
# print(math_task([1, 4, 5, 9]))
