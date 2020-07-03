# import simple_draw as sd

# sd.resolution = (1200, 600)
# point = sd.get_point(65,65)

# radius = 50
# for _ in range(3):
#   radius += 5
#    sd.circle(center_position=point, radius=radius, width=2)
#
#
# sd.pause()
# это был просто круг нарисован. ниже создадим функцию круга
# -------------------------------------------------------------------------------
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# import simple_draw as sd
# sd.resolution = (1200, 600)

# def bubble (point, step):
#    radius = 50
#    for _ in range(3):
#        radius += step
#        sd.circle(center_position=point, radius = radius, width=2)
# point = sd.get_point(100, 100)
# bubble(point, 10)

# sd.pause()
# -------------------------------------------------------------------------------------------
# Нарисовать 10 пузырьков в ряд
#import simple_draw as sd
#
#sd.resolution = (1200, 600)


#def bubble(point):
#    for step in range(25,50,9):
#       sd.circle(center_position=point, radius=step, width=2)
#
#
#for y in range(120, 420, 120):
#    for x in range(100, 1100, 100):
#        point = sd.get_point(x, y)
#        bubble(point)
#
#sd.pause()
#Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (0, 127, 127)

def bubble(point):
    for step in range(25,50,6):
        sd.circle(center_position=point, radius=step, color=sd.random_color(), width=2)


for _ in range(100):
    point = sd.random_point()
    bubble(point)

sd.pause()
