import folium
from geopy.geocoders import Nominatim
import simpleaudio as sa
import librosa

# Inicializa el geolocalizador
geolocator = Nominatim(user_agent="SoundScapes/1.0 (sarerac@gmail.com)")

# Define una función para obtener la latitud y longitud de una dirección
def get_location(address):
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)

# Define una función para reproducir audio
def play_audio(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Define una función para analizar audio y devolver sus características
def analyze_audio(file_path):
    # Carga el archivo de audio
    y, sr = librosa.load(file_path)
    
    # Obtiene las características
    sound_level = librosa.feature.rms(y=y).mean()
    biotic_features = librosa.feature.spectral_contrast(y=y, sr=sr)
    anthropogenic_features = librosa.feature.zero_crossing_rate(y=y)
    
    return sound_level, biotic_features, anthropogenic_features

# Crea un objeto de mapa
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Datos de ejemplo: lista de tuplas (dirección, ruta del archivo de audio)
locations = [
    ("Portland", "bird.wav", "dario.jpg"),
    ("Beaverton", "bird.wav", "dario.jpg"),
    # Añade más localizaciones y archivos de audio correspondientes
]

# Añade marcadores al mapa
for address, audio_file, image_file in locations:
    lat, lon = get_location(address)
    sound_level, biotic_features, anthropogenic_features = analyze_audio(audio_file)
    
    # Crea un popup con las características de audio
    popup_content = f"""
    <h4>{address}</h4>
    <p>Nivel Sonoro: {sound_level:.2f} dB</p>
    <p>Características Bióticas: {biotic_features.mean():.2f}</p>
    <p>Características Antropogénicas: {anthropogenic_features.mean():.2f}</p>
    <img src="{image_file}" alt="Imagen de {address}" width="200">
    <audio controls>
      <source src="{audio_file}" type="audio/wav">
      Tu navegador no soporta el elemento de audio.
    </audio>
    """
    popup = folium.Popup(popup_content, max_width=300)
    
    # Añade el marcador al mapa
    folium.Marker([lat, lon], popup=popup).add_to(m)

# Guarda el mapa en un archivo HTML
m.save('soundscapes_map.html')

# Mensaje de éxito
print("El mapa de soundscapes ha sido creado con éxito y guardado como soundscapes_map.html.")
