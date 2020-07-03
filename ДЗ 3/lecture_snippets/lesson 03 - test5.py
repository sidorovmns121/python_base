import turtle

pen=turtle.Turtle()

pen.shape('turtle')
#forward(X) 	Пройти вперёд X пикселей
#backward(X) 	Пройти назад X пикселей
#left(X) 	Повернуться налево на X градусов
#right(X) 	Повернуться направо на X градусов
#penup() 	Не оставлять след при движении
#pendown() 	Оставлять след при движении
#shape(X) 	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
#stamp() 	Нарисовать копию черепахи в текущем месте
#color() 	Установить цвет
#begin_fill() 	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
#end_fill() 	Вызвать после окончания рисования фигуры
#width() 	Установить толщину линии
#goto(x, y) 	Переместить черепашку в точку (x, y)

#рисуем смайл
#рисуем круг смайла
pen.speed(1)
pen.penup()
pen.setposition(0,-100)
pen.pendown()

radius = 200

pen.width(5)
pen.color("black", "yellow")
pen.begin_fill()
pen.circle(radius)
pen.end_fill()
#рисуем глаза

step = 0
for _ in range(2):
    pen.penup()
    pen.setposition(75-step,160)
    pen.pendown()
    step += 75*2

    pen.width(5)
    pen.color("black", "blue")
    pen.begin_fill()
    pen.circle(radius*0.2)
    pen.end_fill()
#рисуем нос (оставляем след)
pen.penup()
pen.width(10)
pen.setposition(0,100)
pen.pendown()
pen.setposition(0,50)
#рисуем улыбку
pen.penup()
pen.width(10)
pen.color("red")
pen.setposition(-80,0)
pen.down()
pen.right(90)
pen.circle(80,180)





pen.pause
#pen.penup()
#pen.goto(-200,0)
#pen.pendown()
#
#pen.left(90)
#
#def circle():
#    pen.circle(-50,180)
#    pen.circle(-10,180)
#
#
#for _ in range(10):
#    circle()
#вложенные круги
#def circle(radius):
#    pen.right(90)
#    pen.circle(radius)
#    pen.left(180)
#    pen.circle(radius)
#    pen.left(270)
#
#radius = 50
#for _ in range(9):
#    circle(radius=radius)
#    radius +=10

#вложенные многоугольники
#step = 0
#side = 50
#for n in range(3,20):
#    pen.setposition(-30 - step, -30 - step)
#    sum_angle = 180 * (n - 2)
#    if sum_angle%n == 0:
#        angle = sum_angle // n
#        for i in range(n):
#            pen.forward(side)
#            pen.left(180-angle)
#        step +=10
#        side += 10


