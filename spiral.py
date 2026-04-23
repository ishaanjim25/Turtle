import turtle
turtle.bgcolor("white")
colors=["red","yellow","black","blue","green","orange"]
line=turtle.Pen()

for x in range(360):
    line.pencolor(colors[x%6])
    line.width(x/100+1)
    line.forward(x)
    line.left(59)
