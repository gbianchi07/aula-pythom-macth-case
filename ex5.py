print('1 picanha R$ 25,00')
print('2 lasanha R$ 20,00')
print('3 strogonoff R$ 20,00')
print('4 bife acebolado R$ 15,00')
print('5 pao com ovo R$ 5,00')

opcao= int(input('escolha o prato desejado:'))

match opcao:
    case 1:
        valor= 25.0
    case 2:
        valor=20.0
    case 3:
        valor=20.0
    case 4:
        valor=15.0
    case 5:
        valor=5.0
    case _:
        print('opcao invalida')
        valor=0

gorjeta= input('deseja pagar os 10% (sim/nao) ')
match gorjeta:
    case 'sim':
        valor = valor + valor *10/100
        print(f'valor total:{valor}')
    case 'nao':
        print(f'valor total: {valor}')