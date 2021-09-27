# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def rewrite_file():
    numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_count = []
    try:
        with open('task4.txt', 'r+', encoding="utf-8") as file:
            with open('new_file.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_count.append(numbers[i[0]] + ' ' + i[1])
                new_file.writelines(new_count)
    except FileNotFoundError:
        return 'Файл не найден.'

rewrite_file()