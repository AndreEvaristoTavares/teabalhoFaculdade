def trocarVogal(pergunta):
    nome = input(pergunta)
    print(nome.upper())
    nome = nome.replace('a', '@')
    nome = nome.replace('e', '&')
    nome = nome.replace('i', '!')
    nome = nome.replace('o', '#')
    nome = nome.replace('u', '*')
    nome = nome.upper()
    return nome

nome = trocarVogal('nome: ')

print(nome)
