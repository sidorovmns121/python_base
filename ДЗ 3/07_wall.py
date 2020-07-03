# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = sd.COLOR_DARK_ORANGE


def brick():
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_BLACK, width=3)


x_half = 0

for y in range(0, 600, 51):
    x_half += -51
    for x in range(0 + x_half, 1200, 101):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(100 + x, 50 + y)
        brick()

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

sd.pause()
