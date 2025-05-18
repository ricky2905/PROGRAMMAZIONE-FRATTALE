import turtle

def draw_cavolfiore(t, length, level):
    """Disegna un frattale tipo cavolfiore, simile alla curva di Peano.
    t: turtle, length: lunghezza segmento, level: livello ricorsione"""
    if level == 0:
        t.forward(length)
    else:
        draw_cavolfiore(t, length/3, level-1)
        t.left(90)
        draw_cavolfiore(t, length/3, level-1)
        t.right(90)
        draw_cavolfiore(t, length/3, level-1)
        t.right(90)
        draw_cavolfiore(t, length/3, level-1)
        draw_cavolfiore(t, length/3, level-1)
        t.left(90)
        draw_cavolfiore(t, length/3, level-1)
        t.left(90)
        draw_cavolfiore(t, length/3, level-1)
        t.right(90)
        draw_cavolfiore(t, length/3, level-1)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    draw_cavolfiore(t, 300, 3)
    screen.exitonclick()

if __name__ == "__main__":
    main()

