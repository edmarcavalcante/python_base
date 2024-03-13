"""
Script that print "Hello World" consider
the argument passed by user
ex:
>> python hello.py --leng=pt_br count=2
>> Olá, Mundo!
>> Olá, Mundo!

"""

__version__ = "0.1.3"
__author__ = "Edmar Almeida"
__license__= "Unlicense"

import os
import sys

print(os.getenv("LANG"))
print(os.getenv("LANG")[:5])
print(sys.argv) # Retorna uma lista com os argumentos passados
"""
>python 03_project.py --Edmar --Almeida
['.\\03_project.py', '--Edmar', 'Almeida'] - lista com 3 argumentos

"""

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: usar repetição
    if current_language is None:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!", 
}

print(msg[current_language] * int(arguments["count"]))