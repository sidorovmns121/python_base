#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'mother', 'sister']


# список списков приблизителного роста членов вашей семьи
my_family_height = [[my_family [0], 174],[my_family[1], 168],[my_family[2], 170]]

height = {}
height ['Alex'] = my_family_height [0][0:2]

height ['height_summ']=my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]

print(height)
print('Общий рост моей семьи -', height['height_summ'])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
