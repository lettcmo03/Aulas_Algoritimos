palavra = input("Digite uma palavra: ").strip().lower()

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")