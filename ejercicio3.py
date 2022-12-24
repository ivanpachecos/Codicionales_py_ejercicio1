"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error."""
dividendo = float(input("Ingrese el dividendo número: "))
divisor = float(input("Ingrese el divisor número: "))
if divisor == 0:
    print("El segundo numero es cero, no se puede dividir. Intente con otro número")
else:
    print(dividendo/divisor)
