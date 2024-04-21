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
print(arguments)
# valid command
cmds = ("read", "new")

if not arguments:
    print(f"You need pass argument: {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print("Argument invalid")
    #sys.exit(1)
print(arguments[0])
if arguments[0] == "new":
    try:
        print("Dentro do loop")
        title = arguments[1]
    except IndexError as e:
        print(str(e))
        title = input("Type the title: ")
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
        #TODO: fazer um try/except para verificar se já existe a tag no bloco de notas 
        try:
            if tag.strip().lower() == arguments[1].lower():
                print(f"title: {title}")
                print(f"text: {text}")
                print("-"*30)
                print()
        except IndexError as e:
            print(str(e))

