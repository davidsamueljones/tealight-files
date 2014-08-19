from tealight.logo import (move, 
                           turn, 
                           color)

def DrawSquare(edges,size):
  for i in range(0,4):
    move(size)
    turn(90)
  
turn(-90)
DrawSquare(12,20)