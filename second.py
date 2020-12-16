import turtle
import random


def draw_point(x, y, drawer):
    drawer.penup()
    i = 0
    while i < len(x):
        drawer.penup()
        drawer.goto(x[i], y[i])
        drawer.dot(2, "black")
        drawer.end_fill()
        drawer.pendown()
        i += 1


def chaos(triangle, drawer):
    x = []
    y = []

    # Задаётся некоторая произвольная начальная точка
    x.insert(0, -100)
    y.insert(0, -50)

    i = 1
    while i < 10000:
        n = random.random()  # Генерируется случайное число n

        # Вероятностное пространство разбивается на 3 равных части, каждая из которых соответствует одному аттрактору
        p1 = 1.0 / 3.0
        p2 = 2.0 / 3.0

        # Активным аттрактором становится та вершина,
        # на вероятностное подпространство которой выпало сгенерированное число
        if n <= p1:
            x_a = triangle[0][0]
            y_a = triangle[0][1]
        elif p1 < n < p2:
            x_a = triangle[1][0]
            y_a = triangle[1][1]
        else:
            x_a = triangle[2][0]
            y_a = triangle[2][1]

        # Строится точка с новыми координатами
        x.insert(i, (x[i - 1] + x_a) / 2)
        y.insert(i, (y[i - 1] + y_a) / 2)

        # Возврат к началу цикла
        i += 1
    draw_point(x, y, drawer)


def main():
    drawer = turtle.Turtle()
    drawer.speed(1)
    triangle = [[-100, -50], [0, 100], [100, -50]]  # Задаются координаты аттракторов
    chaos(triangle, drawer)
    turtle.Screen().exitonclick()
    turtle.done()


main()
