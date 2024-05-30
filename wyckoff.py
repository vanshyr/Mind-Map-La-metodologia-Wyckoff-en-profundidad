import numpy as np


def indicador_leyes_wyckoff(precios_cierre):
    # Calcula el precio medio
    average_price = np.mean(precios_cierre)

    # Calcula el precio mas alto
    highest_price = np.max(precios_cierre)

    # Calcula el precio mas bajo
    lowest_price = np.min(precios_cierre)

    # Calcular el valor del indicador basado en las tres leyes de Wyckoff
    if average_price > highest_price:
        valor_indicador = 1  # Ley de la oferta
    elif average_price < lowest_price:
        valor_indicador = -1  # Ley de la demanda
    else:
        valor_indicador = 0  # Ley de causa y efecto

    return valor_indicador


# Ejempl de uso
precios_cierre = [10, 12, 8, 14, 9]
valor_indicador = indicador_leyes_wyckoff(precios_cierre)
print("Indicador leyes Wyckoff:", valor_indicador)
