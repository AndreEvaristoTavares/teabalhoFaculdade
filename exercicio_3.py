def validaInt(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x
# PROGRAMA
posicao = ['|1|','|2|','|3|','|4|'],['|5|','|6|','|7|','|8|']
print('_____HOTEL DOS ANIMAIS_____')
while True:
    # FASE 1
    print('a escolha deve ser feita de acordo com a numeração e posição á seguir...')
    for p in posicao: 
        print(p)
    print('FASE 1')
    fase1 = [
        ['|#|','|#|','|_|','|G|'],['|R|','|_|','|#|','|#|'] #RG
        ]
    for i in fase1:
        print(i)
    escolha1 = validaInt('escolha a posição do rato (R):', 1, 8)
    escolha2 = validaInt('escolha a posição gato (G): ',1, 8)
    if escolha1 == 6 and escolha2 == 3:
        print('PARABÉNS VC PASSOU ')
    else:
        print('VC ERROU')
        break
    # FASE 2
    print('FASE 2')
    fase2 = [
        ['|_|','|#|','|#|','|#|'],['|#|','|C|','|_|','|_|'] #CCO
        ]
    for i in fase2:
        print(i)
    escolha1 = validaInt('escolha a posição do cão (C):', 1, 8)
    escolha2 = validaInt('escolha a posição do cão (C):', 1, 8)
    escolha3 = validaInt('escolha a posição do osso (O):', 1, 8)
    if (escolha1 == 7 and escolha2 == 8) or (escolha1 == 8 and escolha2 == 7) and escolha3 == 1:
        print('PARABÉNS VC PASSOU ')
    else:
        print('VC ERROU')
        break
    # FASE 3
    print('FASE 3')
    fase3 = [
        ['|_|','|#|','|#|','|#|'],['|_|','|G|','|_|','|#|'] #GRO
        ]
    for i in fase3:
        print(i)
    escolha1 = validaInt('escolha a posição do gato (G):', 1, 8)
    escolha2 = validaInt('escolha a posição do rato (R):', 1, 8)
    escolha3 = validaInt('escolha a posição do osso (O):', 1, 8)
    if escolha1 == 7 and escolha2 == 1 and escolha3 == 5:
        print('PARABÉNS VC PASSOU ')
    else:
        print('VC ERROU')
        break
    #FASE 4
    print('FASE 4')
    fase4 = [
        ['|_|','|_|','|_|','|#|'],['|#|','|R|','|#|','|#|'] #QQO
        ]
    for i in fase4:
        print(i)
    escolha1 = validaInt('escolha a posição do queijo (Q):', 1, 8)
    escolha2 = validaInt('escolha a posição do queijo (Q):', 1, 8)
    escolha3 = validaInt('escolha a posição do osso (O):', 1, 8)
    if (escolha1 == 1 and escolha2 == 3) or (escolha1 == 3 and escolha2 == 1) and escolha3 == 2:
        print('PARABÉNS VC PASSOU ')
        print('PARABÉNS VC COMPLETOU O JOGO !!!!!!')
        break
    else:
        print('VC ERROU')
        break
# FIM


