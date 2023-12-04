from turtle import*
import colorsys
bgcolor ("black")
width(2)
h=0.0
for i in range(500):
     speed=(10000)
     c=colorsys.hsv_to_rgb(h,1,1)
     color (c)
     forward(i*1)
     right (300) 
     h+=0.02
done()