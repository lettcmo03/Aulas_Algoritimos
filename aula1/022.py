texto = input("Digite um texto: ").lower()
vogais = set("aeiou")

qtd = sum(1 for ch in texto if ch in vogais)

print(f"Quantidade de vogais: {qtd}")