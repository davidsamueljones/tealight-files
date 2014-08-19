from tealight.logo import move, turn

def spiral(size + 2):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  spiral(size + 2)
  
spiral(0)