from modulos.validaciones import pedir_entero, pedir_texto, pedir_flotante
from modulos.gestor import agregar_equipo, listar_equipos, buscar_equipo, eliminar_equipo, obtener_marcas_unicas
from modulos.calculos import calcular_depreciacion
from modulos.reportes import generar_reporte_csv

CATEGORIAS = ("Notebook", "Monitor", "Teclado", "Mouse", "Impresora")

inventario = []

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO TECNOLÓGICO =====")
    print("1. Agregar equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo por código")
    print("4. Eliminar equipo")
    print("5. Calcular depreciación de un equipo")
    print("6. Ver marcas registradas")
    print("7. Generar reporte CSV")
    print("8. Salir")

def ejecutar():
    print("Bienvenida al Sistema de Gestión de Inventario Tecnológico")
    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción (1-8): ", 1, 8)
        if opcion == 1:
            agregar_equipo(inventario, CATEGORIAS)
        elif opcion == 2:
            listar_equipos(inventario)
        elif opcion == 3:
            codigo = pedir_texto("Ingresa el código del equipo: ")
            equipo = buscar_equipo(inventario, codigo)
            if equipo:
                print(f"Encontrado: {equipo['nombre']} | Marca: {equipo['marca']} | Valor: ${equipo['valor']:.2f}")
            else:
                print("No existe un equipo con ese código.")
        elif opcion == 4:
            codigo = pedir_texto("Código del equipo a eliminar: ")
            eliminado = eliminar_equipo(inventario, codigo)
            if eliminado:
                print(f"El equipo {codigo} fue eliminado correctamente.")
            else:
                print("No se pudo eliminar: el código no existe.")
        elif opcion == 5:
            codigo = pedir_texto("Código del equipo: ")
            equipo = buscar_equipo(inventario, codigo)
            if not equipo:
                print("Ese código no está registrado.")
                continue
            anios = pedir_entero("¿Cuántos años quieres proyectar?: ", 1, 20)
            valor_final = calcular_depreciacion(equipo["valor"], anios)
            print(f"El equipo {equipo['nombre']} valdrá ${valor_final:.2f} en {anios} años.")
        elif opcion == 6:
            marcas = obtener_marcas_unicas(inventario)
            if marcas:
                print("Marcas registradas en el inventario:")
                for marca in marcas:
                    print(f"- {marca}")
            else:
                print("Aún no hay equipos registrados.")
        elif opcion == 7:
            generar_reporte_csv(inventario)
        else:
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    ejecutar()