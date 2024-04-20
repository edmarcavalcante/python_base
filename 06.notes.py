"""Bloco de notas
$ notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre qualquer assunto

$ notes.py read tech
...
...

"""

__version__= "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

# valid command
cmds = ("read", "new")

if not arguments:
    print(f"You need pass argument: {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print("Argument invalid")
    sys.exit(1)

if arguments[0].lower == "new":
    title = arguments[1]
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text)+"\n")

if arguments[0] == "read":
    #leitura de notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-"*30)
            print()
