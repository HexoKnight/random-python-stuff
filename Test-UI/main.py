import selopt

print(selopt.selopt(["hi", "hello", "bye", "goodbye"]))
print(selopt.selintopt(["hi", "hello", "bye", "goodbye"], align=True, dict=True, default=5, defaults=[1, 2]))