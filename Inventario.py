
#Valores que controlan los ciclos
n=-1
n2=-1
#Solicita el nombre del producto al usuario
nombre = input("Bienvenido por favor ingrese el nombre del producto que desea ingresar: ")
#Ciclo anidado para asegurarse de que el usuario ingresó bien los datos
while n != 0:
    #Se solicita la cantidad de unidades que quiere ingresar del producto al usuario
    cantidad=int(input("Ingrese la cantidad de existencias que hay del producto: "))
    #Condicional para asegurarse que el usuario ingreso un valor aceptable
    if cantidad <= 0:
            #Mensaje que notifica al usuario que ingreso un valor erroneo
            print("Digite una cantidad válida (mayor a 0)")
    else:
        #Ciclo anidado para no repetir el proceso anterior
        while n2 != 0:
            #Solicita al usuario el precio del producto
            precio=float(input("Digite el costo por unidad del producto: "))
            #Condicional para asegurarse que el usuario ingreso un valor aceptable
            if precio<=0:
                #Mensaje que notifica al usuario que ingreso un valor erroneo
                print("Digite un precio válido (mayor a 0)")
            else:
                #Se realiza la multiplicación del precio y la cantidad para saber el valor total
                costo_total = float(precio*cantidad)
                #Imprime la información que se le solicitó al usuario, más el precio total del producto
                print("Producto:",nombre,"/ Precio por unidad:",precio,"/ unidades disponibles:",cantidad,"/ Precio total:",costo_total)
                #se cambia el valor para cerrar el ciclo
                n2 = 0
        #se cambia el valor para cerrar el ciclo
        n=0
#El algoritmo le solicita al usuario ingresar el nombre del producto, luego entra en un ciclo controlado para evitar que el usuario ingrese valores incorrectos
#Dentro del ciclo solicita la cantidad de unidades del producto, si ingresa un valor incorrecto y vuelve a preguntar hasta que el valor ingresado sea satisfactorio
#Luego ingresa en un ciclo anidado donde pregunta por el precio del producto, donde se repite el proceso anterior, al ingresar un valor satisfactorio realiza una multiplicación entre el precio y la cantidad
#Para finalizar imprime los datos ingresados por el usuario junto al precio total y se cierran los ciclos cambiando el valor de la condicional