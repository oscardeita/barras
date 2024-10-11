import pandas as pd
import matplotlib.pyplot as plt

# Datos de uso de ChatGPT en porcentajes globales
data = {
    'Uso': ['Creación de Contenido', 'Soporte al Cliente', 'Educación', 
            'Asistencia en Programación', 'Traducción', 'Investigación', 'Entretenimiento'],
    'Porcentaje': [70, 60, 55, 50, 45, 40, 35]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['Uso'], df['Porcentaje'], color='skyblue')
plt.xlabel('Uso de ChatGPT')
plt.ylabel('Porcentaje de Uso Global (%)')
plt.title('Usos Principales de ChatGPT a Nivel Global')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
