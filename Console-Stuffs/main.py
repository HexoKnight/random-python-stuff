from os import system
from getch import getch
def useblack(r, g, b):
  GAMMA = 2.2
  return (0.2126 * ((r/255) ** GAMMA) + 0.7152 * ((g/255) ** GAMMA) + 0.0722 * ((b/255) ** GAMMA)) > 0.5

escape_sequences = {
  r"\n": r"newline(\f\r)",
  r"\f": "down a line(formfeed)",
  r"\r": "carriage return",
  r"\t": "tab",
  r"\b": "backspace",
  r"\***": "character with octal value '***'",
  r"\**": "character with hex value '**'",
  r"\uEEA7": "replit arrow(\uEEA7)",
  r"\033[33m\\uEEA7\\033[m": "replit arrow with colour(\033[33m\uEEA7\033[m)",
  r"\033[*$": "special code with type '$' and value '*'(defaults to 0), usually separated by ';'"
}
special_codes = {
  "*A": "cursor up, * = number of characters",
  "*B": "cursor down, * = number of characters",
  "*C": "cursor right, * = number of characters",
  "*D": "cursor left, * = number of characters",
  "*E": "cursor start of next line, * = number of lines",
  "*F": "cursor start of previous line, * = number of lines",
  "*G": "cursor to column *(starting at 1)",
  "*;*H": "move cursor to '{row};{column}' starting at 1",
  "*J": "clear everything (0=after, 1=before, 2=everything) but leave cursor untouched",
  "*K": "clear line (0=after, 1=before, 2=everything) but leave cursor untouched",
  "*S": "move everyting up by * lines",
  "*T": "move everyting down by * lines",
  "?25l": "hide cursor",
  "?25h": "show cursor",
  "s": "saves cursor position",
  "u": "restores cursor position",
  "6n": "reports cursor postion(as though typed) in format '\\033[{row};{column}R'",
  "*m": "special text formatting, * = code, separated by ';', eg.'1;5;31'"
}
print("\033[?25l", end="")
system("clear")
for i in escape_sequences.keys():
  print(i + " - " + escape_sequences[i])
print()
for i in special_codes.keys():
  print(i + " - " + special_codes[i])
print()#"\033[10;10H\033[u", end="", flush=True)

print("\033[1;4mSpecial text formatting aka SGR(Select Graphic Rendition)\033[m\n")
print("\033[4m'\\033[*m' (regular text formatting and colours)\033[m")
for i in range(0, 110, 10):
  text = ""
  for j in range(10):
    text += f"\033[{i+j}m{format(i+j, '4d')}\033[m"
  print(text)

print("\n\033[4m'\\033[{3/4}8;5;*m' (8-bit foreground/background colours)\033[m")
show_text = input("Enter 'y' to disable text: ").lower() != 'y'
show_num = input("Enter 'y' to disable numbers: ").lower() != 'y'
if show_text:
  print("\n0-15 are the default colours (1 is for errors)")
text = ""
for i in range(0, 8):
  text += f"\033[48;5;{i}m{format(i, '4d') if show_num else '    '}\033[m"
print(text)
text = ""
for i in range(0, 8):
  text += f"\033[1;38;5;16;48;5;{8+i}m{format(8+i, '4d') if show_num else '    '}\033[m"
print(text)
if show_text:
  print("16-231 is a colour cube with each dimension representing a different colour,\nunfortunately, this display is only 2D\neach colour can be calculated from rgb values from 0 to 5 with this formula:\n16 + \033[38;5;196m(36*r)\033[m + \033[38;5;46m(6*g)\033[m + \033[38;5;21m(b)\033[m")
for i in range(0, 216, 36):
  text = ""
  for j in range(6):
    text += f"\033[48;5;{16+i+j}m{format(16+i+j, '4d') if show_num else '    '}\033[m"
  for j in range(6, 12):
    text += f"\033[48;5;{16+i+j}m{format(16+i+j, '4d') if show_num else '    '}\033[m"
  for j in range(12, 18):
    text += f"\033[48;5;{16+i+j}m{format(16+i+j, '4d') if show_num else '    '}\033[m"
  print(text)
for i in range(0, 216, 36):
  text = ""
  for j in range(6):
    text += f"\033[1;38;5;16;48;5;{34+i+j}m{format(34+i+j, '4d') if show_num else '    '}\033[m"
  for j in range(6, 12):
    text += f"\033[1;38;5;16;48;5;{34+i+j}m{format(34+i+j, '4d') if show_num else '    '}\033[m"
  for j in range(12, 18):
    text += f"\033[1;38;5;16;48;5;{34+i+j}m{format(34+i+j, '4d') if show_num else '    '}\033[m"
  print(text)
if show_text:
  print("232-255 is a grayscale from black to white in 24 steps")
text = ""
for i in range(0, 12):
  text += f"\033[48;5;{232+i}m{format(232+i, '4d') if show_num else '    '}\033[m"
print(text)
text = ""
for i in range(0, 12):
  text += f"\033[1;38;5;16;48;5;{244+i}m{format(244+i, '4d') if show_num else '    '}\033[m"
print(text)

print("\n\033[4m'\\033[{3/4}8;2;*;*;*m' (24-bit foreground/background rgb colours)\033[m\n(arrow keys and wasd)")
up_down = ('w', 's', '\x1b[A', '\x1b[B')
left_right = ('a', 'd', '\x1b[D', '\x1b[C')
accepted = ('w', 'a', 's', 'd', '\x1b[A', '\x1b[B', '\x1b[C', '\x1b[D', '\n')
rgb = [0, 0, 0]
rgb_text = ("red:  ", "green:", "blue: ")
all = "  RGB  "
current = 0
print(all, end="")
for i in range(3):
  print("\n" + rgb_text[i] + ("\033[1;7m" if i == current else "") + str(rgb[i]) + ("\033[m" if i == current else ""), end="")
print(f"\033[{3-1}A", end="", flush=True)
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
  if char in up_down:
    print("\033[7G\033[K" + str(rgb[current]) + "", end="")
    old = current
    current = (current + (-1 if char == 'w' or char == '\x1b[A' else 1)) % 3
    movement = str(old - current) + "A" if old > current else str(current - old) + "B"
    print(f"\033[7G\033[{movement}\033[K\033[1;7m" + str(rgb[current]) + "\033[m", end="", flush=True)
  elif char in left_right:
    rgb[current] = (rgb[current] + (-1 if char == 'a' or char == '\x1b[D' else 1)) % 256
    print(f"\033[G\033[{'1;38;5;16;' if useblack(rgb[current] if current == 0 else 0,rgb[current] if current == 1 else 0,rgb[current] if current == 2 else 0) else ''}48;2;{rgb[current] if current == 0 else '0'};{rgb[current] if current == 1 else '0'};{rgb[current] if current == 2 else '0'}m" + rgb_text[current] + "\033[m\033[K\033[m\033[1;7m" + str(rgb[current]) + f"\033[m\033[s\033[{'1;38;5;16;' if useblack(rgb[0],rgb[1],rgb[2]) else ''}48;2;{rgb[0]};{rgb[1]};{rgb[2]}m\033[{current + 1}F{all}\033[u", end="", flush=True)