from turtle import *
import math
import random
import time

#dots = 0
#dottime = time.time()
def createdot(pos, size=None):
  if size == None:
    #global dots, dottime
    setpos(pos)
    dot(dotsize)
    #dots += 1
    #if dots > 100:
    #  print(time.time() - dottime)
    #  dots = 0
    #  dottime = time.time()
    #global dots, dottime
    #dots.append(pos)
    #if len(dots) > 100:
    #  for i in dots:
    #    setpos(i)
    #    dot(dotsize)
    #  dots = []
    #  print(time.time() - dottime)
    #  dots = []
    #  dottime = time.time()
  else:
    setpos(pos)
    dot(size)

def interpolate(posa, posb, ratio):
  return (posa[0] + ratio * (posb[0] - posa[0]), posa[1] + ratio * (posb[1] - posa[1]))

def choosenewpoint(currentp, currenti):
  newp = [0, 0]
  while newp == [0, 0] or not validpoint(newp, currentp):
    newi = -1
    while newi == -1 or not validindex(newi, currenti):
      newi = float(random.randint(0, 2 * n - 1)) / 2 if midpoints else random.randint(0, n - 1)
    newp = interpolate(currentp, points[int(newi)] if round(newi) == newi else midpointpoints[int(newi)], ratio)
  return newp, newi

#----v----v----v----EDIT THESE VALUES----v----v----v----

size = 300 # the size of the canvas

vertexsize = size/40 # the size of the dot at each vertex
dotsize = size/200 # the size of each dot

vertices = True # whether to show the vertices or not
sides = False # whether to show the sides or not

randompoints = True # whether the points are random (generally this should be true)
maxdepth = 5 # the number of times new points are generated from old points if the points are not random (0 for infinite)

midpoints = False # whether to allow points to jumps to the midpoints of sides as well

n = 3 # the number of vertices
rat,io = 1, 2#(1+math.sqrt(5))/2 # the ratio of the distance for a point to travel to the distance from that point to the chosen vertex

validindex = lambda index, old : True#index != (old+2)%n # whether to accept a chosen index(midpoints are .5s)
validpoint = lambda point, old : True # whether to accept a chosen point

# ----v----UNCOMMENT TO ENABLE PRESET----v----

# serpinski triangle (default)
#midpoints,n,rat,io,validindex,validpoint=False,3,1,2,lambda index,old:True,lambda point,old:True

# serpinski carpet
#midpoints,n,rat,io,validindex,validpoint=True,4,2,3,lambda index,old:True,lambda point,old:True

# cool but takes a while
#midpoints,n,rat,io,validindex,validpoint=False,7,1,2,lambda index,old:not(old-index)%7in(1,3,4,6),lambda point,old:True

# also cool but also takes a while
#midpoints,n,rat,io,validindex,validpoint=False,7,1,2,lambda index,old:not(old-index)%7in(1,2,5,6),lambda point,old:True


# https://en.wikipedia.org/wiki/Chaos_game
# a beutiful version: http://andrew.wang-hoyer.com/experiments/chaos-game

#----^----^----^----EDIT THESE VALUES----^----^----^----

Screen().setup(size*2.5, size*2.5)
up()
hideturtle()
speed(0)

ratio = float(rat)/float(io)
points = []
for i in range(n):
  points.append((size * math.cos(2 * math.pi * (i + 0.5) / n - math.pi/2), size * math.sin(2 * math.pi * (i + 0.5) / n - math.pi/2)))
  if vertices: createdot(points[i], vertexsize)
if midpoints:
  midpointpoints = []
  for i in range(n):
    midpointpoints.append(interpolate(points[i], points[(i + 1)%n], 0.5))
  bothpoints = []
  for i in range(2 * n):
    bothpoints.append(points[i/2] if i%2 == 0 else midpointpoints[i/2])

if sides:
  setpos(points[0])
  down()
  for i in range(n):
    setpos(points[(i+1)%n])
  up()

if randompoints:
  pos = (random.randint(-size, size), random.randint(-size, size))
  setpos(pos)
  
  new = -1
  while True:
    old = new
    pos, new = choosenewpoint(pos, old)
    createdot(pos)
else:
  poses = [(interpolate(bothpoints[x], bothpoints[(x+1)%n], 0.5), -1) for x in range(2 * n)] if midpoints else [(interpolate(points[x], points[(x+1)%n], 0.5), -1) for x in range(n)]
  for i in poses: createdot(i[0])
  depth = 0
  while maxdepth <= 0 or depth < maxdepth:
    newposes = []
    for i in poses:
      if midpoints:
        for j in range(2 * n):
          nj = float(j)/2
          if validindex(nj, i[1]):
            pos = interpolate(i[0], bothpoints[j], ratio)
            if validpoint(pos, i[0]):
              newposes.append((pos, nj))
              createdot(pos)
      else:
        for j in range(n):
          if validindex(j, i[1]):
            pos = interpolate(i[0], points[j], ratio)
            if validpoint(pos, i[0]):
              newposes.append((pos, j))
              createdot(pos)
    poses = newposes
    depth += 1