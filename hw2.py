# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Результат: [12, 44, 4, 10, 78, 123].
import random
from random import randint

data = []
for i in range(10):
   data.append(random.randint(0, 100))
new_data = []
for key, value in enumerate(data):
        if key + 1 < len(data) and value < data[key + 1]:
            new_data.append(data[key + 1])
print(f'Исходный список: {data}')
print(f'Новый список: {new_data}')

