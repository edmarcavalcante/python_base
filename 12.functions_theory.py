# EXEMPLOS DE APLICAÇÃO

# METHOD SOLID - Single Responsability PRINCIPLE

def funcao_teste( a, b, c):
    """ This function do something with a, b, c

    Use this functionto do this a + b + c

    :param a: int
    :param b: int
    :param c: int
    
    obs: This standard is falling in desuse because the "type hint"
    https://docs.python.org/3/library/typing.html
    
    """

# Type Hint
def funcao_type_hint( a: int, b: int, c: int) -> int:
    resultado = a + b + c
    return resultado

#print(help(funcao_teste))
#output 
"""
funcao_teste(a, b, c)
    This function do something with a, b, c

    Use this functionto do this a + b + c

    :param a: int
    :param b: int
    :param c: int

    obs: This standard is falling in desuse because the "type hint"
    https://docs.python.org/3/library/typing.html
"""

print("*****************")

#print(help(funcao_type_hint))
#Output
"""
funcao_type_hint(a: int, b: int, c: int) -> int
    # Type Hint
"""

# PASSAGE OF ARGUMENTS

def soma( n1, n2):
    """
    Calculate the sum of "a" and "b"
    
    """
    return n1+n2

test1 = [
    {"n1": 90, "n2": 20},
    {"n1": 65, "n2": 23},
    {"n1": 65, "n2": 24},
    {"n1": 905, "n2": 2}
    ]

test2 = [
    (1,2),
    (5,6),
    (9,54)
    ]

print("************")
for i in test1:
    print(soma(**i))#Desempacota dicionários

print("************")
for y in test2:
    print(soma(*y))#Desempacota tuplas

