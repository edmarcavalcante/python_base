#!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
    print(f"Number of arguments incorrect. You need to pass three.")
    sys.exit(1)


operation, n1, n2 = arguments #desempacotamento

if operation not in ["sum","sub", "mul", "div"]:
    print(f"The first argument is invalid!\nChoose one of these: sum, sub, mul, div")
    sys.exit(1)

# TODO: CRIATE A VALIDATE NUMBER isdigit() 

validated_number = arguments[1:]

number_valided = []

for num in validated_number:

    if not num.replace(".", "").isdigit():
        print(f"Number invalided: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    number_valided.append(num)

n1, n2 = number_valided

calc = {
    "sum": n1 + n2,
    "sub": n1 - n2,
    "mul": n1 * n2,
    "div": n1 / n2,
}

print(f"RESULT OF OPERATION: " + str(calc[operation]))

print(arguments)