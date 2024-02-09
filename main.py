import os
import psutil as ps

def map_txt_Driver(arquivo):
    with open("DriverMapped.txt", "a") as file:
        file.writelines(arquivo + '\n')
...


def varrer_e_mapear():

    start = "C:\\"

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            map_txt_Driver(filename)
...

# ***** WORK IN PROGRESS! *****
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

ler_txt()