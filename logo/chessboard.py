from tealight.logo import (move, 
                           turn, 
                           color)

def DrawSquare(size):
  for i in range(0,4):
    move(size)
    turn(90)
    move(1)
    
def BlackenSquare(size):
  size = 50
  for i in range(0,50):
  size = size - 1
  DrawSquare(size)


  
DrawSquare(size)