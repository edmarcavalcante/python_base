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
    print("[Errpr] Missing name in the list.")
    sys.exit(1)