from random import random, randint

NumberOfBombs = 10

BombArray = [[0 for x in range(10)] for x in range(10)]

for i in range(0,10)
x = randint(0,9)
y = randint(0,9)
BombArray[x][y] = 1

print BombArray[x][y]
print x
print y