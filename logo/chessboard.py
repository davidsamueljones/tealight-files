from tealight.logo import (move, 
                           turn, 
                           color)
size = 50

def DrawSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)
    
def DrawBlackSquare(size):
  size = 50
  for i in range(0,size):
    size = size - 1
    DrawSquare(size)

DrawBlackSquare(size)
move(size)
DrawSquare(size)