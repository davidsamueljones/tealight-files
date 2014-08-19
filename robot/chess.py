from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Move set amount
def Move(distance):
  i = 0
  empty = false
  while i < distance and empty == False:
    move()
    i += 1
    
Move(10)