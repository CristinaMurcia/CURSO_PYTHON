
""" Ejercicio comparadores condicionales """

nota = int(input("Introduce la nota: "))

if nota < 5 :
    print("Suspendido")
    
elif nota == 5 :
    print("Suficiente")
    
elif nota == 6 :
    print("Bien")

elif nota <= 8 :
    print("Notable")
    
else:
    print("Excelente")