#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
from pprint import pprint
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)
# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
zooo={}
zooo['номер_клетки_льва']=(zoo.index('lion')+1)
zooo['номер_клетки_жаворонок']=(zoo.index('lark')+1)
pprint(zooo)


