import os
from pathlib import Path


def get_file_size_mb(file_path:Path):
    file_path = Path(file_path)  # 🔥 normalize
    return file_path.stat().st_size / (1024 * 1024)