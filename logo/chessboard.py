from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(10)
    size - 5
 
size = 50
for i in range(0,55):
  size = size - 1
  DrawBlackSquare(size)