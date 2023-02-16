def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [1, 2, 3]

print(f'multiplicar por dos {aplicar_operacion(multiplicar_por_dos, nums)}')
#  [2, 4, 6]

print(f'sumar dos: {aplicar_operacion(sumar_dos, nums)}')
# [3, 4, 5]


