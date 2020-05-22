'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import defaultdict

# Ввожу счетчик, словарь предприятий
firm_counter = int(input('Введите число компаний:\n'))
firm_dict = {}

# Ввожу среднюю прибыль и список по средней прибыли
firm_sum_averange = 0
firm_sum_profit = []

# Прохожусь по количеству компаний
for i in range(firm_counter):

    # Запрашиваю ввод наименования компании
    firm_name = input('Введите имя компании:\n')

    # Ввожу defaultdict и firm_average
    firm_profit = defaultdict(dict)
    firm_average = []

    # Прохожусь по количеству кварталов (4)
    for q in range(1, 5):

        # Запрашиваю у пользователя прибыль по кварталам
        quarter = int(input(f'Введите прибыль за квартал №{q}:\n'))

        # Создаю словарь для каждой компании
        firm_profit[f'Profit_{q+1}'] = quarter

        # Добавляю в списки для каждой компании и для компаний в целом
        firm_average.append(quarter)
        firm_sum_profit.append(quarter)

    # Добавляю в словарь среднюю прибыль
    firm_profit['average'] = sum(firm_average)/len(firm_average)
    firm_dict[firm_name] = firm_profit

# Рссчитываю среднюю прибыль по компаниям
firm_sum_averange = sum(firm_sum_profit)/len(firm_sum_profit)

# Ввожу переменные для оокнчательного вывода
# и прохожусь поциклу
profit_list = []
not_profit_list = []
for key in firm_dict:

    # Распределяю компании по средней прибыли
    if firm_dict[key]['average'] > firm_sum_averange:
        profit_list.append(key)
    else:
        not_profit_list.append(key)

# Ввыожу результат работы, согласно условию
print(f'Компании, имеющие прибыль выше средней: {", ".join(profit_list)}.')
print(f'Компании, имеющие прибыль ниже средней: {", ".join(not_profit_list)}.')