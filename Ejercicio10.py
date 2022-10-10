print('Lista de la compra (usar comas para separar los productos):')
lista = input()
lista_separada = lista.replace(', ', '\n').title()
print(lista_separada)