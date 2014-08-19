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
  empty = False
  while i < distance and empty == False:
    move()
    i += 1
  if touch() == 'fruit':
    distance += 1
    
Move(0)