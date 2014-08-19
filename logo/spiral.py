from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(50)
  spiral(size + 5)
  
spiral(0)