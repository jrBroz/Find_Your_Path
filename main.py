import threading
import time
from modules import ler
from modules import varrer as varrer_driver
# --------------------------------------

def iniciar_programa():

    thread_varrer = threading.Thread(target=varrer_driver.varrer_e_mapear)
    thread_ler = threading.Thread(target=ler.ler_txt)

    thread_varrer.start()
    thread_varrer.join()
    thread_ler.start()
    ...
iniciar_programa()
