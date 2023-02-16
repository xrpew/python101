objetivo = int(input('Escoge un número entero: '))
respuesta = 0 

while respuesta**2 < objetivo:
    respuesta +=1
    # print(respuesta)

if respuesta**2 == objetivo:
    print(f'la respuesta es {respuesta}')
else:    
    print(f'{objetivo} no tiene raiz cuadrada exacta')