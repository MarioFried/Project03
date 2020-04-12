"""
Error Handling
"""
#import sys

file_name = 'receitas.txt'

try:
    my_file = open(file_name,'x')
    my_file.write('Carbonara\n')
    my_file.close()
    
except FileExistsError as err:
    print(f"O Arquivo {file_name} ja existe!!!")
#    sys.exit(1)
except:
    print(f"Não é possivel escrever no arquivo")
#    sys.exit(1)
else:
    print(f"Escrita no arquivo {file_name}")
finally:
    print("Execução Completa")

