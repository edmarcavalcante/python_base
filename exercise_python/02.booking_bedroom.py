"""
Create a program in terminal that show to the users a list of
the bedrooms availabe for rent and the price each of them. This 
informations are in file.txt separete for comma.
'quartos.txt'
# código, nome, preço
1,Suite Master,500
2,Quarto Família,200
3,Quarto Single,100
4,Quarto Simples,50

The program ask to users the name, number of the bedroom wich will be rent
and the number of the days. In the final, show the estimate price to be payied.

The program should save the choice in another file containing the reservations.

'reservas.txt'
# cliente, quarto, dias
Edmar,3,12

if another user try reserve the same bedroom, the program should show a mensage
informing that the bedrooms is already occupied 
"""
import sys
import os

available = {}
with open("quartos.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        Codigo, nome, preco = line.strip().split(",")
        available[int(Codigo)] = {
            "name":nome,
            "preco":float(preco),
            "Disponibilidade": True
        }

print(f"Hello!! Welcome to ours hotel.")

costumer = input("What is your name? ")
while costumer == "":
    costumer = input("You need write your name or type 'enter' to exit: ")
    if costumer == "":
        break

cod_validation = (1, 2, 3, 4)

print(f"Currently our have the following bedrooms, tell me which one do you prefer? ")
for i , ii in available.items():
    print(f"{i} - {ii["name"]} - {ii["preco"]}")


bedroom_number = int(input("What the number of the bedroom would you like?  "))

while bedroom_number not in cod_validation:
    print(f"Invalid code. You need type correct code (1,2,3,4): ")
    bedroom_number = input(f"Type the code again or 'enter' to exit: ")
    if bedroom_number == "":
        sys.exit()
    bedroom_number = int(bedroom_number)

# Check if the bedrooms is available
#TODO se númeo do quarto estiver no arquivo reservas, então não pode reservar
with open ("reservas.txt", "r") as res:
    lines = res.readlines()
    for line in lines:
        lista = line.strip().split(",")
        if int(lista[1]) == int(bedroom_number):
            print(f"Sorry! The bedrooms is occupied! ")
            sys.exit()
        else:
            continue

    #available[bedroom_number]["Disponibilidade"] == False


number_day = int(input("How many day would you like reserve? "))

try:
    with open ("reservas.txt", "a") as res:
            res.write(f"{costumer},{bedroom_number},{number_day},\n")
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit()


