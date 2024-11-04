1. **Grabar el audio**:
   
   - Esto puede hacerse utilizando grabadoras de audio o dispositivos móviles.
   - Asegúrate de etiquetar cada grabación con la categoría correspondiente (por ejemplo, “tráfico”, “aves”, “construcción”, etc.).

2. **Conversión de audio a espectrograma Mel**:
   
   - Los espectrogramas Mel son una representación común para el análisis de audio.
   - Utiliza la librería `librosa` para cargar tus grabaciones de audio y convertirlas en espectrogramas Mel.
   - [La escala Mel es una transformación logarítmica de la frecuencia que imita nuestra percepción auditiva humana](https://ichi.pro/es/aprendiendo-del-audio-la-escala-mel-los-espectrogramas-mel-y-los-coeficientes-cepstrales-de-frecuencia-mel-269883587896488)[1](https://ichi.pro/es/aprendiendo-del-audio-la-escala-mel-los-espectrogramas-mel-y-los-coeficientes-cepstrales-de-frecuencia-mel-269883587896488).

3. **Extraer ventanas del espectrograma**:
   
   - Divide cada espectrograma en ventanas de 21 columnas de ancho (representando 1 segundo de audio).
   - Estas ventanas serán tus entradas para la red neuronal convolucional (CNN).

4. **Aplicar alguna estrategia de normalización**:
   
   - Normaliza tus datos para que tengan una escala similar.
   - Puedes utilizar técnicas como la normalización Z-score o la normalización min-max.

5. **Aplicar el clasificador CNN**:
   
   - Crea un modelo de clasificación utilizando Fastai y PyTorch.
   - Define tu arquitectura de CNN (por ejemplo, usando resnet34) y entrena el modelo con tus datos etiquetados.

Aquí hay un ejemplo simplificado de cómo podrías comenzar:

```python
# Instala las librerías necesarias
!pip install fastai

# Importa las librerías
from fastai.vision.all import *
import librosa

# Carga tus datos y crea el DataBlock
# (Asegúrate de organizar tus archivos de audio en carpetas según las categorías)
data = ImageDataLoaders.from_folder(path, item_tfms=Resize(460), batch_tfms=aug_transforms(), bs=64)

# Crea un modelo de clasificación
learn = cnn_learner(data, resnet34, metrics=accuracy)

# Entrena el modelo
learn.fine_tune(epochs=10)
```
