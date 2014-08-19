from tealight.logo import move, turn

def polygon(edges, size):
  angle = 180.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    
polygon(6,150)