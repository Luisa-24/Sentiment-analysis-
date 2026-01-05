""" El propósito de este módulo es 
realizar la diarización de locutores en archivos de audio,
utilizando el modelo que ya está preentrenado de pyannote

Args: Rutas de archivo de audio
Returns: Lista de segmentos de diarización con hablante, 
         tiempo de inicio y tiempo de fin."""

# Estándar 
import os 

from pathlib import Path 

from pyannote.audio import Pipeline

import torch

# Locales 
from src.schemas.interview import DiarizationSegment


class Speker_Diarizer:
    """ Clase para realizar la diarización de locutores en archivos de audio.
    
        Args:
            hf_token: Token de Hugging Face para autenticación.
            model: Módelo Pyannote
            min_speakers: Número mínimo de locutores esperados.
            max_speakers: Número máximo de locutores esperados.
            num_speakers: Número exacto de locutores ( es opcional).
            device: Dispositivo para ejecutar el modelo (CPU o GPU).
        Returns: None."""

    def __init__(
        self,
        hf_token: str = None,
        model: str = "pyannote/speaker-diarization-3.1",
        min_speakers: int = 2,
        max_speakers: int = 3,
        num_speakers: int = None,
        device: str = None
    ):
        self.hf_token = hf_token or os.getenv("HF_TOKEN")
        if not self.hf_token:
            raise ValueError("Se requiere un token de Hugging Face para usar el modelo de diarización.")

        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.min_speakers = min_speakers
        self.max_speakers = max_speakers
        self.num_speakers = num_speakers

        self.pipeline = Pipeline.from_pretrained(model, use_auth_token=self.hf_token)
        self.pipeline.to(torch.device(self.device))

    def diarize(self, audio_path: Path) -> list[DiarizationSegment]:
        """ Método para realizar la diarización de locutores en un archivo de audio.

        Args: Ruta al archivo de audio.
        Returns: Lista de segmentos de diarización con hablante, tiempo de inicio y tiempo de fin."""

        audio_path = Path(audio_path)

        diarization_params ={}
        if self.num_speakers:
            diarization_params["num_speakers"] = self.num_speakers
        else:
            diarization_params["min_speakers"] = self.min_speakers
            diarization_params["max_speakers"] = self.max_speakers

        diarization = self.pipeline (str(audio_path), **diarization_params)

        segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append(DiarizationSegment(
                speaker=speaker,
                start = turn.start,
                end= turn.end
            ))
        
        return segments

    def assign_roles(self, segments: list[DiarizationSegment]) ->  dict[str, str]:
        """Método para asignar roles a los locutores basados en la duración total de habla 
        
        Args: Lista de segmentos de diarización 
        Returns: Diccionario mapeaando hablantes a roles ( entrevistador, entrevistado)"""

        speaker_durations ={}
        for seg in segments:
            duration = seg.end - seg.start
            speaker_durations[seg.speaker] = speaker_durations.get(seg.speaker, 0) + duration
            
        sorted_speakers = sorted(speaker_durations.items(), key=lambda x: x[1], reverse=True)
        
        roles = {}
        if len(sorted_speakers) >= 2:
            roles[sorted_speakers[0][0]] = "interviewee"
            roles[sorted_speakers[1][0]] = "interviewer"
            for speaker, _ in sorted_speakers[2:]:
                roles[speaker] = "other"
        elif len(sorted_speakers) == 1:
            roles[sorted_speakers[0][0]]= "interviewee"

        return roles
