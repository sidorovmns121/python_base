#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

Moscow = cities['Moscow']
London = cities['London']
Paris = cities['Paris']

Moscow_London = round(((Moscow[0]-London[0]) ** 2 + (Moscow[1]-London[1]) ** 2) ** .5)
Moscow_Paris = round(((Moscow[0]-Paris[0]) ** 2 + (Moscow[1]-Paris[1]) ** 2) ** .5)

London_Moscow = round(((London[0]-Moscow[0]) ** 2 + (London[1]-Moscow[1]) ** 2) ** .5)
London_Paris = round(((London[0]-Paris[0]) ** 2 + (London[1]-Paris[1]) ** 2) ** .5)

Paris_London = round(((Paris[0]-London[0]) ** 2 + (Paris[1]-London[1]) ** 2) ** .5)
Paris_Moscow = round(((Paris[0]-Moscow[0]) ** 2 + (Paris[1]-Moscow[1]) ** 2) ** .5)

destination = {}
destination ['Moscow_city'] = {}
destination ['Moscow_city'] ['to London'] = Moscow_London
destination ['Moscow_city'] ['to Paris'] = Moscow_Paris

destination ['London_city'] = {}
destination ['London_city'] ['to Moscow'] = London_Moscow
destination ['London_city'] ['to Paris'] = London_Paris

destination ['Paris_city'] = {}
destination ['Paris_city'] ['to London'] = Paris_London
destination ['Paris_city'] ['to Moscow'] = Paris_Moscow

pprint(destination)




