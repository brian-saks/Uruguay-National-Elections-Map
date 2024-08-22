import folium
from folium.plugins import Search
import convertor


file_path = 'archivos/MONTEVIDEO FINAL - Hoja 1.tsv'

# Obtain Local objects from the TSV file
locales = convertor.procesar_tsv(file_path)

# Convert Local objects to the data array format
data = []

for local in locales:
    data.append({
        "name": local.nombre_local,
        "address": local.direccion_local,
        "circuits": local.circuitos,
        "coordinates": [local.latitud, local.longitud]
    })

# Create a map centered on Uruguay
uruguay_map = folium.Map(location=[-32.5228, -55.7658], zoom_start=7)

# Create a feature group for markers
marker_group = folium.FeatureGroup(name='Markers').add_to(uruguay_map)

# Generate markers and popups for each entry in the data array
for item in data:
    # Create the HTML content for the popup with adjusted styles
    html = f"""
    <div style="font-family: Arial; font-size: 11px;">
        <h2 style="font-size: 16px; font-weight: bold;">{item['name']}</h2>
        <h4 style="font-size: 12px; font-style: italic;">{item['address']}</h4>
        <p><strong>Circuits:</strong></p>
        <ul>
            {''.join([f'<li>{circuit}</li>' for circuit in item['circuits']])}
        </ul>
    </div>
    """

    # Create and add the marker with the popup to the feature group
    folium.Marker(
        location=item['coordinates'],
        popup=folium.Popup(html, max_width=500),  # Adjust the maximum width of the popup
        icon=folium.Icon(icon='search'),
        name=item['name']  # Name for the search functionality
    ).add_to(marker_group)

# Add the search plugin
search = Search(
    layer=marker_group,  # Use the feature group for search
    search_label='name',  # Use the marker name for the search
    placeholder='Search by center ...',
    collapsed=False,
    position='topleft',
    search_zoom=15
).add_to(uruguay_map)

# Save the map to an HTML file
uruguay_map.save("uruguay_map.html")