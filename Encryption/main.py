import random
import math

def intinput(text, allowNone=False):
  while True:
    try:
      string = input(text)
      return None if not string and allowNone else int(string)
    except:
      print("Enter an integer")

def tochar(num):
  num %= 97
  if num == 95:
    return '£'
  if num == 96:
    return '¬'
  return chr(num + 32)
def tonum(char):
  if char == '£':
    return 95
  if char == '¬':
    return 96
  return (ord(char) - 32) % 97

def tostring(fullnum):
  string = ""
  for i in range(math.floor(math.log(fullnum, 97)) + 1):
    current = fullnum % 97**(i+1)
    fullnum -= current
    string = tochar(current // 97**i) + string
  return string
def tofullnum(string):
  fullnum = 0
  for i in range(len(string)):
    fullnum += tonum(string[-i-1]) * 97**i
  return fullnum

def nextprime(num):
  num += 1
  while True:
    for i in range(2, math.isqrt(num)):
      if (num % i) == 0:
        break
    else:
      break
    num += 1
  return num

def invmod(n, p):
  s, old_s = 0, 1
  r, old_r = p, n
  while r != 0:
    q = old_r // r
    new_r = old_r - q * r
    old_r = r
    r = new_r
    new_s = old_s - q * s
    old_s = s
    s = new_s
  return old_s % p

def polynomial(x, values, prime):
  result = 0
  for i in range(len(values)):
    result += x**i * values[i]
  return result % prime

def lagrange(x, xs, ys, prime):
  if len(xs) != len(ys):
    return
  if x != 0:
    result = 0
    for i in range(len(xs)):
      l = 1
      for j in range(len(xs)):
        if i != j:
          l *= (x - xs[j]) * invmod(xs[i] - xs[j], prime) % prime
      result += l * ys[i] % prime
  else:
    result = 0
    for i in range(len(xs)):
      product = 1
      for j in range(len(xs)):
        if i != j:
          product *= xs[j] * invmod(xs[j] - xs[i], prime) % prime
      result += product * ys[i] % prime
  return result % prime

prev_string = ""
prev_secret = 0
while True:
  if input("\033[mEnter 'y' to encode: \033[93m") == "y":
    print("\n---ENCODING---")
    strings = True
    if input("\033[mEnter 'y' to encode a number instead of a string: \033[93m") == "y":
      strings = False
      secret = intinput("\033[mEnter the secret to be encoded(leave empty for previous value):\n> \033[93m", True)
      if secret == None:
        print("\033[F\033[2C" + str(secret := prev_secret))
      prime = intinput("\033[mEnter the universal key\n(must be higher than the secret and prime or weird stuff happens)\n(leave empty for next highest prime):\n> \033[93m", True)
      if prime == None:
        print("\033[F\033[2C" + str(prime := nextprime(secret)))
    else:
      string = input("\033[mEnter the secret to be encoded(leave empty for previous value):\n> \033[93m")
      if string == "":
        print("\033[F\033[2C" + prev_string + "\n" + str(secret := prev_secret))
      else:
        secret = 0
        for i in range(len(string)):
          secret += tonum(string[-i-1]) * 97**i
        print(secret)
      prime = intinput("\033[mEnter the universal key\n(must be higher than the secret and prime or weird stuff happens)\n(leave empty for perect prime):\n> \033[93m", True)
      if prime == None:
        print("\033[F\033[2C" + str(prime := 97**(len(string) + 1)))
    reqkeys = intinput("\033[mEnter the number of keys required:\n> \033[93m")
    numkeys = intinput("\033[mEnter the number of keys to make\n(preferably more than the amount required):\n> \033[93m")
    extra = [random.randrange(prime) for x in range(reqkeys - 1)]
    if input("\033[mEnter 'y' to manually enter other integer values: \033[93m") == "y":
      print("\033[mEnter other integer values one at a time\n(leave empty for random value):")
      for i in range(reqkeys - 1):
        if (inp := intinput("\033[m> \033[93m", True)) != None:
          extra[i] = inp
    points = {}
    for i in range(1, numkeys + 1):
      points[i] = polynomial(i, [secret] + extra, prime)
    fill = math.floor(math.log10(numkeys)) + 1
    for point in points:
      print(f"\033[96m{str(point).ljust(fill)} : '{tostring(points[point]) if strings else points[point]}'\033[m")
    print()
  else:
    print("\n---DECODING---")
    strings = True
    if input("\033[mEnter 'y' to decode a number instead of a string: \033[93m") == "y":
      strings = False
      prime = intinput("\033[mEnter the universal key:\n> \033[93m")
      print("\033[mEnter keys one at a time(leave empty to stop):")
      keys = {}
      while True:
        key = intinput("\033[mkey  > \033[93m", True)
        if key == None:
          break
        keys[key] = intinput("\033[mvalue> \033[93m")
      print(f"\033[mThe secret was:\n\033[96m{str(lagrange(0, list(keys.keys()), list(keys.values()), prime))}\033[m\n")
    else:
      print("\033[mEnter keys one at a time(leave empty to stop):")
      keys = {}
      while True:
        key = intinput("\033[mkey  > \033[93m", True)
        if key == None:
          break
        keys[key] = input("\033[mvalue> \033[93m")
      prime = intinput("\033[mEnter the universal key\n(leave empty for automatic, which should be correct\nunless keys have been altered or whitespace omitted):\n> \033[93m", True)
      if prime == None:
        length = 0
        for i in keys.values():
          length = max(length, len(i))
        print("\033[F\033[2C" + str(prime := 97**length))
      print(f"\033[mThe secret was:\n\033[96m{tostring(lagrange(0, list(keys.keys()), [tofullnum(x) for x in keys.values()], prime))}\033[m\n")
    # perhaps the keys in strings could be the keys for the (prime mod length) character
    # each character could be a prime number then the prime could be (char**length), basically base 95(but obviously prime)