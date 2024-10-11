import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos del mapa mundial
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Definir países clave en términos de tamaño y economía
# Datos ficticios de ejemplo (se pueden reemplazar con datos reales)
key_countries = {
    'China': 16.8,
    'United States': 22.7,
    'India': 3.2,
    'Russia': 4.2,
    'Brazil': 1.9,
    'Australia': 1.4,
    'Canada': 1.7,
    'Japan': 4.9,
    'Germany': 5.5
}

# Convertir los datos a un DataFrame
data = pd.DataFrame(list(key_countries.items()), columns=['name', 'GDP_Trillions'])

# Unir los datos de economía con el mapa mundial
world = world.merge(data, on='name', how='left')

# Crear un mapa de calor centrado en los países clave
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(column='GDP_Trillions', ax=ax, legend=True, cmap='OrRd', edgecolor='black')

# Ajustar título y leyendas
ax.set_title('Mapa de Calor de los Países con Mayor Economía y Tamaño Territorial', fontsize=15)
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

plt.show()
