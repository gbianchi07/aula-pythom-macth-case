numero = int(input('informe um numero inteiro:'))

resto = numero % 3

match resto:
    case 0:
        print('multiplo de 3')
    case _:
        print('nao é multiplo de 3')