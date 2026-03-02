from pathlib import Path

caminho = Path(input("Caminho do arquivo .txt: ").strip())
if not caminho.exists():
    print("Arquivo não encontrado.")

with caminho.open("r", encoding="utf-8") as f:
    linhas = f.readlines()

print(f"Número de linhas: {len(linhas)}")