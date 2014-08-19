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
  while i < distance:
    move()
    i += 1
    
Move(10)