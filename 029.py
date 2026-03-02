nome = input("Nome: ").strip()
idade = int(input("Idade: "))
pessoa = {"nome": nome, "idade": idade}

print("Dados:", pessoa)
print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")