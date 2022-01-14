"""
Peter Mei

Write a program that will display your splash page as the first page for 20 seconds
The second page will contain the image associated with your Zodiac Sign, stays for 20 seconds
Third page will display the pattern created with the turtle Python module, stays for 30 seconds
Last page should be a night background and the stars are illuminated one by one after ten seconds,
, then the connecting lines will appear one by one, page stays for thirty seconds

"""
import turtle
import time

window = turtle.Screen()
window.setup(width=1.0,height=1.0)
window.bgcolor("black")
turtle.color("white")


#Display a welcome page
def splashpage():
    turtle.hideturtle()
    turtle.penup()
    turtle.write("Python Constellation Project \n The Virgo Constellation \n Peter Mei", True, align="center", font = ("Arial", 48))

#dispalys the constellations pictures
def pageone():
    window.bgpic("virgo.png")
    window.update()

#starting from Spica,move to the upper right
def pageTwo():
    #Spica star is the starting position moving toward small dot 1
    window.bgcolor("black")
    turtle.color("white")
    turtle.setposition(0,.98)
    turtle.write("Spica", align="right", font=("Arial",18))
    turtle.dot(22)
    turtle.left(65)

    turtle.forward(100)
    turtle.dot(10)
    turtle.right(30)
    turtle.forward(150)

    #Porrima
    turtle.dot(22)
    turtle.write("Porrima", align="right", font=("Arial",18))
    turtle.right(20)
    turtle.forward(50)

    turtle.dot(10)
    turtle.forward(10)
    turtle.dot(10)

    turtle.left(7)
    turtle.forward(90)
    turtle.dot(10)

    turtle.left(60)
    turtle.forward(75)
    turtle.dot(10)

    turtle.left(100)
    turtle.forward(55)
    turtle.dot(10)

    turtle.right(50)
    turtle.forward(10)
    turtle.dot(10)


    turtle.penup()
    turtle.hideturtle()
    #Starting from Spica move to the left
    #reset positon turtle
    turtle.setposition(0,.98)
    turtle.pendown()
    turtle.showturtle()
    turtle.left(50)
    turtle.forward(150)
    turtle.dot(10)

    turtle.right(60)
    turtle.forward(50)
    turtle.dot(10)

    turtle.left(58)
    turtle.forward(65)
    turtle.dot(10)

    turtle.penup()
    turtle.hideturtle()

    #Starting from Spica move up left
    #reset position
    turtle.setposition(0,.98)
    turtle.pendown()
    turtle.showturtle()

    turtle.right(65)
    turtle.forward(200)
    turtle.dot(10)

    turtle.right(85)
    turtle.forward(200)
    turtle.dot(10)

    turtle.left(75)
    turtle.forward(75)
    turtle.dot(10)

    #reset
    turtle.penup()
    turtle.hideturtle()

    #starting from spica move to the top
    turtle.setposition(0, .98)
    turtle.showturtle()
    turtle.pendown()
    turtle.left(10)
    turtle.forward(200)
    turtle.dot(10)

    turtle.left(55)
    turtle.forward(150)
    turtle.dot(10)

    turtle.left(13)
    turtle.forward(100)
    turtle.dot(10)

    turtle.hideturtle()
    turtle.penup()

    #connect the last line
    turtle.setposition(0, .98)

    turtle.right(67.5)
    turtle.forward(200)

    turtle.right(85)
    turtle.forward(205)

    turtle.pendown()
    turtle.showturtle()

    turtle.right(87)
    turtle.forward(135)
    turtle.dot(10)


#Have the stars show up
def pagethree():
    window.bgpic("night.gif")
    turtle.color("white")
    window.bgcolor("#000033")
    turtle.hideturtle()
    turtle.penup()
    turtle.speed("slowest")
    turtle.goto(0.0, 0.98)
    turtle.write("Spica", align="right", font=("Arial",18))
    turtle.dot(20,"skyblue")

    turtle.goto(42.26,91.61)
    turtle.dot(10,"skyblue")

    turtle.goto(165.13,177.65)
    turtle.dot(20,"skyblue")
    turtle.write("Porrima", align="right", font=("Arial",18))

    turtle.goto(213.43,190.59)
    turtle.dot(10,"skyblue")

    turtle.goto(223.09,193.18)
    turtle.dot(10,"skyblue")

    turtle.goto(306.54,226.89)
    turtle.dot(10,"skyblue")

    turtle.goto(316.97,301.16)
    turtle.dot(10,"skyblue")

    turtle.goto(262.01,299.24)
    turtle.dot(10,"skyblue")

    turtle.goto(255.32,306.67)
    turtle.dot(10,"skyblue")

    turtle.goto(-149.91,-4.25)
    turtle.dot(10,"skyblue")

    turtle.goto(-176.40,38.15)
    turtle.dot(10,"skyblue")

    turtle.goto((-241.40,38.15))
    turtle.dot(10,"skyblue")

    turtle.goto((-241.40,38.15))
    turtle.dot(10,"skyblue")

    turtle.goto((-84.52,182.24))
    turtle.dot(10,"skyblue")

    turtle.goto((88.68,282.24))
    turtle.dot(10,"skyblue")

    turtle.goto((69.27,354.69))
    turtle.dot(10,"skyblue")

    turtle.goto(-232.24,208.29)
    turtle.dot(10,"skyblue")

    turtle.goto(-332.11,203.06)
    turtle.dot(10,"skyblue")

    turtle.goto(165.04,172.97)
    turtle.dot(10,"skyblue")


#Connect the stars and light them up
def pagefour():
    turtle.setposition(0,.98)
    turtle.pendown()
    turtle.color("skyblue")

    turtle.goto(0.0, 0.98)

    turtle.goto(42.26, 91.61)

    turtle.goto(165.13, 177.65)

    turtle.goto(213.43, 190.59)

    turtle.goto(223.09, 193.18)

    turtle.goto(306.54, 226.89)

    turtle.goto(316.97, 301.16)

    turtle.goto(262.01, 299.24)

    turtle.goto(255.32, 306.67)
    turtle.hideturtle()
    turtle.penup()

    #Next part
    turtle.setposition(0,.98)
    turtle.pendown()
    turtle.goto(-149.91, -4.25)

    turtle.goto(-176.40, 38.15)

    turtle.goto((-241.40, 38.15))

    turtle.goto((-241.40, 38.15))
    turtle.hideturtle()
    turtle.penup()

    #next part
    turtle.setposition(0, .98)
    turtle.pendown()
    turtle.goto(-84.52, 182.24)

    turtle.goto((88.68, 282.24))

    turtle.goto((69.27, 354.69))
    turtle.hideturtle()
    turtle.penup()

    #top left of spica
    turtle.setposition(0, .98)
    turtle.pendown()
    turtle.goto(-84.52,182.24)
    turtle.goto(-232.24, 208.29)
    turtle.goto(-332.11,203.06)
    turtle.hideturtle()
    turtle.penup()

    #last part
    turtle.setposition(0,.98)
    turtle.goto(-86.10,181.50)
    turtle.goto(90.53,285.54)
    turtle.pendown()
    turtle.goto(165.04,172.97)

splashpage()
time.sleep(5)
window.reset()
pageone()
time.sleep(5)
window.clear()
pageTwo()
time.sleep(5)
window.clear()
time.sleep(5)
pagethree()
pagefour()
time.sleep(5)

turtle.bye()
