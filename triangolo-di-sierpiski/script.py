import turtle

def draw_sierpinski(t, length, depth):
    """Disegna il triangolo di Sierpinski usando turtle."""
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        draw_sierpinski(t, length/2, depth-1)
        t.forward(length/2)
        draw_sierpinski(t, length/2, depth-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        draw_sierpinski(t, length/2, depth-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    draw_sierpinski(t, 400, 4)
    screen.exitonclick()

if __name__ == "__main__":
    main()

