#ENTRADAS

número = int (input ("Escriba un número: "))

if número < 0 and número > -100:
    for i in range (-1,-100,-2): #números impares de forma DESCENDENTE
        print (i)
elif número >0 and número < 100: #números pares de forma ASCENDENTE
    for i in range (2, 100, 2):
        print (i)
else:
    print ("No válido")

