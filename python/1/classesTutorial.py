import turtle
def add_turtle_style(turtle, shape, color):
    turtle.shape(shape)
    turtle.color(color)

def load_window():
    w = turtle.Screen()
    w.bgcolor("red")
    return w

def draw_circle(turtle, size):
    turtle.circle(size)

def draw_square(turtle):
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)

def draw_triangle(turtle):
    turtle.right(60)
    for i in range(1,4):
        turtle.forward(100)
        turtle.right(120)
    
def draw():
    w = load_window()
    jose = turtle.Turtle()
    add_turtle_style(jose, "turtle", "black")
    draw_square(jose)
    mony = turtle.Turtle()
    add_turtle_style(mony, "arrow", "blue")
    draw_circle(mony, 100)
    juan = turtle.Turtle()
    add_turtle_style(juan, "arrow", "green")
    draw_triangle(juan)
    
    w.exitonclick()

def drawFractal():
    w = load_window()
    jose = turtle.Turtle()
    draw_square(jose)
    for i in range(1, (360/10)):
        jose.right(10)
        draw_square(jose)
    w.exitonclick()

def draw_hoja(turtle):
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)

def drawhoja():
    w = load_window()
    jose = turtle.Turtle()
    draw_hoja(jose)
    for i in range(1, (360/5) + 1):
        jose.right(5)
        draw_hoja(jose)
    w.exitonclick()
    
#draw()
#drawFractal()
drawhoja()
