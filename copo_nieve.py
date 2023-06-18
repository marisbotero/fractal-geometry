import turtle

def draw_koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_koch_snowflake(length/3, depth-1)
        turtle.left(60)
        draw_koch_snowflake(length/3, depth-1)
        turtle.right(120)
        draw_koch_snowflake(length/3, depth-1)
        turtle.left(60)
        draw_koch_snowflake(length/3, depth-1)

def draw_snowflake(length, depth):
    for _ in range(3):
        draw_koch_snowflake(length, depth)
        turtle.right(120)

turtle.speed(0)

turtle.up()
turtle.goto(-150, 90)
turtle.down()

draw_snowflake(300, 4)

turtle.hideturtle()
turtle.done()
