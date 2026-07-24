from modulos.validaciones import pedir_texto, pedir_flotante, pedir_categoria

def agregar_equipo(inventario, categorias):
    codigo = pedir_texto("Código único del equipo (ej: NB-001): ").upper()
    if buscar_equipo(inventario, codigo):
        print(f"Error: ya existe un equipo con el código {codigo}.")
        return None
    nombre = pedir_texto("Nombre del equipo: ")
    marca = pedir_texto("Marca: ").capitalize()
    categoria = pedir_categoria(categorias)
    valor = pedir_flotante("Valor del equipo en pesos: $")
    equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "marca": marca,
        "categoria": categoria,
        "valor": valor
    }
    inventario.append(equipo)
    print(f"Equipo {nombre} agregado con éxito al inventario.")
    return equipo

def listar_equipos(inventario):
    if not inventario:
        print("El inventario está vacío. Agrega equipos con la opción 1.")
        return
    print(f"\n{'CÓDIGO':<10} {'NOMBRE':<25} {'MARCA':<12} {'CATEGORÍA':<12} {'VALOR':>12}")
    print("-" * 75)
    for equipo in inventario:
        print(f"{equipo['codigo']:<10} {equipo['nombre']:<25} {equipo['marca']:<12} {equipo['categoria']:<12} ${equipo['valor']:>11.2f}")
    print(f"\nTotal de equipos registrados: {len(inventario)}")

def buscar_equipo(inventario, codigo):
    codigo = codigo.upper()
    for equipo in inventario:
        if equipo["codigo"] == codigo:
            return equipo
    return None

def eliminar_equipo(inventario, codigo):
    equipo = buscar_equipo(inventario, codigo)
    if equipo:
        inventario.remove(equipo)
        return True
    return False

def obtener_marcas_unicas(inventario):
    marcas = set()
    for equipo in inventario:
        marcas.add(equipo["marca"])
    return marcas