from tealight.logo import (move, 
                           turn, 
                           color)
size = 50
color = "red"

def DrawSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)
    
def DrawBlackSquare(size):
  for i in range(0,size):  
    DrawSquare(size)
    size = size - 1

turn(0)
for y in range(0,4):
  turn(180)
  move(size * 8)
  turn(-90)
  for y in range(0,4):
   size = 50
   DrawSquare(size)
   move(50)
   DrawBlackSquare(size)
   move(50)