import os
import sys

# LBYL - Look Before You Leap


if os.path.exists("names.txt"):
    names = list(open("names.txt", "r"))
    print(names)
    

else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list.")
    

# EAFP - Easy to Ask Forgiveness than Permission
print("***********")


try:
    names_ = open("names.txt") # FileNotFoundError
    lines = names_.readlines()
    2 / 1 # Zero DivisionError
    print(lines[2]) #
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("Not is permission division by 0.")
    sys.exit(1)
except IndexError:
    print("IndexError: list index out of range")
    sys.exit(1)


for _ in lines:
    print(_)