from turtle import *




speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(100)  #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a left window
color("green")
left(30)
forward(85)

right(270)
forward(80)

right(270)
forward(70)

right(270)
forward(80)

right(180)
forward(40)

right(90)
forward(70)

right(90)
forward(40)

right(90)
forward(85)
#drawing right window
goto(200,200)
right(180)

forward(85)
right(90)

forward(80)
right(90)

forward(70)
left(270)

forward(83)
right(180)

forward(45)
right(270)

forward(70)
color("green")
right(270)
forward(40)

right(270)
# painting purple
color("purple")
forward(85)
right(270)

forward(200)

right(270)

forward(85)



#we want to paint a house
#step 1:  draw a square

exitonclick()


