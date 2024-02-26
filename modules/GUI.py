import psutil as ps
import customtkinter as ctk

def listar_drivers():
    try:
        dispositivo_atual = ps.disk_partitions(all=True)
        output_text.delete(1.0, ctk.END)  # Limpa o conteúdo anterior no widget de texto

        if dispositivo_atual:
            for dispositivo in dispositivo_atual:
                output_text.insert(ctk.END, f" {dispositivo.device}, Tipo: {dispositivo.fstype}\n")

    except Exception as e:
        output_text.insert(ctk.END, f"Ocorreu um erro: {e}\n")

def criar_dropdown(selection):
    if selection == "Mostrar Discos":
        listar_drivers()

root = ctk.CTk()
root.geometry("600x550")
root.title("Find your Path")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

options = ["Mostrar Discos"]
dropdown_menu = ctk.CTkComboBox(master=frame, values=options, command=criar_dropdown)
dropdown_menu.pack(pady=12, padx=10)

output_text = ctk.CTkTextbox(master=frame, height=100, width=260)
output_text.pack(pady=10, padx=10)

root.mainloop()
