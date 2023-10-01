#from os import system
from time import perf_counter
import math
from getch import getch
from vectors import neg, add, sub, dot, cross, mag, magsqr, angle, rot, norm, mult, div

def intinput(text, default=None):
  while True:
    try:
      if default == None:
        return int(input(text))
      else:
        if (string := input(text)) == "":
          print("\033[F\033[2C" + str(default))
          return default
        else:
          return int(string)
    except:
      print("Enter an integer")

def createplane(centre, normal, width, height):
  up = mult([0, 0, 1] if normal == [0, 1, 0] else [0, 0, -1] if normal == [0, -1, 0] else norm(sub([0, 1, 0], mult(normal, dot(normal, [0, 1, 0])))), height/2)
  right = mult(norm(cross(up, normal)), width/2)
  x = add(sub(centre, up), right)
  y = add(sub(centre, right), up)
  return [sub(sub(centre, up), right), x, y]

def lineplaneintersect(line, plane):
  if type(plane) == list:
    linedir = sub(line[1], line[0])
    planex = sub(plane[1], plane[0])
    planey = sub(plane[2], plane[0])
    divisor = -dot(linedir, cross(planex, planey))
    diff = sub(line[0], plane[0])
    try:
      return [dot(cross(planex, planey), diff) / divisor, dot(cross(planey, neg(linedir)), diff) / divisor, dot(cross(neg(linedir), planex), diff) / divisor]
    except:
      return
  elif type(plane) == int:
    linedir = sub(line[1], line[0])
    divisor = -dot(linedir, cross(planexys[plane][0], planexys[plane][1]))
    diff = sub(line[0], planes[plane][0])
    try:
      return [dot(cross(planexys[plane][0], planexys[plane][1]), diff) / divisor, dot(cross(planexys[plane][1], neg(linedir)), diff) / divisor, dot(cross(neg(linedir), planexys[plane][0]), diff) / divisor]
    except:
      return

def brightness(line, plane):
  if len(plane if type(plane) == list else planes[plane]) == 2:
    if type(plane) == int: plane = planes[plane]
    diff = sub(line[0], plane[0])
    dunno = dot(norm(sub(line[1], line[0])), diff)
    if (solution := dunno**2 - magsqr(diff) + plane[1]**2) < 0: return 0
    distance = dunno + math.sqrt(solution)
    return 23+distance*unitmultiplier  if distance <= 0 else 0
  else:
    vals = lineplaneintersect(line, plane)
    return 0 if vals == None else 23 - vals[0]*multiplier if (0 <= vals[1] <= 1 and 0 <= vals[2] <= 1 and vals[0] >= 0) else 0

line = [[0, 0, 0], [0, 0, 2]]
plane = [[20, 20, 20], [30, 20, 20], [20, 40, 20]]
print("Controls:\nmovement - wasd\ncamera - arrow keys\ntry not to hold any of the keys or press them too quickly\notherwise a backlog is built up\n\nthe world wraps around so don't worry about getting lost by\nwandering into the all-emcompassing darkness\n")
size = intinput("\033[?25hEnter the size of the screen:\n(leave empty for 40 but depends on how laggy it is)\n(make sure you screen has been expanded enough or wierd stuff happens)\n> \033[93m", 40)
fov = 90
distance = (size/2) / math.tan(math.radians(fov/2))
unitmultiplier = 23 / (size/2)
multiplier = distance * unitmultiplier

up = ('w',)
down = ('s',)
left = ('a',)
right = ('d',)
turnup = ('\x1b[A',)
turndown = ('\x1b[B',)
turnleft = ('\x1b[D',)
turnright = ('\x1b[C',)
up_down = up + down
left_right = left + right
turn_up_down = turnup + turndown
turn_left_right = turnleft + turnright
accepted = up_down + left_right + turn_up_down + turn_left_right + ('\n',)

posx = size/8
posz = size/2
camyaw = 0
campitch = 0

edge = "░░"
print("\033[m\033[?25l" + edge*(size+2) + "\n" + (edge + "  "*size + edge + "\n")*size + edge*(size+2))
print(f"\033[{size+1}F\033[2C", end="")

planes = [
  createplane([size/2, size/2, size*11/16 - size/8], [0, 0, -1], size/4, size/4),
  createplane([size/2, size/2, size*11/16 + size/8], [0, 0, 1], size/4, size/4),
  createplane([size/2, size/2 - size/8, size*11/16], [0, -1, 0], size/4, size/4),
  createplane([size/2, size/2 + size/8, size*11/16], [0, 1, 0], size/4, size/4),
  [[size/2, size/2, size*5/16], size/8]
]
planexys = [[sub(x[1], x[0]), sub(x[2], x[0])] if len(x) == 3 else None for x in planes]

screen = []
planerot = 0
while True:
  start = perf_counter()
  old = screen
  screen = []
  planerot += 0.1
  screenplane = createplane(add([posx, size/2, posz], mult(rot(camyaw, campitch), distance)), rot(camyaw, campitch), size, size)
  #createplane([20 + 5 * math.sin(rot), 10, 20 + 5 * math.sin(rot)], [math.sin(rot), 0, math.cos(rot)], 20, 10)
  #[plane[0], [20 + 10 * math.sin(rot), plane[1][1], 20 + 5 * math.cos(rot)], plane[2]]
  
  planex = div(sub(screenplane[1], screenplane[0]), size)
  planey = div(sub(screenplane[2], screenplane[0]), size)
  for y in range(size, 0, -1):
    screen.append([])
    for x in range(size):
      line = [[posx, size/2, posz], add(add(screenplane[0], mult(planex, x)), mult(planey, y))]
      screen[size-y].append(max([brightness(line, x) for x in range(len(planes))]))
  
  stringscreen = ""
  for y in range(size, 0, -1):
    for x in range(size):
      stringscreen += "\033[2C" if old and old[size-y][x] == screen[size-y][x] else f"\033[48;5;{232+int(screen[size-y][x])}m  \033[m"
    stringscreen += "\033[E\033[2C"
  print(stringscreen + f"\033[{size+1}F{(str(perf_counter() - start) + '  ' + str(posx) + ', ' + str(posz) + '  ' + str(camyaw) + ', ' + str(campitch) + '  ' + str(brightness([[posx, size/2, posz], add(add(screenplane[0], mult(planex, 20)), mult(planey, 20))], 4))).ljust(70, ' ')}", end="", flush=True)
  start = perf_counter()
  #breakpoint()
  
  char = ''
  while char not in accepted:
    try:
      char = getch()
      if char == '\x1b':
        char += getch()
        char += getch()
    except:
      char = ''
  if char != None:
    if char in right:
      vec = rot((camyaw-90) % 360)
      posx = (posx + vec[0] + size/8) % ((5/4)*size) - size/8
      posz = (posz + vec[2] + size/8) % ((5/4)*size) - size/8
    elif char in left:
      vec = rot((camyaw+90) % 360)
      posx = (posx + vec[0] + size/8) % ((5/4)*size) - size/8
      posz = (posz + vec[2] + size/8) % ((5/4)*size) - size/8
    elif char in up:
      vec = rot((camyaw) % 360)
      posx = (posx + vec[0] + size/8) % ((5/4)*size) - size/8
      posz = (posz + vec[2] + size/8) % ((5/4)*size) - size/8
    elif char in down:
      vec = rot((camyaw+180) % 360)
      posx = (posx + vec[0] + size/8) % ((5/4)*size) - size/8
      posz = (posz + vec[2] + size/8) % ((5/4)*size) - size/8
    elif char in turn_left_right:
      camyaw = (camyaw + (5 if char in turnleft else -5)) % 360
    elif char in turn_up_down:
      campitch = campitch + (5 if char in turnup and campitch < 90 else -5 if campitch > -90 else 0)
  print("\033[E\033[2C", end="")



#█▐▌▄▀▓▒░
#╔═╗
#║0║
#╚═╝
# https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
# https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection