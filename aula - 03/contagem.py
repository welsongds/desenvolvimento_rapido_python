# #resolução da questão 1 da Atividade verificadora de aprendizagem.
def contando_ate(min, max):
    with open("crescente.txt", "w", encoding="UTF-8") as arquivo:
        for elemento in range(min, max + 1):
            arquivo.write(str(elemento) + ";")


contando_ate(1, 100)
