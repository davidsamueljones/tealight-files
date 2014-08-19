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
  distance = 0
  empty = False
  i = 0  
  while i < distance and empty == False:
    if touch() == 'fruit':
      distance += 1
    move()
    i += 1
    
    
MoveThroughFruit()
