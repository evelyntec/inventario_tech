def pedir_entero(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        try:
            numero = int(entrada)
        except ValueError:
            print("Error: debes ingresar un número entero. Inténtalo de nuevo.")
            continue
        if numero < minimo or numero > maximo:
            print(f"Error: el número debe estar entre {minimo} y {maximo}.")
            continue
        return numero

def pedir_flotante(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
        except ValueError:
            print("Error: debes ingresar un valor numérico, por ejemplo 199990.50")
            continue
        if numero <= 0:
            print("Error: el valor debe ser mayor que cero.")
            continue
        return numero

def pedir_texto(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("Error: este campo no puede quedar vacío.")
            continue
        return entrada

def pedir_categoria(categorias):
    print("Categorías disponibles:")
    for indice, categoria in enumerate(categorias, start=1):
        print(f"{indice}. {categoria}")
    posicion = pedir_entero("Elige el número de la categoría: ", 1, len(categorias))
    return categorias[posicion - 1]