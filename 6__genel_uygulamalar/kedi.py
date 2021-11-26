import turtle

t = turtle.Turtle()
t.pensize(8)
t.penup()
t.goto(0, -100)
t.pendown()

# Kafa 
for i in range (36):
    t. forward (30)
    t.left (10)
# Gözler
t.penup()
t. goto (-80, 90)
t. pendown ()

t.left (90)
for i in range (45):
    t. forward(2)
    t.right (4)
t.penup()
t.goto (50, 90)
t.pendown()
t.left(-180)
for i in range (45):
    t. forward (2)
    t.right (4)
    
# Burun
t.penup()
t.goto(0, 50)
t.pendown()

t.setheading(0)

for i in range (5):
    t. forward (25)
    t.right (120)
starting_nose_x = t.xcor()
starting_nose_y = t.ycor()

t.left(120)
t.forward(10)
for i in range(4):
    t.right (16)
    t. forward(17)
t.penup()
t.goto(starting_nose_x, starting_nose_y)
t.pendown()
t.setheading(-60)
t. forward (10)
for i in range (4):
    t.left(16)
    t. forward (17)
t. penup()
t.goto(-19,--10)
t.pendown()
t.right (100)
for i in range (10):
    t. forward (12)
    t.left (21)
t.penup()
t.goto (114, 212)
t.pendown()
t. forward (100)
t.left(120)
t.forward (75)
t.penup()
t.goto(-107, 193)
t.pendown()
t.setheading(75)
t.forward (100)
t.right (120)
t.forward (75)
t.ht()

breakpoint ()
