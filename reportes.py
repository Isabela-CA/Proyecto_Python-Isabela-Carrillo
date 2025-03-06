import json

def cargar_datos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def calcular_crecimiento(anterior, actual):
    if anterior is None:
        return "N/A"
    crecimiento = ((actual - anterior) / anterior) * 100
    icono = "⬆️" if crecimiento > 0 else "⬇️"
    return f"{crecimiento:.2f}% {icono}"

def filtrar_poblacion(datos, pais, anios, id_indicador, estado):
    # Se filtra por estado "disponible"
    filtrados = [d for d in datos if d["estado"] == estado]
    
    if pais and pais.lower() != "todos":
        filtrados = [d for d in filtrados if d["pais"].lower() == pais.lower()]
    
    if anios:
        if len(anios) == 1:
            filtrados = [d for d in filtrados if d["ano"] == anios[0]]
        elif len(anios) == 2:
            filtrados = [d for d in filtrados if anios[0] <= d["ano"] <= anios[1]]
    
    if id_indicador and id_indicador.lower() != "todos":
        filtrados = [d for d in filtrados if d["indicador_id"].lower() == id_indicador.lower()]
    
    return filtrados

def generar_reporte_poblacion(pais="todos", anios=[], id_indicador="todos", estado="D"):
    datos = cargar_datos("poblacion.json")
    datos_filtrados = filtrar_poblacion(datos, pais, anios, id_indicador, estado)
    
    poblacion_por_pais = {}
    for d in datos_filtrados:
        if d["pais"] not in poblacion_por_pais:
            poblacion_por_pais[d["pais"]] = []
        poblacion_por_pais[d["pais"]].append({"ano": d["ano"], "valor": d["valor"]})
    
    resultado = "Población Total:\n"
    resultado += "Pais Población\n"
    for pais_key, valores in poblacion_por_pais.items():
        total_poblacion = sum(v["valor"] for v in valores)
        resultado += f"{pais_key:<20}{total_poblacion}\n"
    ancho =20
    for pais_key, valores in poblacion_por_pais.items():
        valores.sort(key=lambda x: x["ano"])
        resultado += f"\n{pais_key}\n"
        resultado += f"{"Año".center(ancho, " ")}{"Población".center(ancho, " ")}{"Crecimiento".center(ancho," ")}\n"
        anterior = None
        for v in valores:
            crecimiento = calcular_crecimiento(anterior, v["valor"])
            resultado += f"{str(v['ano']).center(ancho, " ")}{str(v['valor']).center(ancho, " ")}{str(crecimiento).center(ancho, " ")}\n"
            anterior = v["valor"]
    
    return resultado

def pedir_datos():
    pais = input("Ingrese el país (o 'todos' para todos): ")
    anios_input = input("Ingrese un año o un rango de años (ejemplo: 2010 o 2010,2020): ")
    if anios_input.strip() == "":
        anios = []
    else:
        try:
            # Si hay coma se asume rango, sino, se toma como año único
            if "," in anios_input:
                anios = [int(x.strip()) for x in anios_input.split(",")]
            else:
                anios = [int(anios_input.strip())]
        except Exception as e:
            print("Error al procesar el/los año(s). Se usará la lista vacía.")
            anios = []
    id_indicador = input("Ingrese el id del indicador (o 'todos'): ")
    estado = input("Ingrese el estado (D para disponible, ND para no disponible): ").lower()
    estado = "disponible" if estado == "d" else "no disponible"
    reporte = generar_reporte_poblacion(pais, anios, id_indicador, estado)
    print(reporte)
    return reporte