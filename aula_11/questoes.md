# Atividade Autônoma Aura - Aula 11

Questão 1: PostgreSQL é um dos bancos de dados mais utilizados no mundo, por ser opensource torna-se uma ótima opção aos bancos de dados pagos como Oracle e SqlServer. O PSYCOPG é considerado o adaptador mais utilizado para conexões com o PostgreSQL. A forma correta de abrir conexão com PSYCOPG é:
a- import psycopg con = psycopg.open(host='localhost', database='exemplo', user='postgres',
password='postgres123')
b- import psycopg2 con = psycopg2.open(host='localhost', database='exemplo', user='postgres',
password='postgres123')
c- import psycopg con = psycopg.connect(host='localhost', database='exemplo', user='postgres',
password='postgres123')
d-import psycopg2 con = psycopg2.postgres(host='localhost', database='exemplo', user='postgres',
password='postgres123')
e- import psycopg2 con = psycopg2.connect(host='localhost', database='exemplo', user='postgres',
password='postgres123')

RESPOSTA: E

Questão 2: O Python possui diversos frameworks para trabalhar com banco de dados. Um desses frameworks é o psycopg2 que faz interface com o Postgres. Observe o programa abaixo.
    import psycopg2
    conn = psycopg2.connect(database="postgres", user="postgres", password="senha123", host="127.0.0.1", port="5432")
    print("COnexão com o Banco de Dados aberta com sucesso!")
    cur = conn.cursor()
    cur.execute("""select * from public."AGENDA" where "id" = 1""")
    registro = cur.fetchone()
    print(registro)
    conn.commit()
    print("Seleção com sucesso!")
    conn.close()
Agora selecione a opção correta a respeito do programa:
a- O programa garante que sempre vai retornar dados
b- O programa realiza uma consulta na tabela AGENDA onde o atributo id da tabela seja igual a 1.
c- O código está preparado para tratar possíveis exceções de execução.
d- O código está implementado usando programação orientada a objetos
e- A ultima linha é dispensável.

RESPOSTA: B