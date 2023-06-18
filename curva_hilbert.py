import turtle

def hilbert_curve(order, angle, distance):
    # Caso base: order es 0
    if order == 0:
        return

    turtle.right(angle)
    hilbert_curve(order-1, -angle, distance)
    turtle.forward(distance)
    turtle.left(angle)
    hilbert_curve(order-1, angle, distance)
    turtle.forward(distance)
    hilbert_curve(order-1, angle, distance)
    turtle.left(angle)
    turtle.forward(distance)
    hilbert_curve(order-1, -angle, distance)
    turtle.right(angle)

# inicializar la tortuga
turtle.speed(0)

# cambiar el tamaño de la ventana de la tortuga
turtle.setup(800, 800)

# posicionar la tortuga
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# dibujar la curva de Hilbert
hilbert_curve(5, 90, 10)

# ocultar la tortuga
turtle.hideturtle()

# mantener la ventana abierta
turtle.done()
