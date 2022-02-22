#ENTRADAS
Cls = int (input("Escriba los grados Celsius: "))
Frn = int (input ("Escriba los grados Fahrenheit: "))
Kvn = int (input("Escriba los grados Kelvin: "))

#PROCESOS
Cls = (Frn -32)/1.8
Frn = Cls * 1.8 + 32
Kvn = Cls + 273.15
Kvn = 5/9*(Frn-32)+273.15
Cls = Kvn - 273.15
Frn = 1.8*(Kvn-273.15)+32



#SALIDAS
print(f"Conversion de grados Fahrenheit a grados Celsius = {Cls}")
print(f"Conversion de grados Celsius a grados Fahrenheit = {Frn} ")
print (f"Conversion de grados Celsius a grados Kelvin = {Kvn}")
print(f"Conversion de grados Fahrenheit a grados Kelvin = {Frn}")
print(f"Conversion de grados Kelvin a grados Celsius = {Kvn}")
print(f"Conversion de grados Kelvin a grados Fahrenheit = {Kvn}")