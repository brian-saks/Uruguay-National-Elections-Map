import csv
import requests
import os

# Definir la clase Local
class Local:
    def __init__(self, nombre_local, direccion_local, latitud, longitud, circuitos):
        self.nombre_local = nombre_local
        self.direccion_local = direccion_local
        self.latitud = latitud
        self.longitud = longitud
        self.circuitos = circuitos

def procesar_csv(file_path):
    locales = []
    current_local = None

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            nombre_local = row['Local']
            direccion_local = row['DIRECCION']
            latitud = float(row['Latitud'].replace(',', '.'))
            longitud = float(row['Longitud'].replace(',', '.'))
            circuito = int(row['NÚMERO'])

            # Si current_local es None o el local actual es diferente del último local procesado
            if current_local is None or current_local.nombre_local != nombre_local:
                if current_local is not None:
                    locales.append(current_local)

                # Crear un nuevo objeto Local
                current_local = Local(
                    nombre_local=nombre_local,
                    direccion_local=direccion_local,
                    latitud=latitud,
                    longitud=longitud,
                    circuitos=[circuito]
                )
            else:
                # Añadir el circuito al objeto Local actual
                current_local.circuitos.append(circuito)

        # Añadir el último objeto Local procesado
        if current_local is not None:
            locales.append(current_local)
    
    return locales