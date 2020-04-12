"""
Using Files
"""
my_file = open('/home/centos/curso-python-linkedin/DevOps-Prokect/Project03/marvel.txt','w+')
my_file.write('Homem de Ferro\n')
my_file.write('Homem Aranha\n')
my_file.write('Capitão America\n')
my_file.writelines([
    'Thor\n'
    'Hulk\n'
    'Viuva Negra\n'
])
my_file.close()

my_file = open('/home/centos/curso-python-linkedin/DevOps-Prokect/Project03/marvel.txt','r')
print(my_file.read())
print('Vamos ler o arquivo novamente')
print(my_file.read())
my_file.close()

"""
Outra forma de abrir um arquivo
"""
with open('/home/centos/curso-python-linkedin/DevOps-Prokect/Project03/dc.txt','w+') as my_dc_file:
    my_dc_file.write('Batman\n')
    my_dc_file.write('Robin\n')
    my_dc_file.write('Mulher Maravilha\n')
    my_dc_file.writelines([
        'Aquaman\n'
        'Super Man\n'
    ])

my_dc_file = open('/home/centos/curso-python-linkedin/DevOps-Prokect/Project03/dc.txt','r')
with my_dc_file:
    print(my_dc_file.read())
    print('Vamos ler o arquivo novamente')
    print(my_dc_file.read())
