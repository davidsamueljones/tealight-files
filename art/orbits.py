from tealight.art import (color, line, spot, circle, box, image, text, background)
from math import sin, cos, pi

x = 400
y = 600
vx = 0
vy = 0
ax = 0
ay = 1

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 1
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  if x < 1 or x > 898:
    vx = -vx
  elif y < 1 or y > 1024:
    vy = -vy
    vy = vy * 0.9
  
  
  
  