from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Move set amount
def Move(distance):
  while i <= distance:
    move()
    
Move(10)