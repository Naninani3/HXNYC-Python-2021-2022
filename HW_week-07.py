'''
please familiarize yourself with the turtle module and draw a square as we did in the class.
(if you already know how to use "turtle" to draw a square...draw a triangle instead.) 
'''

https://trinket.io/python/7545d88b78

 
import turtle


tt = turtle.Turtle()

tt.speed(7)

tt.hideturtle()

tt.fillcolor("red")

tt.begin_fill()

tt.forward(200)

tt.right(90)

tt.forward(200)

tt.right(90)

tt.forward(200)

tt.right(90)

tt.forward(200)

tt.end_fill()

tt.penup()

tt.sety(-100)

tt.pendown()

tt.fillcolor("black")

tt.begin_fill()

tt.right(45)

tt.forward(141)

tt.right(90)

tt.forward(141)

tt.right(90)

tt.forward(141)

tt.right(90)

tt.forward(141)

tt.right(90)

tt.forward(141)

tt.end_fill()

tt.penup()

tt.sety(-150)

tt.setx(100)

tt.pendown()

tt.fillcolor("blue")

tt.begin_fill()

tt.setheading(0)

tt.circle(50)

tt.end_fill()
