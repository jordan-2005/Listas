#Primero creamos un diccionario#
información_personal = {"nombre":"Jordan","edad":34, "ciudad":"Los Angeles"}
#Si queremos cambiar algún valor de una llave hacemos de la siguiente manera#
información_personal["ciudad"] = "Quito"
#De este modo la llave "ciudad" tiene un nuevo valor#

#Ahora agregemos un nuevo par-clave#
#Realizamos lo mismo que al cambiar el valor de una llave, en este caso, agregamos nuevos valores#
información_personal["profesión"] = "Marketing Manager"

#Comprobar si hay la clave "teléfono" en el diccionario#
#Creamos el condicional "if" y escribimos la clave que comprobaremos dentro del diccionario. Si esta dentro del diccionario imprimiremos un "comprobado",caso contrario generaremos la clave con su valor#
if "teléfono" in información_personal:
    print("El teléfono ya está registrado")
else:       #En caso de que no exista la clave "teléfono", agregará al diccionario#
    información_personal["teléfono"]="02-1234567"
#Eliminar claves
#En este caso usamos el comando "del" seguido del nombre del diccionario con la clave que vamos a eliminar#
del información_personal["edad"] #Esto elimina la clave y el valor#
#Por último imprimimos el diccionario con los nuevos datos#
#Listo Calisto#
print(información_personal)
