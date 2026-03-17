def buscar_aluno_aprovado_com_a(lista_alunos):
    for nome, nota in lista_alunos:
        if nota >= 7 and nome.startswith("A"):
            return nome

    return "Não encontrado"


alunos = [
    ("Carlos", 8.0),
    ("Amanda", 6.5),
    ("Ana", 7.5),
    ("Arthur", 9.0)
]

resultado = buscar_aluno_aprovado_com_a(alunos)
print(f"Resultado: {resultado}")