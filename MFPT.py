#!/usr/bin/python
from scipy.integrate import quad, dblquad
import numpy as np

k = 10
kb = 0.0019872041
T = 298
kbT = kb * T
beta = 1/kbT
D=1.0
delta = 1/12.0
xRange = 4

def potential(x):
    return k/4 * (x**2 - 1)**2

def inner(x):
  return np.exp(-beta * potential(x))

def outer(x):
  return np.exp(beta * potential(x))

def func(x, swap):
  a = np.inf * swap
  return outer(x) * quad(inner, a, x)[0]

def MFPT(x1, x2, D):
  if(x2>x1):
    swap = 1
  else:
    swap = -1
  return quad(func, x1, x2, args=(swap))[0]/D

#print MFPT(-1, 0, 1)

def findBot(x, delta, xRange):
  bins = xRange / (2 * delta)
  start = xRange / -2.0
  for i in range(int(bins)):
    start += 2 * delta
    if(start>x):
      return start - 2 * delta

def findTop(x, delta, xRange):
  bins = xRange / (2 * delta)
  start = xRange / -2.0
  for i in range(int(bins)):
    start += 2 * delta
    if(start>x):
      return start


def partition(x, bot, top):
  return inner(x)/quad(inner, bot, top)[0]

def intFunc(x1, x2, D):
  delta = 1/12.0
  xRange = 4
  bot1 = findBot(x1, delta, xRange)
  bot2 = findBot(x2, delta, xRange)
  top1 = findTop(x1, delta, xRange)
  top2 = findTop(x2, delta, xRange)
  part1 = partition(x1, bot1, top1)
  part2 = partition(x2, bot2, top2)
  part = part1*part2
  return part * MFPT(x1, x2, D)

def innerInt(xP, D, bot, top):#xP is the other x, i.e. xPrime
  return quad(intFunc, bot, top, args=(xP, D))[0]

def outerInt(D, botI, topI, botO, topO):
  return quad(innerInt, botO, topO, args=(D,botI,topI))


def bigIntegral(x1,x2, delta, xRange, D):
  bot1 = float(findBot(x1, delta, xRange))
  bot2 = float(findBot(x2, delta, xRange))
  top1 = float(findTop(x1, delta, xRange))
  top2 = float(findTop(x2, delta, xRange))

#  numerator = dblquad(lambda x1, x2: part * MFPT(x1, x2,D),bot1,top1, lambda x2: bot2, lambda x2: x1)
#  denominator = dblquad(lambda x2, x1: part * MFPT(x2, x1,D), bot2, top2, lambda x1: bot1, lambda x1: x2)
  numerator = outerInt(D, bot1, top1, bot2, top2)
  denominator = outerInt(D, bot2, top2, bot1, top1)
  print numerator, denominator
  return np.exp(-beta * numerator[0]) / np.exp(-beta * denominator[0])


print "Big Integral from -1 to 0", bigIntegral(-1.0, 0.0, delta, xRange, D)

print "Big Integral from -1 to 1", bigIntegral(-1.0, 1.0, delta, xRange, D)


#>>> from scipy.integrate import dblquad
#>>> area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)

