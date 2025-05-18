import turtle

def draw_tree(branch_length, t):
    """Disegna un albero frattale usando turtle.
    branch_length: lunghezza del ramo corrente
    t: oggetto turtle"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)  # Puntare verso l'alto
    t.speed(0)  # Velocità massima
    t.penup()
    t.goto(0, -200)  # Posizione iniziale
    t.pendown()
    draw_tree(100, t)
    screen.exitonclick()

if __name__ == "__main__":
    main()

