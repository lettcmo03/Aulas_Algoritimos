def busca_nome(lista_nomes, nome_alvo):
    nome_alvo = nome_alvo.lower()

    for indice, nome in enumerate(lista_nomes):
        if nome.lower() == nome_alvo:
            return indice

    return -1


nomes = ["Ana", "Carlos", "joão", "Marina"]
alvo = "JOÃO"

resultado = busca_nome(nomes, alvo)

if resultado != -1:
    print(f"O nome '{alvo}' foi encontrado no índice {resultado}.")
else:
    print("Nome não encontrado.")