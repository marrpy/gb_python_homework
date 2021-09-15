# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func():
    var_1 = float(input('Введите число: '))
    var_2 = float(input('Введите число: '))
    var_3 = float(input('Введите число: '))
    nums = [var_1, var_2, var_3]
    del nums[nums.index(min(nums))]
    return sum(nums)

print(my_func())
