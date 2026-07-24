import csv
from datetime import datetime
from modulos.calculos import calcular_depreciacion, valor_total_inventario

def generar_reporte_csv(inventario):
    if not inventario:
        print("No hay datos para exportar. Agrega equipos primero.")
        return None
    nombre_archivo = "reporte_inventario.csv"
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Codigo", "Nombre", "Marca", "Categoria", "Valor Actual", "Valor en 3 anios"])
        for equipo in inventario:
            valor_futuro = calcular_depreciacion(equipo["valor"], 3)
            escritor.writerow([
                equipo["codigo"],
                equipo["nombre"],
                equipo["marca"],
                equipo["categoria"],
                f"{equipo['valor']:.2f}",
                f"{valor_futuro:.2f}"
            ])
        escritor.writerow([])
        escritor.writerow(["Total de equipos", len(inventario)])
        escritor.writerow(["Valor total del inventario", f"{valor_total_inventario(inventario):.2f}"])
        escritor.writerow(["Fecha de generacion", datetime.now().strftime("%d-%m-%Y %H:%M")])
    print(f"Reporte generado con éxito: {nombre_archivo}")
    return nombre_archivo