from getch import getch

def inputchar():
  try:
    char = getch()
  except:
    char = ''
  if char == '\x1b':
    char += getch()
    char += getch()
  return char

accepted = ('a', 'd', '\x1b[C', '\x1b[D', '\n')
def selopt(options, fill=' ', fillnum=4, retval=False, start="", end=""):
  if not hasattr(options, 'index'):
    raise TypeError("Parameter 'options' must be indexable")
  if not hasattr(fill, '__str__') or (hasattr(fill, '__index__') and not all([hasattr(x, '__str__') for x in fill])):
    raise TypeError("Parameter 'fill' must be a string or stringable or indexable of strings or stringables")
  if not hasattr(fillnum, '__int__'):
    raise TypeError("Parameter 'fillnum' must be an integer or intergerable")
  if not hasattr(retval, '__bool__'):
    raise TypeError("Parameter 'retval'(return_value) must be a boolean or booleanable")
  if not hasattr(start, '__str__'):
    raise TypeError("Parameter 'start' must be a string or stringable")
  if not hasattr(end, '__str__'):
    raise TypeError("Parameter 'end' must be a string or stringable")

  print("\033[?25l", end="")
  current = 0
  while True:
    print("\r" + start, end="")
    for i in range(len(options)):
      if i == current:
        print("\033[1;7m", end="")
      print(options[i], end="")
      if i == current:
        print("\033[m", end="")
      if i < len(options) - 1:
        print((str(fill) * int(fillnum)) if hasattr(fill, '__str__') and (not hasattr(fill, '__index__') and type(fill) == str) else fill[i % len(fill)], end="")
    print(end, end="", flush=True)

    char = ''
    while char not in accepted:
      char = inputchar()

    #if char == '\x1b[A' or char == 'w':
    #if char == '\x1b[B' or char == 's':
    if char == '\x1b[C' or char == 'd':
      current = (current + 1) % len(options)
    elif char == '\x1b[D' or char == 'a':
      current = (current - 1) % len(options)
    elif char == '\n':
      print("\033[?25h")
      if bool(retval):
        return options[current]
      return current

'''def seltblopt(options, fill=' ', fillnum=4, retval=False, start="", end=""):
  if not hasattr(options, 'index'):
    raise TypeError("Parameter 'options' must be indexable")
  for i in options:
    if not hasattr(options[i], 'index'):
      raise TypeError("Parameter 'options' must have indexable elements")
  if not hasattr(fill, '__str__'):
    raise TypeError("Parameter 'fill' must be a string or stringable")
  if not hasattr(fillnum, '__int__'):
    raise TypeError("Parameter 'fillnum' must be an integer or intergerable")
  if not hasattr(retval, '__bool__'):
    raise TypeError("Parameter 'retval'(return_value) must be a boolean or booleanable")
  if not hasattr(start, '__str__'):
    raise TypeError("Parameter 'start' must be a string or stringable")
  if not hasattr(end, '__str__'):
    raise TypeError("Parameter 'end' must be a string or stringable")

  print("\033[?25l", end="")
  up = ('w', '\x1b[A')
  down = ('s', '\x1b[B')
  left = ('a', '\x1b[D')
  right = ('d', '\x1b[C')
  accepted = up + down + left + right + ('\n',)
  current = 0
  while True:
    print("\r" + start, end="")
    for i in range(len(options)):
      if i == current:
        print("\033[1;7m", end="", flush=True)
      print(options[i], end="", flush=True)
      if i == current:
        print("\033[m", end="", flush=True)
      if i < len(options) - 1:
        print(str(fill) * int(fillnum), end="", flush=True)
    print(end, end="")

    char = ''
    while char not in accepted:
      char = inputchar()

    #if char == '\x1b[A' or char == 'w':
    #if char == '\x1b[B' or char == 's':
    if char == '\x1b[C' or char == 'd':
      current = (current + 1) % len(options)
    elif char == '\x1b[D' or char == 'a':
      current = (current - 1) % len(options)
    elif char == '\n':
      print("\033[?25h")
      if bool(retval):
        return options[current]
      return current'''

from os import listdir, system
from importlib import reload
from sys import modules

def runselfile(clear=True, notinclude=["main", "selopt"], fill=' ', fillnum=4, start="", end=""):
  if not hasattr(clear, '__bool__'):
    raise TypeError("Parameter 'clear' must be a boolean or booleanable")
  if not hasattr(notinclude, '__iter__'):
    raise TypeError("Parameter 'notinclude' must be iterable")
  if not hasattr(fill, '__str__'):
    raise TypeError("Parameter 'fill' must be a string or stringable")
  if not hasattr(fillnum, '__int__'):
    raise TypeError("Parameter 'fillnum' must be an integer or intergerable")
  if not hasattr(start, '__str__'):
    raise TypeError("Parameter 'start' must be a string or stringable")
  if not hasattr(end, '__str__'):
    raise TypeError("Parameter 'end' must be a string or stringable")
  
  if (file := selopt([x[:-3] for x in listdir() if x[-3:] == ".py" and x[:-3] not in notinclude], retval=True, fill=fill, fillnum=fillnum, start=start, end=end)) in modules:
    if clear: system("clear")
    reload(modules[file])
  else:
    if clear: system("clear")
    __import__(file)

def selintopt(options, defaults=None, default=0, mid=": ", align=False, fill=None, minval=0, maxval=None, wrap=False, dict=False):
  if not hasattr(options, 'index'):
    raise TypeError("Parameter 'options' must be indexable")
  if defaults != None and not hasattr(defaults, 'index'):
    raise TypeError("Parameter 'defaults' must be indexable")
  if not hasattr(default, '__int__'):
    raise TypeError("Parameter 'default' must be an integer or intergerable")
  if not hasattr(mid, '__str__'):
    raise TypeError("Parameter 'mid' must be a string or stringable")
  if fill != None and not hasattr(fill, '__int__'):
    raise TypeError("Parameter 'fill' must be an integer or intergerable")
  if not hasattr(align, '__bool__'):
    raise TypeError("Parameter 'align' must be a boolean or booleanable")
  if minval != None and not hasattr(minval, '__int__'):
    raise TypeError("Parameter 'minval' must be an integer or intergerable")
  if maxval != None and not hasattr(maxval, '__int__'):
    raise TypeError("Parameter 'maxval' must be an integer or intergerable")
  if not hasattr(wrap, '__bool__'):
    raise TypeError("Parameter 'wrap' must be a boolean or booleanable")
  if not hasattr(dict, '__bool__'):
    raise TypeError("Parameter 'dict' must be a boolean or booleanable")
  
  if align:
    fill = max(fill, max([len(x) for x in options]) + len(mid)) if fill != None else max([len(x) for x in options]) + len(mid)
  print("\033[?25l", end="")
  up = ('w', '\x1b[A')
  down = ('s', '\x1b[B')
  left = ('a', '\x1b[D')
  right = ('d', '\x1b[C')
  accepted = up + down + left + right + ('\n',)
  optints = [(defaults[x] if defaults != None and len(defaults) > x else default) for x in range(len(options))]
  current = 0
  for i in range(len(options)):
    print("\n" + options[i] + str(mid) + f"\033[{fill + 1 if align else len(str(options[current]) + str(mid)) + 1}G" + ("\033[1;7m" if i == current else "") + str(optints[i]) + ("\033[m" if i == current else ""), end="")
  print(f"\033[{len(options)-1}A", end="", flush=True)
  while True:
    char = ''
    while char not in accepted:
      try:
        char = getch()
      except:
        char = ''
      if char == '\x1b':
        char += getch()
        char += getch()
    if char in up or char in down:
      print(f"\033[{fill + 1 if align else len(str(options[current]) + str(mid)) + 1}G\033[K" + str(optints[current]), end="")
      old = current
      current = (current + (-1 if char in up else 1)) % len(options)
      movement = str(old - current) + "A" if old > current else str(current - old) + "B"
      print(f"\033[{fill + 1 if align else len(str(options[current]) + str(mid)) + 1}G\033[{movement}\033[K\033[1;7m" + str(optints[current]) + "\033[m", end="", flush=True)
    elif char in left or char in right:
      if wrap and minval != None and maxval != None:
        optints[current] = (optints[current] + (-1 if char in left else 1) - minval) % (maxval + 1) + minval
      else:
        val = optints[current] + (-1 if char in left else 1)
        if minval == None:
          if maxval == None:
            optints[current] = val
          else:
            optints[current] = min(val, maxval)
        else:
          val = max(val, minval)
          if maxval == None:
            optints[current] = val
          else:
            optints[current] = min(val, maxval)
      print(f"\033[{fill + 1 if align else len(str(options[current]) + str(mid)) + 1}G\033[K\033[m\033[1;7m" + str(optints[current]) + "\033[m", end="", flush=True)
    elif char == "\n":
      print(f"\033[{fill + 1 if align else len(str(options[current]) + str(mid)) + 1}G\033[K{str(optints[current])}\033[{len(options) - current}E\033[?25h", end="")
      return {options[x]:optints[x] for x in range(len(options))} if dict else optints