print('1 - linux')
print('2 - banco de dados')
print('3 - windos server')
print('4 - logica e programacao')

opcao =  int(input('informe a opcao desejada:'))

match opcao:
    case 1:
        print('auditorio 1')
    case 2:
        print('auditorio 2')
    case 3:
        print('auditorio 3')
    case 4:
        print('auditorio 4')
    case _:
        print('opcao invalida')
        