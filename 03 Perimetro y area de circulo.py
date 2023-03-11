"""Problema*: Desarrollar dos funciones, una que calcula el
el área de un círculo y otra para el perímetro de un
círculo. Usar las funciones tres veces para calcular el
área y el perímetro de los círculos con los siguientes tres
radios:"""

import math
print("Las áreas y perímetros de los tres círculos son los siguientes:")
print("")
def fCalculoCirculo(a):
    area=math.pi*a*a
    print("El área del círculo de radio",a,"es:",area)
    perimetro=a*2*math.pi
    print("El perimetro del círculo de radio",a,"es:",perimetro)
    print("")
fCalculoCirculo(1.5)
fCalculoCirculo(5.4)
fCalculoCirculo(7.8)
