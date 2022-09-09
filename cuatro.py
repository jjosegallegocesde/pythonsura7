# crear menú empanadas 
contador=0
empanadas=[]

print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. SALIR")

while(contador !=3):
    ingredientes=[]
    empanada={}
    contador=int(input("Digite la opción: "))
    if (contador==1):
        empanada['Nombre']=input("ingrese nombre empanada: ")
        for i in range (3):
            ingredientes.append(input(f"digite el ingrediente {i+1}: "))
        
        empanada['ingredientes']=ingredientes
        empanada['precio']=int(input("ingrese el precio: $"))
        empanadas.append(empanada)
        print("Agregando empanada")

    elif (contador==2):
        print("Mostrar empanadas")
        print(empanadas)
    elif (contador==3):
        print("SALIR")
        break

    else: 
        print("Opción Invalida")


