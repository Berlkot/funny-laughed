import turtle
import time
k = 20
turtle.color("black", "red")
turtle.speed(100)
turtle.left(90)
turtle.up()
turtle.begin_fill()
for i in range(12):
    turtle.forward(10 * k)
    turtle.right(60)
    turtle.forward(10 * k)
    turtle.right(120)
turtle.end_fill()
co = 0
turtle.up()
turtle.goto(-1000, -1000)
canvas = turtle.getcanvas()
print(canvas.find_all())
for i in range(5):
    canvas.delete(i)
canvas.update()   
for x in range(-100, 310, k):
    for y in range(-100, 310, k):
        canvas.create_line(x, y, x+1, y+1)
co = len(canvas.find_enclosed(*canvas.bbox(5)))
##for x in range(-100, 350, k):
##    for y in range(-100, 300, k):
##        s = canvas.find_overlapping(x,y, x, y)
##        if len(s) > 0:
##            print(s)
##        if len(s) == 1:
##            co += 1
print(co)
