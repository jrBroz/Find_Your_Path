import os
import psutil as ps

def map_TXT_Driver(arquivo):
    with open("DriverMapped.txt", "a") as file:
        file.writelines(arquivo + '\n')


...


def listar_drivers():
    try:
        Current_Devices = ps.disk_partitions(all=True)

        if Current_Devices:
            print("Lista de Drivers:")
            for dispositivo in Current_Devices:
                print(f"Nome: {dispositivo.device}, Tipo: {dispositivo.fstype}")
        else:
            print("Nenhum driver encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


...


def procurarArquivo():
    start = "C:\\"

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            map_TXT_Driver(filename)


...

# ***** WORK IN PROGRESS! *****
def ler_txt():
    palavras = []

    with open("DriverMapped.txt", "r") as rd_file:

     ler =  rd_file.read()
    print(ler)
    # O .read() não retorna todas as linhas presentes no arquivo txt.
    # Readlines() também não retornou todas as linhas.
    #Arquivo .txt está dando por volta de 74mb com mais de 10 mil linhas
    #Encontrar uma forma de talvez dividir em chunks,
    ...

procurarArquivo()

