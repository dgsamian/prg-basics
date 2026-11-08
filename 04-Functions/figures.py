import turtle

def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)

# Backward compatibility for older code
# that still uses the misspelled name.
draw_trangle = draw_triangle

def draw_rectangle(lenght_a, lenght_b):
    for i in range(2):
        turtle.forward(lenght_a)
        turtle.right(90)
        turtle.forward(lenght_b)
        turtle.right(90)

def move_to(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()