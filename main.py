import json
from funciones import *
from reportes import *

while True:
        print("\n******** MENÚ INS.ESTADISTICAS GLOBALES ********")
        # opc1. se despliega una lista de los paises ingresados 
        print("1. Lista de paises registrados")
        print("2. Registrar pais")
        print("3. Registrar poblacion")
        #print("4. Informe")
        #opc5. se muestran todas las condiciones  a la a-y para el pais que quiere saber
        print("4. Reporte")
        #print("6. Crecimiento poblacional")
        print("0. para salir ")
        opc = input("Ingrese la opcion que necesita saber: ")
        
        
        if opc == "1":
            paises = cargar_datos("paises.json")
            for pais in paises:
                 print(pais)
        
        if opc == "2":
            agregar_nuevo_pais()
                 
        if opc == "3":
            agregar_poblacion()
            #agregar poblacion como en la funcion

        if opc == "4":
            pedir_datos()

        if opc == "0":
             print("saliendo...")
        
             
if __name__ == "__main__": 
    main()