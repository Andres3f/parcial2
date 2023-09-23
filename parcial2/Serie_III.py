pi = 3.14

def area_circulo(radio):
  return pi * radio ** 2

def area_triangulo(base, altura):
  return base * altura / 2

def area_rectangulo(largo, ancho):
  return largo * ancho

print("Elige una figura geométrica:")
print("1. Círculo")
print("2. Triángulo")
print("3. Rectángulo")
opcion = int(input("Ingresa el número de tu opción: "))

if opcion == 1:
  radio = float(input("Ingresa el radio del círculo: "))
  area = area_circulo(radio)
  print(f"El área del círculo es {area:.2f} unidades cuadradas.")
elif opcion == 2:
  base = float(input("Ingresa la base del triángulo: "))
  altura = float(input("Ingresa la altura del triángulo: "))
  area = area_triangulo(base, altura)
  print(f"El área del triángulo es {area:.2f} unidades cuadradas.")
elif opcion == 3:
  largo = float(input("Ingresa el largo del rectángulo: "))
  ancho = float(input("Ingresa el ancho del rectángulo: "))
  area = area_rectangulo(largo, ancho)
  print(f"El área del rectángulo es {area:.2f} unidades cuadradas.")
else:
  print("Opción inválida.")
    