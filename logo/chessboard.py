from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(size):
  for i in range(0,size):
    turn(0)
    move(size)
    turn(90)
    move(1)
  
DrawBlackSquare(50)