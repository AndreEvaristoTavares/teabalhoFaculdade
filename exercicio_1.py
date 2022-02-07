while True:
    print('consultar qual ensino aluno esta ')
    nome = str(input('nome do aluno: '))
    idade = int(input('idade do aluno: '))
    if idade >= 1 and idade <= 5:
        print('o aluno {} tem {} anos e pertence ao ensino infantil '.format(nome, idade))
    if idade >= 6 and idade <= 10:
        print('o aluno {} tem {} anos e pertence ao ensino fundamental 1 '.format(nome, idade))
    if idade >= 11 and idade <= 14:
        print('o aluno {} tem {} anos e pertence ao ensino fundamental 2 '.format(nome, idade))
    if idade >= 15:
        print('o aluno {} tem {} anos e pertence ao ensino médio '.format(nome, idade))
    con = str(input('quer continuar a consultar  (s)sim, (n)não: '))
    if con == 's':
        continue
    elif con == 'n':
        print('saindo do programa')
        break



