from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(size):
  for i in range(0,100):
    turn(0)
    move(size)
    turn(90)
    move(10)
    
DrawBlackSquare(50)