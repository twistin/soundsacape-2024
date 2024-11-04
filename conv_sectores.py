import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv(
    "/Users/sdcarr/Documents/CityNet/files-csv-predictions/prediction_summaries_castro.csv")

# Definir colores según tus especificaciones
# Verde para biótico, azul oscuro para antropogénico
colores = ['#228B22', '#1E90FF']

# Itera sobre cada nombre de archivo único
for nombre_archivo in df['Filename'].unique():
    # Filtra los datos para el nombre de archivo actual
    data = df[df['Filename'] == nombre_archivo]

    # Extrae los valores para los gráficos de sectores
    valores = data[['Average biotic sound',
                    'Average anthropogenic sound']].iloc[0]

    # Nombres de las etiquetas de los sectores
    etiquetas = ['Origen biótico', 'Origen antropogénico']

    # Configuración del gráfico de sectores
    plt.figure(figsize=(6, 6))  # Tamaño del gráfico
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%',
            startangle=140, colors=colores)
    plt.title(f'Gráfico de sectores para {nombre_archivo}')
    plt.axis('equal')  # Aspecto de círculo

    # Guardar el gráfico en una carpeta específica
    nombre_grafico = f'{nombre_archivo}_pie_chart.png'
    ruta_guardado = "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/" + \
        nombre_grafico  # Reemplaza 'tu_ruta_de_carpeta/' con la ruta deseada
    plt.savefig(ruta_guardado)  # Guardar como PNG en la carpeta especificada

    # Mostrar el gráfico (opcional)
    plt.show()

    # Cierra la figura para liberar memoria
    plt.close()
