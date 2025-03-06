#funciones de reportes 
import json
from reportes import *

#se carga el archivo datos 
def cargar_datos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8" ) as archivo:
        json.dump(datos, archivo, indent=4 )

def nuevos_elementos_json(archivo, nuevo_elemeno):
    datos = cargar_datos(archivo)
    datos.append(nuevo_elemeno)
    guardar_datos(archivo,datos)
    return cargar_datos(archivo)

def devolvelr_codigo_iso3(pais):
    paises = {pais["nombre"]:[pais["codigo_iso"],pais["codigo_iso3"] ] for pais in cargar_datos("paises.json")}
    if pais in paises:
        return paises[pais][1]
    else:
        return input("Ingrese Codigo ISO 3: ").upper()

def devolver_descripcion(indicador):
    indicadores = {indicador["id_indicador"]:indicador["descripcion"] for indicador in cargar_datos("indicadores.json")}
    if indicador in indicadores:
        return indicadores[indicador]
    else:
        return input("Ingrese La descripcion del indicador: ").capitalize()

# mirar lista de los paises registrados opc 1
def validar_paises(pais_validar):
    paises = [pais["nombre"] for pais in cargar_datos("paises.json")]
    if pais_validar in paises:
        return True
    else:
        return False
    
# agregar pais opc 2
def agregar_nuevo_pais():
    nombre = input("ingrese nombre del pais: ")
    codigo_iso = input("ingrese codigo iso : ")
    codigo_iso3 = input("ingrese codigo_iso3: ")

    nombre = {
        "nombre": nombre.capitalize(),
        "codigo_iso": codigo_iso.upper(),
        "codigo_iso3": codigo_iso3.upper()
    }

    if validar_paises(nombre["nombre"]):
        print("el pais ya existe en la base de datos paises")
    else:
        nuevos_elementos_json("paises.json", nombre)

#########################################################

# agregar nueva poblacion opc 3
def agregar_poblacion():

    ano = int(input("ingrese el año de la poblacion que quiere agregar ")) 
    pais =str(input("ingrese nombre del pais: ")).capitalize()
    codigo_iso = devolvelr_codigo_iso3(pais)
    indicador = str(input("ingrese id indicador: ")).capitalize()
    descripcion = devolver_descripcion(indicador)
    valor = input("ingrese la cantidad de poblacion en " + {pais}  )
    estado = input(str("ingrese el estado (disponible/no disponible): "))
    unidad =  input(str("ingrese la unidad en la cual esta la poblacion: "))

    poblacion = {
        "ano":ano,
        "pais": pais,
        "codigo_iso3": codigo_iso,
        "indicador_id": indicador,
        "descripcion": descripcion,
        "valor":valor,
        "estado": estado,
        "unidad": unidad
    }    
    nuevos_elementos_json("poblacion.json", poblacion)

