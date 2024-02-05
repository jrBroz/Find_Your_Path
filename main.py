import os

def map_TXT_Driver(arquivo):
    with open("DriverMapped.txt", "a") as file:
        file.writelines(arquivo + '\n')

...

###
#def readTXT(arquivo):

 #   with open("DriverMapped.txt", "w") as file:
      #  file.read(arquivo)
   # ...
#

def ProcurarArquivo():

        start = "C:\\"

        for dirpath, dirnames, filenames in os.walk(start):
            for filename in filenames:

                    filename = os.path.join(dirpath, filename)
                    map_TXT_Driver(filename)

...

ProcurarArquivo()
