from random import random, randint
from tealight.art import (color, line, spot, circle, box, image, text, background)

NumberOfBombs = 15
HLimit = 10
WLimit = 10
StartingX = 50
StartingY = 50
SquareSize = 50
OffsetX = 0
OffsetY = 0


BombArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
VisibleArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
VisibleArray[5][8] = 1


def PlaceBombs(NumberOfBombs):
  BombsPlaced = 0
  while BombsPlaced < NumberOfBombs + 1:
    x = randint(1,9)
    y = randint(1,9)
    if BombArray[x][y] == 0:
      BombArray[x][y] = -1
      BombsPlaced += 1
  
def DrawGrid():
  global OffsetX, OffsetY
  for x in range(0,HLimit):
    for y in range(0,WLimit):
      OffsetY += SquareSize
      if VisibleArray[x][y]==0:
        DrawCoveredSquare()
      elif VisibleArray[x][y] == 1:
        DrawUncoveredSquare()
      if BombArray[x][y] == -1:
        DrawMine(x,y)
    OffsetX += SquareSize
    OffsetY = 0
   
def DrawCoveredSquare():
  color("#cccccc")
  box(StartingX + OffsetX,StartingY + OffsetY,SquareSize,SquareSize)
  color("#757575")
  box(StartingX + (SquareSize * 0.1)/2 + OffsetX,StartingY + (SquareSize * 0.1)/2 + OffsetY,SquareSize * 0.9,SquareSize * 0.9)

def DrawUncoveredSquare():
  color("#757575")
  box(StartingX + OffsetX,StartingY + OffsetY,SquareSize,SquareSize)
  color("#cccccc")
  box(StartingX + (SquareSize * 0.1)/2 + OffsetX,StartingY + (SquareSize * 0.1)/2 + OffsetY,SquareSize * 0.9,SquareSize * 0.9)

def DrawMine(x,y):
  color("red")
  spot(StartingX + SquareSize * x + SquareSize * 0.5,StartingY + SquareSize * y + SquareSize * 0.5, 10)
  
  
PlaceBombs(NumberOfBombs)
DrawGrid()