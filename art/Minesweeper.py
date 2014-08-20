from random import random, randint

NumberOfBombs = 10
BombsPlaced = 0
BombArray = [[0 for x in range(10)] for x in range(10)]

while BombsPlaced < NumberOfBombs + 1:
  x = randint(0,9)
  y = randint(0,9)
  if BombArray[x][y] = 0
    BombArray[x][y] = 1
    BombsPlaced += 1
  
  

print BombArray[x][y]
print x
print y