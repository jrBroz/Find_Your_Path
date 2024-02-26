def ler_txt():

    palavra_procurada = input("vai procurar pelo o que: ")

    with open("DriverMapped.txt", "r", encoding="utf-8") as rd_file:

        for linha, conteudo in enumerate(rd_file):

            if palavra_procurada in conteudo: print("Linha: ", linha), print("Caminho: ", conteudo)

        print("-" * 30)
        segunda_busca = input("Vai procurar algo a mais no driver atual ?  s/n ")

        if segunda_busca == 's': ler_txt()
        else: print("-" * 20) ,    print("Fim da busca.")
    ...