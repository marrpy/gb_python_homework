text_1 = 'Hello Python!'
text_2 = 'World'

print(text_1 + text_2)  # конкатенация
print(text_2 * 2)  # дублирование

a = 10
b = 20
c = not a > b # булевая инверсия, если было true, то будет false
d =  a > b

print(c, d)

num_1 = input('Введите первое число - ') # input по умолчанию принимает str
num_2 = input('Введите второе число - ')

sum_result = int(num_1) + int(num_2)
print(sum_result)