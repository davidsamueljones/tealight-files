from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, vertical, horizontal, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (horizontal * cos(angle))
    y0 = y + (vertical * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)
star(300, 300, "blue", 100,250, 50)
star(600, 400, "purple", 50,200, 100)
star(450, 200, "orange", 200,50, 30)