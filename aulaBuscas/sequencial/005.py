def buscar_primeiro_maior_de_idade(lista_alunos):
    for aluno in lista_alunos:
        if aluno["idade"] >= 18:
            return aluno["nome"]

    return "Não encontrado"


alunos = [
    {"nome": "Pedro", "idade": 16},
    {"nome": "Maria", "idade": 17},
    {"nome": "João", "idade": 18},
    {"nome": "Ana", "idade": 20}
]

resultado = buscar_primeiro_maior_de_idade(alunos)
print(f"Resultado: {resultado}")