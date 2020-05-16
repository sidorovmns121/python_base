#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

from pprint import pprint

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
movies = {}
movies ['First_movie'] = my_favorite_movies[:10]
movies ['Last_movie'] = my_favorite_movies[-15:]
movies ['Second_movie'] = my_favorite_movies[12:25]
movies ['Second_from_the_end_movie'] = my_favorite_movies[-22:-17]

pprint(movies)

