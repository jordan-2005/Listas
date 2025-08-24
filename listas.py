##HELLO WORLD##
L=[0, 1, 2, 3, 4, 6, 7]
L.extend([8,9,10]) ##Utilizamos extend para agregar varios elementos a la lista##
print(L)           ##Utilizamos corchetes y cuando imprimemos no se ve los corchetes##

##Append##
L.append([5]) ##Utilizamos append para agregar un solo elemento a la lista##
print(L)      ##En este caso se ve los corchetes##

##Cambiamos un elemento de la lista##
Frutas=["Manzana", "Pera", "Naranja"]
Frutas[0]="Mote"       ##En este caso cambiamos el elemento 0 por uno nuevo##
print(Frutas)          ##Imprimimos la lista de frutas con el elemento cambiado##

##Eliminamos un elemento de la lista##
del(Frutas[1])
print(Frutas)          ##En este caso eliminamos el elemento 1 de la lista de frutas##|

##Transformamos una cadena en una lista##
Cadena="Hola Mundo"
Lista=Cadena.split()  ##Utilizamos split para transformar la cadena en una lista##
print(Lista)          ##Imprimimos la lista##

Newcadena="hola, mundo, python"
Newlista=Newcadena.split(" ")
print(Newlista)         ##En este caso utilizamos la coma como separador##

##Clonamos una lista##
Lista1=[1,2,3,4,5]
Lista2=Lista1.copy()  ##Utilizamos copy para clonar la lista##
Lista2.append("Me gusta python")
print(Lista2)          ##Imprimimos la lista clonada##  
print(Lista1)          ##Imprimimos la lista original##


      ##Hay otra manera (supongo)
celulares=["Samsung", "Apple", "Xiaomi"]
celulares2=celulares  ##En este caso no es una clonacion, es una referencia##
                      ##Si cambiamos un elemento de celulares2 se afecta a celulares##

##Ahora podemos ordenar las listas##
numeros=[5, 2, 9, 1, 5, 6]
numeros.sort()  ##Utilizamos sort para ordenar la lista de numeros##
print(numeros)  ##Imprimimos la lista de numeros ordenada##

##Cambiar valores de una lista en un índice específico##
ropa = ["camisa","pantalón", "chaqueta"]     
ropa.insert(1,"gorro")
print(ropa)  ##Utilizamos insert para agregar un elemento en un índice específico##
 ##Saber la longitud de una lista##
A=[1]
A.append([2,3,4]) ##En este caso agregamos una lista dentro de otra lista##
print(len(A))  ##Utilizamos len para saber la longitud de la lista A##
##En este caso la longitud se cuenta desde 1##