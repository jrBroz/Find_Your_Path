import os
import Listagem
import time
from Escrever import *

def varrer_e_mapear():
    start2 = time.perf_counter()
    Listagem.listar_drivers() #Pra que o usuario possa ter uma lista dos drivers dentro do computador e escolher qual varrer

    start = input("Qual Driver voce deseja varrer: ")

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            map_txt_Driver(filename) #Essa função pega justamente todos os diretórios e nomes de arquivos e junto da função map_txt_Driver ele escreve dentro de um arquivo .txt

            end = time.perf_counter()
            duracao = round(end - start2)
                                            # Decidi Colocar o timer só para ter noção mesmo de quanto tempo leva, ** altamente dependente do quão cheio o driver é. **
    print('duracao em segundos: ' , duracao)

...