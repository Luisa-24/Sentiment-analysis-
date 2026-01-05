""" Este módulo contiene la 
clase AudioLoader que carga y valida archivos de audio.

Args: Ruta de archivo o directorio de audio
Returns: Objeto interview o lista de objetos interview cargados."""

# Estándar
from datetime import datetime 

from importlib.resources import path
from pathlib import Path

#Locales
from src.schemas.interview import interview 

from src.utils.audio import get_duration, validate_audio_file, SUPPORTED_FORMATS

from src.utils.files import list_audio_files


class AudioLoader:
    """ Clase para cargar y validar archivos de audio.
    
    Args: None 
    Returns: None"""
    
    def load(self, path: Path)-> interview:
        """ Método para cargar y validar un archivo de audio. 
        
        Aegs: Ruta al archivo de audio
        Returns: Objeto interview cargado."""
        
        path = Path(path)
        if not validate_audio_file(path):
            raise ValueError(f"Archivo de audio inválido o no soportado: {path}")
    
        interview_id = path.stem 
        metadata = self._extract_metadata(path)
    
        return interview(
            interview_id=interview_id,
            source_path=path,
            metadata=metadata
      )
    
    def load_batch(self, directory: Path)-> list[interview]:
        """Método para cargar y validar múltiples archivos de audio en un directorio.
        
        Args: Ruta al directorio
        Returns: Lista de objetos interview cargados."""
        
        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"El directorio no existe: {directory}")
    
        audio_files = list_audio_files(directory, SUPPORTED_FORMATS)
        return [self.load(f) for f in audio_files]
    
    def _extract_metadata(self, path: Path) -> dict:
        """ Método para extraer metadatos de un archivo de audio. 
        
        Args: Ruta al archivo de audio 
        Returns: Diccionario con metadatos extraídos."""
        
        duration = get_duration(path)
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        
        return {
            "date": mtime.isoformat(),
            "duration_s": round(duration, 2),
            "participants": ["interviewer", "interviewee"],
            "source_file" : str(path.name)
        }


