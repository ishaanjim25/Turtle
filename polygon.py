import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(500,500)
polygon=turtle.Turtle()

n=int(input("Enter number of sides: "))
l=int(input("Enter the length of sides: "))
angle=360.0/n

for i in range(n):
    polygon.forward(l)
    polygon.right(angle)

turtle.done()
