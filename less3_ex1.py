# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func():
    var_1 = float(input('Введите делимое: '))
    var_2 = float(input('Введите делитель: '))
    if var_2 == 0:
        print('На нуль делить нельзя!')
        var_1 = float(input('Введите делимое: '))
        var_2 = float(input('Введите делитель: '))
        quotient = var_1 / var_2
    else:
        quotient = var_1 / var_2
    return quotient
result = div_func()
print(result)