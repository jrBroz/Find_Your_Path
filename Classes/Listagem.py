from dataclasses import  dataclass
import psutil as ps

@dataclass
class Listagem:

    def listar_drivers(self):
        try:
            dispositivo_atual = ps.disk_partitions(all=True)

            if dispositivo_atual:
                print("Lista de Drivers:")
                for dispositivo in dispositivo_atual:
                    print(f"Nome: {dispositivo.device}, Tipo: {dispositivo.fstype}")
            else:
                print("Nenhum driver encontrado.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    ...

listar_discos_rigidos = Listagem()

listar_discos_rigidos.listar_drivers()