"""Quick sanity check before running notebooks."""

from pathlib import Path

import importlib

REQUIRED_CSV = [
    "studentInfo.csv",
    "studentVle.csv",
    "vle.csv",
    "studentAssessment.csv",
    "assessments.csv",
    "studentRegistration.csv",
    "courses.csv",
]

REQUIRED_PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "sklearn",
    "xgboost",
]


def main() -> int:
    root = Path(__file__).resolve().parent
    data_dir = root / "datasets"
    errors = []

    if not data_dir.is_dir():
        errors.append("Missing datasets/ folder")
    else:
        for name in REQUIRED_CSV:
            if not (data_dir / name).is_file():
                errors.append(f"Missing datasets/{name}")

    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg)
        except ImportError:
            errors.append(f"Missing Python package: {pkg} (run pip install -r requirements.txt)")

    notebooks = [
        root / "task 1" / "task1_engagement_score.ipynb",
        root / "task 2" / "task2_feature_engineering.ipynb",
        root / "task 2" / "task2_model_comparison.ipynb",
        root / "task 3" / "task3_recommenders.ipynb",
    ]
    for nb in notebooks:
        if not nb.is_file():
            errors.append(f"Missing notebook: {nb.relative_to(root)}")

    if errors:
        print("Setup check FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Setup check passed.")
    print(f"  Data: {data_dir}")
    print(f"  Notebooks: {len(notebooks)} found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
