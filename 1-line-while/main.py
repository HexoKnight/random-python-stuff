inp = ""
while inp != "hi":
  inp = input()

print("next")

print([x if (x := input()) == "hi" else print() for i in range(1000) if (x if "x" in globals() else "") != "hi"][-1])