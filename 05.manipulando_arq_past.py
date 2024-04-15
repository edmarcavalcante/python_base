import os

# criando pasta no python
# os.mkdir("pasta_teste")

# Exibindo caminho absoluto da pasta atual

os.path.abspath(os.curdir)

# criando um arquivo 

open("arquivo.txt", "w")

# Listar arquivos na pasta

os.listdir(".")

# Esquevendo no arquivo criado

arquivo = open("arquivo.txt", "a") #o parâmetro 'a' acrescenta texto. o 'w' substitui tudo
arquivo.write("Hello\n")
arquivo.close()

# Ler conteúdodo arquivo
print(open("arquivo.txt", "r").read())


# CONTEXT MANAGER 

with open("arquivo.txt","a") as arquivo:
    arquivo.write("Hello - Context Manager\n")
    
    # Usando esse design, não é necessário explicitar o close()

# TRABALHANDO COM CAMINHOS 


