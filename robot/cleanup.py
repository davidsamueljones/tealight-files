from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

wallcount = 0

def MoveSearch(thing):
  global wallcount
  wallcount = 0
  distance = 1
  i = 0
  while i < distance:
    if touch() == thing:
      distance += 1
    i += 1
    if i < distance:
      move()

z = 0
while z < 512:
  z+=1
  if touch() == 'fruit':
    MoveSearch('fruit')
  elif left_side() == 'fruit':
    turn(-1)
  elif right_side() == 'fruit':
    turn(1)
  elif look() == 'wall' and wallcount < 4:
    turn(1)
    wallcount += 1
  elif look() == 'fruit':
    MoveSearch(None)