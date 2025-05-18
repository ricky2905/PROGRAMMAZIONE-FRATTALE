import turtle

def koch_curve(t, length, level):
    """Disegna la curva di Koch ricorsiva.
    t: turtle, length: lunghezza segmento, level: livello di dettaglio"""
    if level == 0:
        t.forward(length)
    else:
        koch_curve(t, length/3, level-1)
        t.left(60)
        koch_curve(t, length/3, level-1)
        t.right(120)
        koch_curve(t, length/3, level-1)
        t.left(60)
        koch_curve(t, length/3, level-1)

def snowflake(t, length, level):
    """Disegna il fiocco di neve unendo 3 curve di Koch"""
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    snowflake(t, 300, 4)
    screen.exitonclick()

if __name__ == "__main__":
    main()

