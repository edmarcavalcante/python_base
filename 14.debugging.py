# Biblitoteca built-in do Python para debugging -->> pdm ou ipdb (mais atual e interativo)
"""
Exemplo
> python -m pdb 14.debugging.py

pdb é a ferramenta padrão de debugging interativo 
do Python e além de ser uma ferramenta 
bastante tradicional também se tornou um padrão 
adotado por todos os outros debuggers.

> (pdb) hep
> (pdb) ?

__________________________
> python -m ipdb 14.debugging.py

Ao trocar pdb por ipdb e executar teremos a mesma 
experiência porém dentro de um terminal ipython

__________________________
Comandos:

(pdb) l: show the current execution line 
(pdb) n: run the current block and jump to the next
(pdb) s: step into > enter into the execution of a function
(pdb) b 12: create a breakpoint in the line 12
(pdb) disable 12: remove the breakpoint in line 12




"""

def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word
print(repete_vogal("banana"))