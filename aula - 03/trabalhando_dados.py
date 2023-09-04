# resolução da questão 2 da Atividade verificadora de aprendizagem.
def controle_alunos():
    nomes = []
    emails = []
    cursos = []

    while True:
        try:
            op = int(input('1 - Cadastrar novo aluno.\n'
                           '2 - Lista de alunos.\n'
                           '3 - Buscando aluno\n'
                           '4 - Sair\n'
                           'Resposta:'))
            if op == 1:
                nome = input('Digite o nome do aluno: ')
                nomes.append(nome)
                email = input('Digite o e-mail do aluno: ')
                emails.append(email)
                curso = input('Digite o nome do curso: ')
                cursos.append(curso)
            elif op == 2:
                print("Lista de alunos:")
                for i in range(len(nomes)):
                    print(
                        f"Nome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}")
            elif op == 3:
                nome_busca = input(
                    "Digite o nome do aluno que deseja buscar: ")
                encontrado = False
                for i in range(len(nomes)):
                    if nomes[i] == nome_busca:
                        print(
                            f"Aluno encontrado:\nNome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Aluno não encontrado.")
            elif op == 4:
                break
            else:
                print('Opção inválida')
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    with open("alunos1.txt", "w") as arquivo:
        for i in range(len(nomes)):
            arquivo.write(
                f"Nome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}\n")


controle_alunos()
