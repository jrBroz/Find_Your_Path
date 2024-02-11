import os
import psutil as ps
import Listagem
import time



def map_txt_Driver(arquivo):
    with open("DriverMapped.txt", "a" , encoding="utf-8") as file:
        file.writelines(arquivo + '\n')
...


def varrer_e_mapear():
    start2 = time.perf_counter()
    Listagem.listar_drivers()

    start = input("Qual Driver voce deseja varrer: ")

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            map_txt_Driver(filename)

            end = time.perf_counter()
            duracao = round(end - start2)

    print('duracao em segundos: ' , duracao)

...



def ler_txt():

    with open("DriverMapped.txt", "r") as rd_file:

        for linha, conteudo in enumerate(rd_file):

            if "Curriculo" in conteudo:

                print("Linha: " , linha)
                print("Caminho: " , conteudo)

        else:
            print("________________")
            print("Fim da busca.")

    ...

varrer_e_mapear()


