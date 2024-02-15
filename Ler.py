def ler_txt():

    palavra_procurada = input("vai procurar pelo o que: ")

    with open("DriverMapped.txt", "r", encoding="utf-8") as rd_file:

        for linha, conteudo in enumerate(rd_file):

            if palavra_procurada in conteudo:

                print("Linha: ", linha)
                print("Caminho: ", conteudo)

        else:
            print("________________")
            print("Fim da busca.")

    ...