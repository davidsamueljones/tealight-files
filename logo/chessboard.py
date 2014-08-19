from tealight.logo import (move, 
                           turn, 
                           color)

def DrawSquare(edges,size):
  move(size)
  turn(90)
  
turn(-90)
DrawSquare(12,150)