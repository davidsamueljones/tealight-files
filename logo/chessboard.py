from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(edges,size):
  if size < 50:
    move(size)
    turn(90)
    stop = false
  if size == 50:
    stop = true
  
turn(-90)
DrawBlackSquare(12,20)