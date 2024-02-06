import os
import psutil

def map_TXT_Driver(arquivo):
    with open("DriverMapped.txt", "a") as file:
        file.writelines(arquivo + '\n')
...

def listar_drivers():
    try:
        Current_Devices = psutil.disk_partitions(all=True)

        if Current_Devices:
            print("Lista de Drivers:")
            for dispositivo in Current_Devices:
                print(f"Nome: {dispositivo.device}, Tipo: {dispositivo.fstype}")
        else:
            print("Nenhum driver encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
...


def ProcurarArquivo():

        start = "C:\\"

        for dirpath, dirnames, filenames in os.walk(start):
            for filename in filenames:

                    filename = os.path.join(dirpath, filename)
                    map_TXT_Driver(filename)

...

ProcurarArquivo()