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

def procesar_tsv(file_path):
    locales = []
    with open(file_path, newline='', encoding='utf-8') as tsvfile:
        # Usar el delimitador de tabulación para TSV
        reader = csv.DictReader(tsvfile, delimiter='\t')
        current_local = None
        latitud = None
        longitud = None

        for row in reader:
            nombre_local = row['Local']
            direccion_local = row['DIRECCION']
            latitud_str = row['Latitud']
            longitud_str = row['Longitud']
            circuito = int(row['NÚMERO'])

            # Si current_local es None o el local actual es diferente del último local procesado
            if current_local is None or current_local.nombre_local != nombre_local:
                if current_local is not None:
                    if latitud is not None and longitud is not None:
                        current_local.latitud = latitud
                        current_local.longitud = longitud
                        locales.append(current_local)
                    else:
                        print(f"Error: {current_local.nombre_local} no tiene coordenadas válidas.")
                
                # Resetear para el nuevo local
                current_local = Local(
                    nombre_local=nombre_local,
                    direccion_local=direccion_local,
                    latitud=None,
                    longitud=None,
                    circuitos=[circuito]
                )
                latitud = None
                longitud = None
            else:
                # Añadir el circuito al objeto Local actual
                current_local.circuitos.append(circuito)

            # Convertir latitud y longitud de string a float reemplazando comas por puntos
            if latitud_str != "#ERROR!" and longitud_str != "#ERROR!":
                try:
                    latitud = float(latitud_str.replace(',', '.'))  # Reemplazar la coma por punto
                    longitud = float(longitud_str.replace(',', '.'))  # Reemplazar la coma por punto
                except ValueError:
                    print(f"Error al convertir coordenadas para {nombre_local}: {latitud_str}, {longitud_str}")
                    latitud = None
                    longitud = None
            else:
                latitud = None
                longitud = None
        
        # Añadir el último objeto Local procesado
        if current_local is not None:
            if latitud is not None and longitud is not None:
                current_local.latitud = latitud
                current_local.longitud = longitud
                locales.append(current_local)
            else:
                print(f"Error: {current_local.nombre_local} no tiene coordenadas válidas.")
    
    return locales