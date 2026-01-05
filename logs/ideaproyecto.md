# Análisis de Sentimiento para Entrevistas

Lo que se quiere con este proyecto es tomar en audios 
entrevistas de trabajo y reuniones de seguimiento con empleados.
para transcribir grabaciones de audio, identifica a los hablantes, 
detecta preguntas y respuestas, y analiza la emocionalidad de las respuestas. 

# Estructura del proyecto

Se propone inicialmente la siguiente estructura de lo que se desea para el proyecto.

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   1. INGEST   │────▶│   2. CONVERT  │────▶│   3. DIARIZE  │
│  Cargar audio │     │  WAV 16kHz    │     │ ¿Quién habla? │
└───────────────┘     └───────────────┘     └───────────────┘
                                                    │
                                                    ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   6. OUTPUT   │◀────│  5. EMOTION   │◀────│ 4. TRANSCRIBE │
│   JSON/CSV    │     │   Análisis    │     │    Whisper    │
└───────────────┘     └───────────────┘     └───────────────┘
```

# Herramientas requeridas

| Componente | Tecnología | Propósito |
|---|---|---|
|conveertidor|pydub|convierte cualquier tipo de audio a wav|
| Transcripción | OpenAI Whisper v3 | Convierte de voz a texto  |
| Detección de hablantes | pyannote-audio | Identifica las personas que están hablando  |
| Procesamiento de texto | spaCy | Detectar preguntas vs. respuestas |
| Análisis de emociones | GoEmotions| Clasificar 28 emociones diferentes |

# Librerías usadas y para qué sirven

## Soundfile:
Librería apra manejo de archivosde audio.

- Soporta formatos como WAV, FLAC, OGG, AIFF
- Permite guardar audio en distintos formatos cpn control de parámetros

## Pydub:
Librería para manipulación  de audio, es decir, cortar, 
unir, convertir formatos, cambiar volumen, etc.

- Lee múltiples formatos: Soporta mp3, wav, OGG, etc.
- Exportar y convertir:  Transforma audios entre formatos 
- Editar segmentos: Cortar, unir, repetir o extraer partes de un audio
-Ajusta el volumen: subir o bajar volumes a decobelos en fragmentos específicos

# Explicación de módulos 

# carpeta audio_processing 
 
## Módulo convert.py : 
este módulo se encarga de convertir 
y normalizar cualquier audiio legible a WAV y guardar el resultado 
en un directorio de salida

Este módulo contiene una clase llamada AudioConverter con constantes 

- TARGET_SAMPLE_RATE = 16000 :  frecuencia de muestreo objetivo en Hz. Es necesario para que todos los WAV resultantes tengan 16 kHz (estándar para procesamiento de voz/ASR).

- TARGET_CHANNELS = 1 : número de canales objetivo. Nos es útil para modelos de voz y para reducir tamaño.

- TARGET_FORMAT = "wav" : formato de salida. Usado en audio para crear archivos WAV 
 
Además esta clase contiene dos métodos:

###   Metodo  convert :
Hace la conversion de formato completa

### Método  normalize:
 Normaliza para garantizar que todos los audios tengan el mismo formato
 antes de exportarlo a wav

# Carpeta utils

## Módulo files
El objetivo de este módulo es proporcionar utilidades comunes
para manejo de rutas y listados de archivos usadas por 
el pipeline de audio que lo que hace es asegurar directorios, crear rutas
de salida y obtener la lista de audios.

Es un módulo de funciones que contiene los siguientes métodos

 ### ensure_dir: 
este método nos es útil para garantizar que un 
directorio de salida exista antes de escribir arvhivos

### get_outpu_path: 
Encuentra archivos con la extrension indicada.
Acumula coincidencias y devuelve la lita ordenada por nombre.

### list_audio_files:
Busca en el directorio todos los archivos cuyo sufijo
coincida con cada extensión de extensions 

## Módulo audio 

El propósito de este módulo es proveer utilidades para validar 
y obtener metadatos básicos de archivos de audio y conocer un poco
la estructura de audio, como por ejemplo, cuanto dura y si el audio es 
legible o si tiene un formato conveniente 

Este módulo contiene dos métodos:

 ## get_duration: 
 como su nombre lo dice, me detecta la duración del audio

 ## validate_audio_file :
 Me valida que el audio nos es servible, legible y compatible


# Carpeta ingestion 

## Loader
El propósito de esta carpeta es hacer ciertas validaciones haciendose las siguientes
preguntas.

1. ¿ existe el archivo?
2. ¿ Es un formato soportado? (que no vaya ser pdf, .txt, etc.)
3. ¿ El adio es válido o corrupto?


# Carpeta Schemas 

Esta carpeta tiene varias clases que se encargan de lo siguiente:

### Clase Sentiment:

el proposito de esta clase es representar el resultado del análisis de emociones 
para un segmento de texto.

#### label: etiqueta de emoción
#### score: valor asociado entre 0.0 y 1.0

### Clase Segment

El propósito de esta clase es guardar el quien, cuando, que dijo,  rol y emoción. 
Tiene los siguientes atributos:

#### segment_ id: identificador único local dentro de la entrevista 
#### speaker: identificador del hablante
#### start: tiempo de inicio en srgundos
#### end: tiempo de fin en segundos
#### text: transcripción asociaa a ese intervalo
#### role: si es una pregunta o una respuesta
#### paired_repose_id : id del segmento que responde a esa pregunta
#### Sentiment: resultado del análisis de emoción

### Clase transcriptSegment 

el proposito de esta clase es representar la salida del transcriptor.
contiene los siguientes atributos 

#### start: inicio en segundos 
#### end : fin en segundos 
#### text : texto transcrito
#### información por plabra, en que segundo empieza y en cual termina 


### Clase interview

#### interviwe_id : id de la entrevista ( nombre base del archivo)
#### source_path: ruta de audio original 
#### processed_path: ruta a arcivo procesado 
#### metadata: dict_metadatos ( duracióm, sample_rate, size, decha, etc.)

También se crea el módulo diarización, convert y loader siguiendo la propuesra estructural dada.
No he añadido carpetas diferentes ni módulos diferentes, todo lo he hecho en base a la propuesta
siguiendo y respetando la ruta. 



A



















.

