from getch import getch

def useblack(r, g, b):
  # 2.2 is gamma
  return (0.2126 * ((r/255) ** 2.2) + 0.7152 * ((g/255) ** 2.2) + 0.0722 * ((b/255) ** 2.2)) > 0.5
def rgb(r, g, b):
  return f"\033[{'1;38;5;16;' if useblack(r, g, b) else ''}48;2;{r};{g};{b}m"

def inputchar():
  char = getch()
  if char == '\x1b':
    char += getch()
    char += getch()
  return char

def intinput(text, error="Enter an integer"):
  try:
    return int(input(text))
  except:
    print(error)

def spinput(text="", default="", allowed=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), extra=None, end="\n", empty=""):
  total_allowed = (allowed := tuple(allowed) + (tuple(extra) if extra != None else ())) + ('\x7f', '\x1b', '\n')
  print(text + (input := default), end="", flush=True)
  pos = len(input)
  while True:
    char = ''
    while char not in total_allowed:
      try:
        char = getch()
      except:
        char = ''
    if char in allowed:
      pos += 1
      print(char + input[pos-1:] + f"\033[{len(input) - pos + (1 if pos < len(input)  else 0)}D", end="", flush=True)
      input = input[:pos-1] + char + input[pos-1:]
    elif char == '\x7f':
      if pos > 0:
        print("\b\033[K" + input[pos:] + f"\033[{len(input) - pos - (0 if pos < len (input) else 1)}D", end="", flush=True)
        pos -= 1
        input = input[:pos] + input[pos+1:]
    elif char == '\x1b':
      char += getch() + getch()
      if char == '\x1b[D':
        if pos > 0:
          print("\033[D", end="", flush=True)
          pos -= 1
      elif char == '\x1b[C':
        if pos < len(input):
          print("\033[C", end="", flush=True)
          pos += 1
    elif char == '\n':
      print(end=end)
      break
  if input == "":
    return empty
  return input