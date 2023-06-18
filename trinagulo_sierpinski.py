import turtle

def draw_sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# Inicializar la tortuga
turtle.speed(0)

# Posición inicial de la tortuga
turtle.up()
turtle.goto(-200, -175)
turtle.down()

# Dibujar el triángulo de Sierpinski
draw_sierpinski(400, 5)

# Ocultar la tortuga
turtle.hideturtle()

# Mantener la ventana abierta
turtle.done()
