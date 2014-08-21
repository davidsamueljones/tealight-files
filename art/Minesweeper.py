from random import random, randint

NumberOfBombs = 15
HLimit = 10
WLimit = 10
BombsPlaced = 0

BombArray = [[0 for x in range(HLimit)] for y in range(WLimit)]
VisibleArray = [[0 for x in range(HLimit)] for y in range(WLimit)]

while BombsPlaced < NumberOfBombs + 1:
  x = randint(0,9)
  y = randint(0,9)
  if BombArray[x][y] == 0:
    BombArray[x][y] = 1
    BombsPlaced += 1
  
  