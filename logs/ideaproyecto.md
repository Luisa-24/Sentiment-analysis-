# Análisis de Sentimiento para Entrevistas

Lo que se quiere con este proyecto es tomar en audios 
entrevistas de trabajo y reuniones de seguimiento con empleados.
para transcribir grabaciones de audio, identifica a los hablantes, 
detecta preguntas y respuestas, y analiza la emocionalidad de las respuestas. 

# Estructura del proyecto

Se propone inicialmente la siguiente estructura de lo que se desea para el proyecto.

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. INGEST  │──▶│  2.CONVERT   │──▶│ 3. DIARIZE  │
│  Load audio │    │  WAV 16kHz  │    │ Who speaks? │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  6. OUTPUT  │◀── │ 5. EMOTION │ ◀──│ 4.TRANSCRIBE│
│  JSON/CSV   │    │  Analysis   │    │   Whisper   │
└─────────────┘    └─────────────┘    └─────────────┘

# Herramientas requeridas

| Componente | Tecnología | Propósito |
|---|---|---|
|conveertidor|pydub|convierte cualquier tipo de audio a wav|
| Transcripción | OpenAI Whisper v3 | Convierte de voz a texto  |
| Detección de hablantes | pyannote-audio | Identifica las personas que están hablando  |
| Procesamiento de texto | spaCy | Detectar preguntas vs. respuestas |
| Análisis de emociones | GoEmotions| Clasificar 28 emociones diferentes |



.

