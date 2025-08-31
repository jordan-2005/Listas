from enum import nonmember

arreglo = [
            [1,2,3],
            [4,5,6],
            [7,8,9]

]
valor = 2
if any (valor in fila for fila in arreglo):
    print(f"Se encontro {valor} en arreglo")
else:
    print(f"No se encontro {valor} en arreglo")