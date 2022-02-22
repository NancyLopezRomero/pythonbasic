#Importar una librería defunciones matemáticas
import math
# ENTRADAS DE DATOS
# Obtener los 2 números

número1 = int(input("escribe un número: ")) #Input ingresa valores de Texto
número2 = int(input("Escribe otro número: "))





# PROCESOS (Operaciones, cálculos matemáticos y Lógicos)
# Operaciones de los dos números

suma = número1 + número2
resta = número1 - número2
multiplicación = número1 * número2
división = número1 / número2
potencia1 = número1 ** número2
potencia2= pow(número1, número2)
cuadrado = pow(número1,2) #número1**2
cubo = pow(número2,3) #número1**3
raíz_cuadrada1 = pow(número1, 1/2)
raíz_cuadrada2 = math.sqrt(9)
raíz_cúbica= pow(número2,1/3)
módulo_residuo = (número1 % número2)
modulo2 = 9 % 2

# SALIDAS DE DATOS
# Resultado de las operaciones

print("La suma =", suma)
print("La suma = "+str(suma))# concatenar
print(f"La suma = {suma}") # interpolación
print("La resta = ", resta)
print("La resta = "+str(resta)) # concatenar
print(f"La resta = {resta}") # interpolación
print("La multiplicación = ", multiplicación)
print("La multiplicacion = " +str(multiplicación)) # concatenar
print(f"La multiplicación = {multiplicación}") # interpolación
print("La división =", división)
print("La división =" + str(división))
print(f"La división ={división}")
print("La potencia1 = ", potencia1)
print("La potencia1 = " + str(potencia1))
print(f"La potencia1 = {potencia1}")
print("La potencia 2 = ", potencia2)
print("La potencia2 = "+ str(potencia2))
print(f"La potencia2 = {potencia2}")
print("El cuadrado = ", cuadrado)
print("El cuadrado = " + str (cuadrado))
print(f"El cuadrado = {cuadrado}")
print("El cubo = ", cubo)
print("El cubo = " + str(cubo))
print(f"El cubo = {cubo}")
print("La raíz cuadrada = " , raíz_cuadrada1)
print(f"modulo_residuo = {módulo_residuo}")
print(f"residuo = {modulo2}")
