import folium
import simpleaudio as sa
import librosa

# Define una función para reproducir audio


def play_audio(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = play_obj.play()
    play_obj.wait_done()

# Define una función para analizar audio y devolver sus características


def analyze_audio(file_path):
    # Carga el archivo de audio
    y, sr = librosa.load(file_path)

    # Obtiene las características
    sound_level = librosa.feature.rms(y=y).mean()
    biotic_features = librosa.feature.spectral_contrast(y=y, sr=sr)
    anthropogenic_features = librosa.feature.zero_crossing_rate(y=y)

    return sound_level, biotic_features.mean(), anthropogenic_features.mean()

# Crea un objeto de mapa


location = [42.23282, -8.72264]
zoom_start = 13
# m = folium.Map(location=[42.23282, -8.72264], zoom_start=13,)
m5 = folium.Map(location=location, control_scale=True, zoom_start=zoom_start, tiles='CartoDB positron',
                attr='Map data © OpenStreetMap contributors, CC-BY-SA, Imagery © CartoDB')

'''
icon = folium.CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
   # Datos de ejemplo: lista de tuplas (coordenadas, nombre del lugar, archivo de audio, archivo de imagen, archivo de gráfico
)

'''


url = "https://leafletjs.com/examples/custom-icons/{}".format
icon_image = url("leaf-red.png")
shadow_image = url("leaf-shadow.png")

icon = folium.CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76),
)

'''folium.Marker(
    location=[45.3288, -121.6625], icon=icon, popup="Mt. Hood Meadows"
).add_to(m)

m'''


locations = [
    ([42.2309009, -8.7254402], "Mirador-Fortaleza-Vista_Plaza", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/1_part005.wav",
     "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/1_mirador_plaz_españa.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0010_LR_part005.wav_pie_chart.png"),
    ([42.2311563, -8.7263736], "Frente al repetidor", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/2_part005.wav",
     "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/2_frente_repetidor.jpg",
     "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0011_LR_part005.wav_pie_chart.png"),
    ([42.2320503, -8.7267662], "Junto al muro fortaleza mirador ria",
     "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/3_part005.wav", "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/3_mirador_ria.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0012_LR_part005.wav_pie_chart.png"),
    ([42.2332685, -8.7265998],"Anclas Galeones", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/4_part002.wav", "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/4_anclas_galeones.jpg",
     "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0013_LR_part002.wav_pie_chart.png" ),
    ([42.2332401, -8.7270673], "Sendero bajo estanque las anclas", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/5_part008.wav",
     "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/5_paseo_bajo_anclas.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0014_LR_part008.wav_pie_chart.png"),
    ([42.2331607, -8.7256001],"Rincon fuera del sendero con fondo a Guía","/Users/sdcarr/Desktop/soundscape-2024/audio/castro/6_part005.wav", "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/6_rincon_vista_frente_aguia.jpg",
     "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0015_LR_part005.wav_pie_chart.png"),
    ([42.2298972, -8.7229534], "Rincon bajo el parque infantil", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/7_part005.wav",
     "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/7_rincon_bajo_parque.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0016_LR_part005.wav_pie_chart.png"),
    ([42.2296656, -8.7236086], "Promontorio sobre el parque infantil", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/8_part005.wav", "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/8_promontorio_parque.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0017_LR_part005.wav_pie_chart.png" ),
    ([42.2303284, -8.7257982], "Sendero sobre el vivero de plantas", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/9_part005.wav", "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/9_sendero_vivero.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0018_LR_part005.wav_pie_chart.png"
    ),
    ([42.2302209, -8.7266387], "MiradorPlaza Martín Codax", "/Users/sdcarr/Desktop/soundscape-2024/audio/castro/10_part005.wav",
     "/Users/sdcarr/Desktop/soundscape-2024/imagenes/CASTRO/10_mirador_martin_codax.jpg", "/Users/sdcarr/Desktop/soundscape-2024/sectores-pandas/castro/ZOOM0019_LR_part005.wav_pie_chart.png")
    
]

# Añade marcadores al mapa
for coordinates, place_name, audio_file, image_file, graph_file in locations:
    lat, lon = coordinates

    # Analiza el archivo de audio y obtiene características
    sound_level, biotic_features, anthropogenic_features = analyze_audio(
        audio_file)

    # Crea un popup con las características de audio y la imagen del gráfico
    popup_content = f"""
    <h4>{place_name}</h4>
    <p>Nivel Sonoro: {sound_level:.2f} dB</p>
    <p>Características Bióticas: {biotic_features:.2f}</p>
    <p>Características Antropogénicas: {anthropogenic_features:.2f}</p>
    <img src="{image_file}" alt="Imagen de {place_name}" width="200">
    <br>
    <img src="{graph_file}" alt="Gráfico" width="300">
    <br>
    <audio controls>
      <source src="{audio_file}" type="audio/wav">
      Tu navegador no soporta el elemento de audio.
    </audio>
    """

    popup = folium.Popup(popup_content, max_width=400)

    # Añade el marcador al mapa
    folium.Marker([lat, lon], popup=popup).add_to(m5)

# Guarda el mapa en un archivo HTML
m5.save('soundscapes_map.html')

# Mensaje de éxito
print("El mapa de soundscapes ha sido creado con éxito y guardado como soundscapes_map.html.")
