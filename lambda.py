# sumar = lambda x,y: x + y

# print(sumar(9,7))

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-2))
# [2, -2.0]