#Antes de realizar la lectura y escritura del documento, debemos crear un archivo tipo txt#
storage = open("my_notes.txt", "r")   #aperturamos una nueva variable llamada "storage", ahí vamos a interactuar con el archivo utilizando open() para dar conexión o crear un archivo nuevo#
newstorage = storage.read() #Luego utilizamos el metodo .read para leer de corrido todos los elementos del texto, lo almacenamos en otra variable#
print(newstorage) #Por último imprimimos la variable anterior#
storage.close() #Cerramos el archivo para no utilizar recurso y por seguridad#

#Utilizamos el metodo ecritura .write()
storage = open("my_notes.txt", "a")  #En este caso utilizamos la letra "a" para agregar texto a nuestro archivo#
newtext = storage.write("\nMe gusta el mote") #Aplicamos el metodo.write, abrimos paréntesis y escribimos el texto, pero antes de eso usamos \n para que tenga un salto de línea#
storage.close() #Cerramos el archivo##


