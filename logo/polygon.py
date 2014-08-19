from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(1)
    turn(angle)
    
polygon(6,150)