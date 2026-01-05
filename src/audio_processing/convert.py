# Estándar
from pathlib import Path

from pydub import AudioSegment

#Locales
from src.utils.files import  get_output_path

class AudioConverter:
    """Clase para convertir archivos de audio a un formato  wav
    Args: 
        Ruta al archivo de audio de entrada.
    Returns:
           Directorio donde se guardará el archivo convertido."""
    TARGET_SAMPLE_RATE = 16000
    TARGET_CHANNELS = 1
    TARGET_FORMAT = "wav"


    def convert(self, input_path: Path, output_dir: Path) -> Path:
        """Método para convertir  archivos de audio.

        Args:
            Ruta al archivo de audio de entrada.
        Returns:
               Directorio donde se guardará el archivo convertido."""

        input_path = Path(input_path)
        output_path = get_output_path(input_path, output_dir, self.TARGET_FORMAT)

        audio = AudioSegment.from_file(str(input_path))
        audio = self._normalize(audio)

        audio.export(
            str(output_path),
            format=self.TARGET_FORMAT,
            parameters=["-ar", str(self.TARGET_SAMPLE_RATE), "-ac", str(self.TARGET_CHANNELS)]
        )

        return output_path


    def _normalize(self, audio: AudioSegment) -> AudioSegment:
        """Método para normalizar la frecuencia de muestreo y los canales de audio.
        
        Args: Objeto AudioSegment. 
        Returns: AudioSegment normalizado."""

        audio = audio.set_channels(self.TARGET_CHANNELS)
        audio = audio.set_frame_rate(self.TARGET_SAMPLE_RATE)
        return audio