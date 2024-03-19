from tkinter import *
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import os
import threading
import psutil




    # Função para listar os drivers usando psutil
def listar_drivers():
        drives = []
        for partition in psutil.disk_partitions():
            drives.append(partition.device)
        return drives

def varrer_e_mapear(start, file_path, progresso_var, botao_varrer):
        excluir_da_busca = ('__', '.')
        with open(file_path, 'w', encoding='utf-8') as file:
            for dirpath, dirnames, filenames in os.walk(start, topdown=True):
                dirnames[:] = [dirname for dirname in dirnames if not dirname.startswith(excluir_da_busca)]
                for filename in filenames:
                    filename = os.path.join(dirpath, filename)
                    file.write(filename + '\n')
                    # Atualizar a barra de progresso
                    progresso_var.set(progresso_var.get() + 1)
                    app.update_idletasks()  # Atualizar a interface gráfica
        # Habilitar o botão após a varredura
        botao_varrer.config(state=NORMAL)

def pesquisar_palavra_chave(file_path, palavra_chave):
        resultados = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for linha, conteudo in enumerate(file):
                if palavra_chave in conteudo:
                    resultados.append(conteudo.strip())
        return resultados

def iniciar_varredura():
        # Desabilitar o botão durante a varredura
        botao_varrer.config(state=DISABLED)
        start = driver_combobox.get()  # Obter o diretório selecionado no combobox
        # Definir o caminho para o arquivo de texto
        file_path = "caminhos_mapeados.txt"
        # Iniciar a varredura em uma thread separada
        thread_varredura = threading.Thread(target=varrer_e_mapear, args=(start, file_path, progresso_var, botao_varrer))
        thread_varredura.start()
        # Animar a barra de progresso
        animar_barra_progresso()

def pesquisar_palavra():
        palavra_chave = entrada_palavra_chave.get()
        resultados = pesquisar_palavra_chave("caminhos_mapeados.txt", palavra_chave)
        # Mostrar os resultados na caixa de texto
        retornar_caminho.delete(1.0, END)
        for resultado in resultados:
            retornar_caminho.insert(END, resultado + '\n')

def animar_barra_progresso():
        # Aumentar progresso até 100
        for i in range(101):
            progresso_var.set(i)
            app.update_idletasks()
            app.after(10)
        # Diminuir progresso de volta para 0
        for i in range(100, -1, -1):
            progresso_var.set(i)
            app.update_idletasks()
            app.after(10)
        # Continuar animação enquanto a varredura estiver em andamento
        

app = ttk.Window("")
app.geometry("620x670")  # Aumentei um pouco para caber a barra de progresso
style = Style(theme="cyborg") # voltar pra cyborg
app.title("Find Your Path")
# Configurar estilo para botões e barra de progresso
style.configure('green_neon.TButton', background='#39FF14', foreground='black')
style.configure('green_neon.Horizontal.TProgressbar', background='#39FF14')

icone = PhotoImage(file = 'Find Your Path/assets/find_your_path_icon.png')
app.iconphoto(False, icone)
# Frame principal
main_frame = Frame(app)
main_frame.pack(fill=BOTH, expand=True)

    # Dropdown acima do frame de texto
driver_label = ttk.Label(main_frame, text="Selecione o driver:")
driver_label.pack(side=TOP, pady=(10, 0))

    # Obtém a lista de drivers usando a função personalizada
drives = listar_drivers()
driver_combobox = ttk.Combobox(main_frame, values=drives, bootstyle=DARK)
driver_combobox.pack(side=TOP, fill=X, pady=(0, 10))

    # Frame de texto no meio da tela
text_frame = Frame(main_frame, width=325, height=400)  # Ajuste a altura conforme necessário
text_frame.pack(side=TOP, fill=BOTH, expand=True)

    # ScrolledText fixo no meio do text_frame
retornar_caminho = ScrolledText(text_frame, height=18, width=1300, wrap=WORD)  # Ajuste height conforme necessário
retornar_caminho.pack(side=TOP, fill=BOTH, expand=True)

    # Entrada de texto para palavra-chave
entrada_palavra_chave = ttk.Entry(main_frame)
entrada_palavra_chave.pack(side=TOP, pady=10)

    # Barra de progresso
progresso_var = DoubleVar()
progresso_barra = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=200, mode='determinate', variable=progresso_var, style='green_neon.Horizontal.TProgressbar')
progresso_barra.pack(side=TOP, pady=10)

    # Botão "Varrer"
botao_varrer = ttk.Button(main_frame, text="Varrer", command=iniciar_varredura, style='green_neon.TButton')
botao_varrer.pack(side=LEFT, padx=5)

    # Botão "Pesquisar"
botao_pesquisar = ttk.Button(main_frame, text="Pesquisar", command=pesquisar_palavra, style='green_neon.TButton')
botao_pesquisar.pack(side=LEFT, padx=5)

    # Label "Feito por:"
label_feito_por = ttk.Label(main_frame, text="Feito por João Rafael Broz dos Santos", anchor=SE, foreground='#555')  # Defina a cor do texto para cinza escuro
label_feito_por.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)


app.mainloop()
