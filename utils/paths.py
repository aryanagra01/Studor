"""Shared path helpers for StudorAI notebooks."""

from pathlib import Path


def get_data_dir() -> Path:
    """
    Return the datasets directory regardless of notebook working directory.

    Looks for a folder named ``datasets`` containing ``studentInfo.csv`` in the
    current directory or one level up (e.g. when running from ``task 1/``).
    """
    candidates = [
        Path("datasets"),
        Path("../datasets"),
    ]
    for path in candidates:
        if (path / "studentInfo.csv").is_file():
            return path.resolve()
    raise FileNotFoundError(
        "Could not find datasets/ with OULAD CSV files. "
        "Place the CSV files in <project>/datasets/ or run notebooks from "
        "the project root or a task folder."
    )
