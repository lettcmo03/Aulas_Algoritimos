from pathlib import Path

caminho = Path(input("Caminho para salvar o .txt (ex: saida.txt): ").strip())
texto = input("Digite o texto para salvar: ")

with caminho.open("w", encoding="utf-8") as f:
    f.write(texto + "\n")

print("Salvo com sucesso!")