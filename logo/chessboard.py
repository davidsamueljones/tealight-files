from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(edges,size):
  for i in range(0,4):
    move(size)
    turn(90)
  
turn(-90)
DrawBlackSquare(12,50)