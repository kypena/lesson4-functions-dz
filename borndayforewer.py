"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
# Variant 1

# def year():
#     return input('Ввведите год рождения А.С.Пушкина:')
#
#
# def day():
#     return input('Ввведите день рождения Пушкин?')

# Variant 2

# def ask_year():
#     year = input('Ввведите год рождения А.С.Пушкина:')
#     while year != '1799':
#         print("Не верно")
#         year = input('Ввведите год рождения А.С.Пушкина:')
#
#
# def ask_day():
#
#     day = input('Ввведите день рождения Пушкин?')
#     while day != '6':
#         print("Не верно")
#         day = input('В какой день июня родился Пушкин?')
#     print('Верно')
#
#
# ask_year()
# ask_day()

# Variant 3

def question_data(question, data):
    answer = input(question)# функция input() используется для ввода значений с клавиатуры
    while answer != data: # что такое ключевое слово while
        print("Не верно")
        answer = input(question)
    else:
        print(" Correct!")


question_data('Enter year - ', '1799')