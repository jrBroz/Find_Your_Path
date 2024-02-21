import os
from modules import listagem
from modules import escrever as mapear
from modules import ler as ler_txt

def varrer_e_mapear():

    listagem.listar_drivers() #Pra que o usuario possa ter uma lista dos drivers dentro do computador e escolher qual varrer

    start = input("Qual Driver voce deseja varrer: ")

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            mapear.map_txt_Driver(filename)

        ...
    ...
    ler_txt.ler_txt()

#Essa função pega justamente todos os diretórios e nomes de arquivos e junto da função map_txt_Driver ele escreve dentro de um arquivo .txt

...

