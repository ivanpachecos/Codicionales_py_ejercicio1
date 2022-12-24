"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""
#Datos
bonificacion = 2.400 
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
rendimiento = float(input("Ingrese la putuación: "))

#Algoritmo
if rendimiento == inaceptable:
    valor = "Inaceptable"
elif rendimiento == aceptable:
    valor = "Aceptable"
elif rendimiento >= meritorio:
    valor = "Meritorio"
else:
    valor = ""

#Resultado
if valor == "":
    print("Ingrese otro valor, ese valor es incorrecto")
else: 
    print("Tu nivel de rendimiento es %s" % valor)
    print("Te corresponde cobrar %.2f€" % (rendimiento * bonificacion))
