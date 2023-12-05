from turtle import *
import colorsys
bgcolor("black")
pensize(3)
tracer(5)
speed(0)
setpos(-90, 80)

h =0.0
for i in range (9000):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    fd(1)
    rt(1)
    circle(100)
    h += 0.009
hideturtle()
done()

