# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


def count_subjects():
    try:
        mydict = {}
        with open("school.txt", encoding='utf-8') as f_obj:
            for line in f_obj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()