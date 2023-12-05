"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

# 3. история покупок
# выводим историю покупок пользователя (название и сумму)
# возвращаемся в основное меню

# Variant 1

# while True: #Ключовое слово while используется для создания цикла 
#     print('1. пополнение счета')
#     print('2. покупка')
#     print('3. история покупок')
#     print('4. выход')
#
#     choice = input('Choose menu - ')
#
#     balance_account = 0
#
#     while choice == '1':
#
#         donation = int(input('Enter the sum to dowload - '))
#
#         balance_account += donation
#         print(f" balance_account: {balance_account}")
#         choice = input('Enter choice code - ')
#
#     if choice == '2':
#         purchase_price = int(input('Enter purchase price - '))
#         if purchase_price <= balance_account:
#             purchase_history = []
#             balance_account -= purchase_price
#             purchase_name =  input('Enter the name of purchse -  ')
#             purchase_history.append((purchase_name,purchase_price, balance_account))
#
#         else:
#             print('Lack of funds on the account')
#
#     elif choice == '3':
#         print(purchase_history)
#     elif choice == '4':
#         break
#     else:
#         print('Not existing menu type.')


# Variant 2

def choice_1(account): # what do u mean keyword def ? 

    while choice == '1': # Why is 1 is string but not integer type
        donation = int(input('Enter the sum to dowload - '))
        account += donation
        #print(f" balance_account: {balance_account}")
        return account
    #else:
    #    print('Enter another code')


def choice_2(account):
    if choice == '2':
        purchase_price = int(input('Enter purchase price - '))

        if purchase_price > account:

            print('Lack of funds on the account')


        else:
            #purchase_history = []
            account -= purchase_price
            purchase_name =  input('Enter the name of purchse -  ')
            purchase_history.append((purchase_name,purchase_price, balance_account))
            return account

purchase_history = []
balance_account = 0

while True:
    print("""1. пополнение счета 
          \n2. покупка
          \n3. история покупок
          \n4. выход\n""") # We use escape sequence fhttps://code-basics.com/ru/languages/python/lessons/escape-characters 



    choice = input('Choose menu - ')


    if choice == '1':
        choice_1(balance_account)

    # while choice == '1':
    #
    #     donation = int(input('Enter the sum to dowload - '))
    #
    #     balance_account += donation
    #     print(f" balance_account: {balance_account}")
    #     choice = input('Enter choice code - ')

    if choice == '2':
        balance_account = choice_2(balance_account)

    elif choice == '3':
        print(purchase_history)
    elif choice == '4':
        break
    else:
        print('Not existing menu type.')
print(f" balance_account: {balance_account}")


 # Variant 3
# def purchase():
#
#     purchase_list = dict()
#     account = 0
#     money = int(input("Enter the sum you want to submit on your account - "))
#     account += money
#
#     price = int(input('Enter purchase price - '))
#
#     if price > account:
#         print("Lack of funds for this purchase.")
#     else:
#         account -= price
#         purchase_name = input('Enter the purchase name - ')
#         purchase_list['purchase_name'] = purchase_name
#         purchase_list['price'] = price
#         purchase_list['account balance'] = account
#     print(purchase_list)
#         #print(purchase_name, ":", price,':', account)
#
#
# purchase()
