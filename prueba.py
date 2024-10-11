import geopandas as gpd

ruta_mapa = "C:/Users/Pablo/Documents/TUTORIAL/ne_110m_admin_0_countries.shp"
world = gpd.read_file(ruta_mapa)
print(world.columns)
