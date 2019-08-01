import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(50)
    for j in range(45):
        for i in range(3):
            brad.forward(200)
            brad.right(120)
            brad.right(60)
        brad.right(8)
    window.exitonclick()

draw_square()