from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Move set amount
def MoveDefinedDistance(distance):
  i = 0
  while i < distance:
    move()
    i += 1
    
def MoveThroughFruit():
  if touch() == 'fruit':
      distance = 1
  i = 0  
  while i < distance:
    if touch() == 'fruit':
      distance += 1
    move()
    i += 1
    
    
MoveThroughFruit()
