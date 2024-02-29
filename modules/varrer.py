import os
from modules import listagem
from modules import escrever as mapear

def varrer_e_mapear():

    excluir_da_busca = ('__', '.')
    listagem.listar_drivers()
    start = input("Qual Driver voce deseja varrer: ")
    for dirpath, dirnames, filenames in os.walk(start, topdown=True):
        dirnames[:] = [dirname for dirname in dirnames if not dirname.startswith(excluir_da_busca)]
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            mapear.map_txt_Driver(filename)
...


#When topdown is True, the caller can modify the dirnames list in-place (perhaps using del or slice assignment),
#and walk() will only recurse into the subdirectories whose names remain in dirnames; this can be used to prune the search,
# impose a specific order of visiting,
# or even to inform walk() about directories the caller creates or renames before it resumes walk() again.

