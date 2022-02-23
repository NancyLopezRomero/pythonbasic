#ENTRADAS

metros = float (input("Escribe el nivel de agua en metros de la cisterna: "))

#PROCESOS

if (metros < 0): 
    print("Fuga en cisterna")
elif (metros ==0):
    print("Encender bomba de agua")
elif (metros >0 and metros <= 2):
    print("Acelerar bomba de agua")
elif (metros >2 and metros <=4):
        print("Bomba trabajando")
elif (metros >4 and metros <6):
        print("Desacelerar Bomba")
elif (metros == 6):
    print("Apagar bomba")
elif (metros >6):
    print ("Desbordamiento de agua en cisterna")    