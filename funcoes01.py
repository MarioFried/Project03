"""
Trabalhando com FUNCOES
"""
def inspect(func,*args):
    print(f"Executando a Funcao : {func.__name__}")
    val = func(*args)
    print(val)
    return(val)
    
def combine(a,b):
    return(a+b)