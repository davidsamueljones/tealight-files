from random import random, randint
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

def PlaceBombs(NumberOfBombs):
  BombsPlaced = 0
  while BombsPlaced < NumberOfBombs + 1:
    x = randint(0,9)
    y = randint(0,9)
    if BombArray[x][y] == 0:
      BombArray[x][y] = -1
      BombsPlaced += 1
  for x in range(0,HLimit):
    for y in range(0,WLimit):
      if BombArray[x][y] > -1:
        BombCheck(x,y)
  
def DrawGrid():
  global OffsetX, OffsetY
  OffsetX = 0
  OffsetY = 0
  for x in range(0,HLimit):
    for y in range(0,WLimit):
      if VisibleArray[x][y]==0:
        DrawCoveredSquare()
      elif VisibleArray[x][y] == 1:
        DrawUncoveredSquare()
        if BombArray[x][y] > 0:
          BombNumber = BombArray[x][y]
          DrawNumber(x,y,BombNumber)
        elif BombArray[x][y] == -1:
          DrawMine(x,y, "black")
      OffsetY += SquareSize
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

def DrawMine(x,y, colour):
  color(colour)
  x += 0.5
  y += 0.5
  spot(StartingX + SquareSize * x,StartingY + SquareSize * y, 10)

def DrawNumber(x,y,NumberOfMines):
  color("red")
  x += 0.35
  y += 0.25
  text(StartingX + SquareSize * x,StartingY + SquareSize * y, NumberOfMines)
  

def BombCheck(x,y):
  global BombArray
  BombCount = 0
  
  for (i,j) in [(x-1,y-1),(x-1,y), (x-1, y+1), (x,y-1), (x, y+1), (x+1,y-1),(x+1,y), (x+1, y+1)]:
  
    if (i >= 0 and i < WLimit and j >= 0 and j < HLimit):
      if BombArray[i][j] == -1:
        BombCount += 1  
  
  BombArray[x][y]=BombCount

def handle_mousedown(Mx,My, button):
  global lastx, lasty, VisibleArray, lost
  
  Mx = Mx - StartingX
  My = My - StartingY
  if lost == False:
    if button == "left":
    
      if 0 < Mx < SquareSize*WLimit: 
        if 0 < My < SquareSize*HLimit:
          i=Mx/SquareSize
          j=My/SquareSize
          print(i,j)
          lastx = i
          lasty = j
          VisibleArray[lastx][lasty] = 1
          IsBomb(lastx,lasty)
          DrawGrid()
          if lost == True:
               for x in range(0,HLimit):
                  for y in range(0,WLimit):
                    VisibleArray[x][y] = 1
                    DrawMine(50,50,"red")
        
def IsBomb(x,y):
  global lost
  if BombArray[x][y] == -1:
   lost = True
     
  
NumberOfBombs = 15
NumberOfBombsLeft = NumberOfBombs
HLimit = 10
WLimit = 10
SquareSize = 50
StartingX = screen_width /2 - SquareSize * WLimit/2
StartingY = 100
OffsetX = 0
OffsetY = 0
lastx = 0
lasty = 0
lost = False

BombArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
VisibleArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
PlaceBombs(NumberOfBombs)
DrawGrid()
