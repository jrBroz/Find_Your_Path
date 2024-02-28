import psutil as ps

def listar_drivers():
    try:
        dispositivo_atual = ps.disk_partitions(all=True)

        if dispositivo_atual:
            print("Lista de Drivers:")

        for dispositivo in dispositivo_atual:
            print(f"Nome: {dispositivo.device}, Tipo: {dispositivo.fstype}")

    except Exception as e: print(f"Ocorreu um erro: {e}")

    ...