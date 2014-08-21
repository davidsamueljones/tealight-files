from random import random, randint
from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)

NumberOfBombs = 15
HLimit = 10
WLimit = 10

BombArray = [[0 for x in range(HLimit)] for y in range(WLimit)]
VisibleArray = [[0 for x in range(HLimit)] for y in range(WLimit)]

def PlaceBombs(NumberOfBombs):
  BombsPlaced = 0
  while BombsPlaced < NumberOfBombs + 1:
    x = randint(0,9)
    y = randint(0,9)
    if BombArray[x][y] == 0:
      BombArray[x][y] = 1
      BombsPlaced += 1
  
def DrawGrid():
  box(250,250,100,100)
  color("red")
  box(500,250,100,100)
  
PlaceBombs(NumberOfBombs)
DrawGrid()