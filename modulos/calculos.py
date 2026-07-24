TASA_DEPRECIACION = 0.20

def calcular_depreciacion(valor, anios):
    if anios == 0:
        return valor
    valor_reducido = valor * (1 - TASA_DEPRECIACION)
    return calcular_depreciacion(valor_reducido, anios - 1)

def valor_total_inventario(inventario):
    total = 0
    for equipo in inventario:
        total += equipo["valor"]
    return total