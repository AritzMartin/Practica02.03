nombre = input('Escribe nombre:\n')
precio = float(input('Precio del producto con dos decimales:\n'))
unidades = int(input('Numero de unidades:\n'))
resultado = round(precio*unidades, 2)
print('{} = {:6.2f} * {:3} = {:8.2f}'.format(nombre, precio, unidades, resultado))