# Um professor deseja desenvolver um sistema para gerenciar as notas dos alunos de sua turma. Esse sistema deve permitir cadastrar alunos, registrar suas notas e calcular a média da turma. Além disso, o sistema precisa salvar essas informações em um arquivo e ser capaz de lidar com possíveis erros de entrada e saída. Siga os requisitos abaixo para implementar a solução.

# defs =  /  / media_turma / /  / salvar_em_arquivo

# dict -> nome (string) / notas (lista de floats) [min 2, max 5] / media (float)


# Use uma lista para armazenar um dicionário para cada aluno. Cada dicionário deve conter os seguintes dados: 

# - Crie uma função ordenar_alunos que ordene a lista de alunos por média de forma decrescente (do aluno com maior média para o menor).

# - Crie uma função salvar_em_arquivo que salve os dados de todos os alunos em um arquivo de texto ( alunos.txt ). Cada linha do arquivo deve conter o nome do aluno e a sua média, separados por uma vírgula.

# adicionar_aluno -> solicitar o nome / notas [calcula a sua media] / armazenar no dicionário do aluno / adicionar à lista de alunos

def line():
    print('='*30)

alunos = {}

def ordenar_aluno():
    print(sorted(alunos))

def cadastrar_alunos():
    alunos['Nome'] = input('Insira o nome do aluno: ').capitalize()

    notas = []

    try:
        while len(notas) < 5 :
            nota = float(input('Insira a nota do aluno ou -1 para finalizar: '))
            if len(notas) < 2 and nota == -1:
                print('ERRO! POR FAVOR INSIRA NO MÍNIMO 2 NOTAS!!\n')   
                nota = float(input('Insira a nota do aluno ou -1 para finalizar: '))
            if nota == -1:
                break
            notas.append(nota)
    except ValueError:
        print('ERRO! Digite apenas números')
    
    sum = list(map(int, notas))

    def somaNotas(sum):
        if len(sum) == 0:
            return 0
        return sum[0] + somaNotas(sum[1:])
    
    def media_aluno():
        alunos['Média'] = media = somaNotas(sum) / len(notas)
        return media

    alunos['Notas'] = notas
    
    media_aluno()
    
    # print(alunos)
def mainMenu():
    while True:
            line()
            print('MENU')
            menu = int(input('1 - Cadastrar Aluno \n2 - Exibir Alunos \n3 - Ordenar Alunos \n4 - Gerar Arquivo \n0 - Sair \n'))

            match menu:
                case 1:
                    cadastrar_alunos()
                case 2:
                    print(alunos)
                case 3:
                    # ordenar_aluno()
                    print('Ordenando Alunos...')
                case 4:
                    print('Gerando Arquivo...')
                case 5:
                    print('Saindo...')
                    break
                case _:
                    print('Opção inválida!')

mainMenu()