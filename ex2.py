numero = float(input('numero:'))

print('opcao 1 - o dobro')
print('opcao 2 - a metade')
print('opcao 3 - 10% do numero')


opcao= int (input('escolha uma opcao:'))

match opcao:
    case 1:
        resultado = numero * 2 
        print(f'o dobro de {numero} é {resultado}')
    case 2:
        resultado = numero / 2
        print(f'a metade de {numero} é {resultado}')
    case 3:
        resultado = numero * 0.10
        print(f'10% de {numero} é {resultado}')
    case _:
        print('opcao invalida')