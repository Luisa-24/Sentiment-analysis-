""" El propósito de este 
modulo es preparar archivso de audio para su
posterior procesamiento

Args: Rutas de archivos de audio
Returns: Archivos de audio convertidos y normalizados."""

# Estándar 
import argparse 

import logging 

import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


#Locales 
from src.audio_processing.convert import AudioConverter

from src.utils.files import list_audio_files, ensure_dir

from src.utils.audio import SUPPORTED_FORMATS


def setup_logging():
    """ Configura el logging para la aplicación.
    Args: None
    Returns: None"""
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Prepare audio files for processing"
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data/raw"),
        help="Directory containing raw audio files"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="Output directory for converted files"
    )

    args = parser.parse_args()
    setup_logging()
    logger = logging.getLogger(__name__)

    if not args.input_dir.is_dir():
        logger.error(f"Input directory not found: {args.input_dir}")
        sys.exit(1)

    ensure_dir(args.output_dir)

    audio_files = list_audio_files(args.input_dir, SUPPORTED_FORMATS)
    if not audio_files:
        logger.warning(f"No audio files found in {args.input_dir}")
        sys.exit(0)

    logger.info(f"Found {len(audio_files)} audio files")

    converter = AudioConverter()
    converted = []

    for audio_file in audio_files:
        try:
            output_path = converter.convert(audio_file, args.output_dir)
            converted.append(output_path)
            logger.info(f"Converted: {audio_file.name} -> {output_path.name}")
        except Exception as e:
            logger.error(f"Failed to convert {audio_file}: {e}")

    logger.info(f"Successfully converted {len(converted)}/{len(audio_files)} files")


if __name__ == "__main__":
    main()