import turtle


def drawTriangle(points, color, drawer):
    drawer.fillcolor(color)
    drawer.up()
    drawer.goto(points[0][0], points[0][1])
    drawer.down()
    drawer.begin_fill()
    drawer.goto(points[1][0], points[1][1])
    drawer.goto(points[2][0], points[2][1])
    drawer.goto(points[0][0], points[0][1])
    drawer.end_fill()


def getMid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def iterative(triangle, angles, drawer):
    colormap = ['black', 'purple', 'gray', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(triangle, colormap[angles], drawer)
    if angles > 0:
        iterative([triangle[0],
                   getMid(triangle[0], triangle[1]),
                   getMid(triangle[0], triangle[2])],
                  angles - 1, drawer)
        iterative([triangle[1],
                   getMid(triangle[0], triangle[1]),
                   getMid(triangle[1], triangle[2])],
                  angles - 1, drawer)
        iterative([triangle[2],
                   getMid(triangle[2], triangle[1]),
                   getMid(triangle[0], triangle[2])],
                  angles - 1, drawer)


def main():
    drawer = turtle.Turtle()
    triangle = [[-100, -50], [0, 100], [100, -50]]
    iterative(triangle, 3, drawer)
    turtle.Screen().exitonclick()


main()
