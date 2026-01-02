from pathlib import Path


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_output_path(input_path: Path, output_dir: Path, extension: str) -> Path:
    ensure_dir(output_dir)
    return output_dir / f"{input_path.stem}.{extension.lstrip('.')}"


def list_audio_files(directory: Path, extensions: tuple = (".wav", ".mp3", ".m4a", ".flac")) -> list[Path]:
    files = []
    for ext in extensions:
        files.extend(directory.glob(f"*{ext}"))
    return sorted(files, key=lambda x: x.name)