from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
collectedfruit = 0

def MoveDefinedDistance(distance):
  i = 0
  while i < distance:
    move()
    i += 1
    
def MoveThroughFruit():
  global collectedfruit
  
  distance = 1
  i = 0
  while i < distance:
    if touch() == 'fruit':
      distance += 1
      i += 1
    if i < distance:
      move()
      collectedfruit += 1

z = 0
while z < 512:
  z+=1
  if touch() == 'fruit':
    MoveThroughFruit()
  elif left_side() == 'fruit':
    turn(-1)
  elif right_side() == 'fruit':
    turn(1)
