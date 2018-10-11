from turtle import*
screensize(600,300,"red")
penup()
goto(-350,200)
pendown()
color('yellow')
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
    end_fill()
penup()
goto(0,200)
pemdown()
begin_fill
while True:
    forward(150)
    right(144)
    if abs(pos())<10:
        break
    end_fill()
    penup
