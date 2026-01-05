# Estándar 
from pathlib import Path


"""Módulo de funciones para manejo de archivos y directorios.
Crea el directorio si no existe y devuelve la ruta.

Args: Ruta al directorio
Returns: Ruta al directorio creado. """

def ensure_dir(path: Path) -> Path:
    """ Método para asegurar que un directorio exista
    
    Args: Ruta al directorio
    Returns: Ruta al directorio creado."""
    
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_output_path(input_path: Path, output_dir: Path, extension: str) -> Path:
    """Método para obtener la ruta de salida para 
    un archivo procesado.
    
    Args: Ruta al archivo de entrada y directorio de salida, extensión del archivo
    Returns: Ruta al archivo de salida con la nuevaa extensión. """
    
    ensure_dir(output_dir)
    return output_dir / f"{input_path.stem}.{extension.lstrip('.')}"


def list_audio_files(directory: Path, extensions: tuple = (".wav", ".mp3", ".m4a", ".flac")) -> list[Path]:
    """Método para listar archivos de audio en un 
    directorio dado ciertas extensiones.
    
    Args: Ruta al directorio y extensiones del archivo
    Returns: Lista de rutas a los archivos de audio encontrados."""
    
    files = []
    for ext in extensions:
        files.extend(directory.glob(f"*{ext}"))
    return sorted(files, key=lambda x: x.name)