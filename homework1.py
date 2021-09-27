# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
import win32file

with open('text.txt', 'a') as f_obj:
    while True:
        content = input('Write your all what you want: ')
        if not content:
            f_obj.close()
            print('Exit')
            break

        f_obj.write(f'{content}\n')