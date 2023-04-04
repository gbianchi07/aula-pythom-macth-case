letra= input('informe seu estado civil(D,C,S,V):')

match letra:
    case 'D'| 'd':
        print('divorciado')
    case 'C'| 'c':
        print('casado')
    case 'S'|'s':
        print('solteiro')
    case 'V'|'v':
        print('viuvo')
    case _:
        print('opcao invalida')