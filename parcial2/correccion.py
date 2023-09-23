def mostrar_mensaje(mensaje):
    print("************")
    print(mensaje)
    print("************")

def cargar_suma():
    valor1= int(input("Ingrese el primer valor:"))
    valor2= int(input("Ingrese el segundo valor:"))
    suma = valor1 + valor2
    print("La suma es:", suma )

#programa principal
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado")
cargar_suma()
mostrar_mensaje()


