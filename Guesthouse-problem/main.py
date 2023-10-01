import math
import random

def checkPrime(i):
  isprime = True
  for x in range(2, int(math.sqrt(i) + 1)):
    if i % x == 0: 
      isprime = False
      break
  return isprime

def baseN(num,base):
  # I took this code from someone else and
  # subsequently don't really know how it works
  return ((num == 0) and digits[0]) or (baseN(num // base, base).lstrip(digits[0]) + digits[num % base])
def toRoomNumber(num):
  return baseN(num, 31).zfill(10)

def genCode(oldcode):
  return (secretnums[1] * oldcode + secretnums[0])%max

max = 31**10

print("-------------------------\n\033[1;91mWelcome to the Guesthouse\033[m\n-------------------------\n\n\033[96mThe next code for any given lock can be calculated with the old code and 2 secret numbers,\nwhich are the only 2 numbers that have to be permanently embedded in the locks' systems\n(other than its original starting number which is important only for syncing the\ntwo calculations at the start)\n\n\033[2;1mby the way, the calculation involves some use of polynomials\033[m")
yes = ["y", "yes"]
rand = input("\nIf starting values are not random, you will always get the exact same codes in the exact\nsame order for each room no matter when they are produced, however, obviously in an actual\nguesthouse all the stating codes and values would be random to prevent people from being\nable to predict the next code\n\nWould you like to use random starting codes and values? (y/n)\n(rather than the initial code for say room 7 being 0000000007)\n\033[91m>\033[m ").lower() in yes

#base 31 digits
digits = "0123456789abcdefghijklmnopqrstu"
roomcodes = []
if rand:
  secretnums = [random.randint(0, 31**10 - 1), random.randint(0, 31**10 - 1)]
else:
  secretnums = [123456789, 987654321]

for i in range(1, 200 + 1):
  if rand:
    temp = random.randint(0, 31**10 - 1)
    roomcodes.append([temp, genCode(temp)])
  else:
    roomcodes.append([i, genCode(i)])

while True:
  computer = False
  while True:
    try:
      cmd = input("\nChoose a room to unlock or open main computer: (1-200 for rooms, c for computer)\n\033[91m>\033[m ")
      if cmd.lower() == 'c':
        computer = True
        break
      room = int(cmd) - 1
      break
    except:
      print("Please enter a valid room number or c for computer")
  if not computer:
    while True:
      code = input("Please enter the code on the card:\n\033[91m>\033[m ")
      if [x for x in code if x not in digits] == [] and len(code) <= 10:
        code = int(code, 31)
        break
      print("Please enter a valid code")
    if roomcodes[room][0] == code:
      print("You unlocked the room!")
    elif roomcodes[room][1] == code:
      print("You unlocked the room and the code has now been changed!")
      roomcodes[room][0] = roomcodes[room][1]
      roomcodes[room][1] = genCode(roomcodes[room][1])
    else:
      print("That code is incorrect")
      print(roomcodes[room][0])
    print(toRoomNumber(roomcodes[0][1]))
  else:
    while True:
      try:
        room = int(input("\nChoose a room to check: (1-200)\n\033[91m>\033[m ")) - 1
        break
      except:
        print("Please enter a valid room number")
    print(f"the current code is {toRoomNumber(roomcodes[room][0])} and the next code will be {toRoomNumber(roomcodes[room][1])}\ngenerated with the algorithm\nf(x) = ({secretnums[1]}x + {secretnums[0]}) mod {max}\nand displayed in base 31, allowing for the next number to be generated pseudorandomly completely separately but completely accurately")