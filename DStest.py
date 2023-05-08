import turtle
turtle.delay(10)
turtle.pensize(20)

# Move the turtle to the right position of the left tyre
turtle.penup()
turtle.setposition(-87.5, -50)
turtle.setheading(90)

# Draw the left tyre
turtle.begin_fill()
turtle.circle(62.5)
turtle.end_fill()

# Move the turtle to the right position of the right tyre
turtle.penup()
turtle.setposition(212.5, -50)
turtle.setheading(90)

# Draw the right tyre
turtle.begin_fill()
turtle.circle(62.5)
turtle.end_fill()

# Draw the handle
turtle.penup()
turtle.setposition(137.5, 0)
turtle.pendown()
turtle.setposition(75, 150)

# Draw the straight part of the handle
turtle.setheading(0)
turtle.setposition(125, 150)

# Draw the circular part of the handle
turtle.penup()
turtle.setposition(125, 100)
turtle.pendown()
turtle.circle(25, 180)

# Draw the seat tube
turtle.penup()
turtle.setposition(12.5, -50)
turtle.pendown()
turtle.setposition(-62.5, 137.5)

# Draw the saddle
turtle.setheading(180)
turtle.setposition(-100, 137.5)

# Draw the top tube
turtle.penup()
turtle.setposition(100, 75)
turtle.pendown()
turtle.setposition(-37.5, 75)

# Draw the down tube
turtle.penup()
turtle.setposition(100, 75)
turtle.pendown()
turtle.setposition(12.5, -50)

# Draw the seat stay
turtle.penup()
turtle.setposition(-37.5, 75)
turtle.pendown()
turtle.setposition(-150, -50)

# Draw the chain stay
turtle.penup()
turtle.setposition(12.5, -50)
turtle.pendown()
turtle.setposition(-150, -50)