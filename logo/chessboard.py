from tealight.logo import (move, 
                           turn, 
                           color)

def DrawSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)
    
def DrawBlackSquare(size):
  size = 50
  for i in range(0,50):
    size = size - 1
    DrawSquare(size)

DrawBlackSquare(50)
move(50)
DrawSquare(50)