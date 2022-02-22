#ENTRADAS
import math

a = int (input("Escribe el valor de a = "))
b = int (input("Escribe el valor de b= "))
c = int (input("Escribe elvalor de c= "))


#PROCESOS
X1= (-b - math.sqrt((b**2)-(4*a*c))) / (2*a)
X2= (-b + math.sqrt((b**2)-(4*a*c))) /(2*a)



#SALIDAS
print(f"Resultado de Fórmula general b positva = {X1}")
print(f"Resultado de Fórmula general b negativa = {X2}")