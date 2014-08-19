from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(edges,size):
  for i in range(0,20):
    turn(0)
    move(size)
    turn(90)
    move(1)
  
DrawBlackSquare(12,20)