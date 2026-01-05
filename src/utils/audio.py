""" El propósito de este módulo es
obtener información sobre audios y  validar archivos de audio.

Args : Ruta al archivo de audio
Returns: Duración del audio en segundos 
         y validación del archivo de audio"""

# Estándar
from pathlib import Path  

import soundfile as sf 

from pydub import AudioSegment 
 
"""Módulo de funciones para procesamiento de audio.

Args: Ruta al archivo de audio
Returns: Duración del archivo de audio en segundos. """

SUPPORTED_FORMATS = (".wav", ".mp3", ".m4a", ".flac", ".ogg", ".webm")


def get_duration(path: Path) -> float:
    """Método para obtener la duración de un archivo de audio en segundos.
    
    Args: Ruta al archivo de audio
    Returns: Duración del archivo de audio en segundos."""
    
    info = sf.info(str(path))
    return info.duration


def validate_audio_file(path: Path) -> bool:
    """ Método para validar si un archivo de audio es legible y está en un formato soportado.

    Args: Ruta al archivo de audio
    Returns: True si el archivo es válido, False si es inválido."""

    if not path.exists():
        return False
    if path.suffix.lower() not in SUPPORTED_FORMATS:
        return False
    
    path_str = str(path)
    

    try:
        sf.info(path_str)
        return True
    except (RuntimeError, OSError):
        pass

    try:
        AudioSegment.from_file(path_str)
        return True
    except (OSError, ValueError, Exception):
        return False