from tealight.logo import (move, 
                           turn, 
                           color)

def DrawBlackSquare(size):
  for i in range(0,100):
    move(size)
    turn = 90
    move(10)
    turn(90)
  
DrawBlackSquare(50)