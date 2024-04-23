# 

nome = "Global"
numero = 1



def fundcao_1():
    nome = "Local" # essa variável é local, só existe dentro da função. Não subrescreve a variável nome definida fora dela.
    return nome

fundcao_1()
print("********")
print(nome)

def funcao_2():
    global nome #mecanismo que se utiliza para acessar a variável global caso queira manipulá-la.
    nome += " Incremento"
    return nome
print("********")
print(nome)
funcao_2()
print(nome)
