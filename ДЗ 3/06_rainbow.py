# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.background_color = sd.COLOR_WHITE

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


#def line():
#    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)


#step = 0

#for color in rainbow_colors:
#    start_point = sd.get_point(50 + step, 50)
#    end_point = sd.get_point(350 + step, 550)
#    line()
#    step += 5

#sd.pause()
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
def circle():
    sd.circle(center_position=center, radius=radius, color=color, width=width)


radius = 400
width = 15

for color in rainbow_colors:
    center = sd.get_point(350, 0)
    circle()
    radius += 18
    width += 0

sd.pause()
