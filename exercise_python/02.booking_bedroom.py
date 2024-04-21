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
available = {}
with open("quartos.txt", "r") as file:
    lines = file.readlines()
    #print(lines)
    for line in lines[1:]:
        #print(line)
        Codigo, nome, preco = line.strip().split(",")
        dic = {
            "Codigo":Codigo,
            "nome": nome,
            "preco": preco
        }


        available[Codigo] = dic

print(available)

print(f"We have the follows bedrooms available:")
for cod, d in available.items():
    n = d["nome"]
    p = d["preco"]
    print(f"Código: {cod} -> {n} - R$ {p}")

ask = input("Wich bedroom would you like? ")

