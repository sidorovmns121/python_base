# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month_expenses = 0
month_income = 0
i = 0
while i < 10:
    month_income += educational_grant
    if i == 0:
        month_expenses = expenses
    elif i >= 1:
        month_expenses += expenses*1.03
    i += 1
    print('Расходы в', i, 'месяце - ', month_expenses, 'доходы', month_income)
difference = month_expenses-month_income
print('Студенту надо попросить', difference, 'рублей')

# TODO здесь ваш код
