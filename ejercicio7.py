"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
renta = float(input("Su renta anual "))

if renta < 10000:
    impo = 5
elif renta < 20000:
    impo = 15
elif renta < 35000:
    impo = 20
else:
    impo = 4

print("El valor total de pagar incluido el tipo de impositivo es: ", renta * impo / 100, "$", sep='' )


