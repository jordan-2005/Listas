def descuento (a,b,saludo="Hola, su valor total aplicando el descuento es de"):
     operacion = (a-(a*(b/100)))
     print(f"{saludo} {operacion}$")
descuento(10,50)
descuento(10,90)
descuento(54,75)



