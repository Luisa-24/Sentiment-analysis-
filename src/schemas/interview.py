"""Este módulo contiene las 
clases de datos para representar entrevistas
y sus segmentos asociados.
Args: Clases de datos para entrevistas y segmentos de audio
Returns: Clases de datos definidas."""

#Estandar 
from dataclasses import dataclass, field

from pathlib import Path 

from typing import Optional 

@dataclass
class Sentiment:
    """Clase para representar el sentimiento de un segmento de audio.
    
    Args: 
        Etiqueta del sentimiento, puntaje del sentimiento, puntajes detallados opcionales.
    returns: None."""
    
    label: str
    score: float
    all_scores: Optional[dict[str, float]] = None
    
@dataclass
class Segment: 
    """Clase para representar un segmento de audio en una entrevista
     
    Args: 
        ID del segmento, hablante, tiempo de inicio, tiempo de fin, texto transcrito,
        rol, ID de respuesta emparejada, sentimiento.
    returns: None"""
    
    segment_id: str 
    speaker: str
    start : float
    end : float
    text : str
    role : Optional[str] = None
    paired_response_id: Optional[str] = None
    sentiment : Optional[Sentiment] = None

@dataclass
class DiarizationSegment: 
    """Clase para representar un segmento de diarización de audio.
    
    Args: hablante, tiempo de inicio, tiempo de fin.
    returns: None"""
    
    speaker: str
    start : float
    end : float

@dataclass
class TranscriptSegment:
    """Clase para representar un segmento de transcripción de audio.
    
    Args: tiempo de inicio, tiempo de fin, texto transcrito.
    Returns: None"""
    
    start : float
    end : float
    text : str
    words: Optional[list[dict]] = None

@dataclass
class interview:
    """Clase para representar una entrevista de audio.
    
    Args: 
        ID de la entrevista, ruta al archivo fuente, ruta al archivo procesado
    Returns: None"""
    
    interview_id: str
    source_path: Path
    processed_path: Optional[Path] = None
    metadata: dict = field(default_factory=dict)
    segments: list[Segment] = field(default_factory=list)