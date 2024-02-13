import os
os.system('cls' if os.name == 'nt' else 'clear')

fila = []

#Añadir elementos a la fila
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
fila.append('cliente4')
fila.append('cliente5')
print("Los elementos de la fila son:", fila)

#Atender cliente (eliminar elemento de la fila)
#pop sirve para elegir cual elemento de los 4
cliente_atendido = fila.pop(1)
print("Cliente atendido fue:", cliente_atendido)
print("Fila despues de atender a un cliente son:", fila)
