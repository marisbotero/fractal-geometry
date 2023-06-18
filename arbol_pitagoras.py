import turtle

def draw_tree(order, size):
    """
    Dibuja un árbol de Pitágoras de un cierto orden y tamaño.
    """
    if order == 0:  # caso base: solo dibuja una línea
        turtle.forward(size)
        turtle.backward(size)
    else:
        # dibuja la "rama" (un triángulo rectángulo)
        turtle.forward(size)

        turtle.right(45)

        # dibuja dos "sub-árboles"
        draw_tree(order-1, size/2)

        turtle.left(90)

        draw_tree(order-1, size/2)

        turtle.right(45)

        # vuelve a la posición y orientación original
        turtle.backward(size)

# establece la velocidad de dibujo
turtle.speed(1)

# mueve la tortuga a una buena posición de inicio
turtle.up()
turtle.goto(-100, -200)
turtle.left(90)  # Hace que la tortuga mire hacia arriba
turtle.down()

# dibuja el árbol
draw_tree(10, 200)

# oculta la tortuga
turtle.hideturtle()

# mantiene la ventana abierta hasta que el usuario la cierre
turtle.done()
