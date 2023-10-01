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
      return current

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