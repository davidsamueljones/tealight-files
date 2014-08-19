from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)
    
def DrawWhiteSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)

size = 50
for i in range(0,50):
  size = size - 1
  DrawBlackSquare(size)
  
DrawWhiteSquare(size)