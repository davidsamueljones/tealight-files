from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(edges,size):
  if size < 50:
    move(size)
    turn(90)
    stop = 0
  if size == 50:
    stop = 1
  
turn(-90)
DrawBlackSquare(12,20)