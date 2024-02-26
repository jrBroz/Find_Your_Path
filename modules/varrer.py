import os
from modules import listagem
from modules import escrever as mapear
def varrer_e_mapear():


    listagem.listar_drivers()
    start = input("Qual Driver voce deseja varrer: ")

    for dirpath, dirnames, filenames in os.walk(start):

        for filename in filenames: filename = os.path.join(dirpath, filename) ,   mapear.map_txt_Driver(filename)
        ...
    ...
...

