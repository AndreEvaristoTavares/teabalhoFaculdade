from random import randint
pessoa = []
def Menu():
    try:
        print('1- cadastrar\n2- listar cadastros\n0- sair')
        opcao = int(input('opção: '))
        if opcao >= 0 and opcao <=2:
            return opcao
        else:
            print('opção invalida ' )
            Menu()
    except ValueError:
        print('opção invalida ')
        Menu()
def novoCadastro():
    voucher = randint(1, 10000)
    nome = input('nome: ')
    email = input('email: ')
    telefone = input('telefone: ')
    curso = input('curso: ')
    dicionarioCadastro = {'voucher':voucher, 'nome':nome, 'email':email, 'telefone':telefone, 'curso':curso}
    pessoa.append(dicionarioCadastro)

#programa principal
while True:
    print('SEJA BEM VINDO AO CADASTRO DO CURSO!!!')
    opcaoMenu = Menu()
    if opcaoMenu == 1:
        novoCadastro()
    elif opcaoMenu == 2:
        for p in pessoa:
          print(p)
    elif opcaoMenu == 0:
        print('SAINDO...')
        break