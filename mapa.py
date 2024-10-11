import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Cambia esta ruta a la ubicación exacta de tu archivo .shp
ruta_mapa = "C:/Users/Pablo/Documents/TUTORIAL/ne_110m_admin_0_countries.shp"

# Cargar el archivo desde la ruta local
world = gpd.read_file(ruta_mapa)

# Definir países clave en términos de tamaño y economía
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

# Crear el mapa de calor centrado en los países clave
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(column='GDP_Trillions', ax=ax, legend=True, cmap='OrRd', edgecolor='black')

# Ajustar título y leyendas
ax.set_title('Mapa de Calor de los Países con Mayor Economía y Tamaño Territorial', fontsize=15)
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

plt.show()
