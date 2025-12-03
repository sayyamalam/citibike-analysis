import os
from pathlib import Path

# Projektroot relativ zur Position dieser Datei
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Datenverzeichnisse
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DATA_RAW = os.path.join(DATA_DIR, "data_raw")
DATA_RAW_PROCESSED = os.path.join(DATA_DIR, "data_raw_processed")
DATA_SPATIAL = os.path.join(DATA_DIR, "data_spatial")
DATA_TEMPORAL = os.path.join(DATA_DIR, "data_temporal")
DATA_MODEL = os.path.join(DATA_DIR, "data_model")

# Abbildungsverzeichnis
FIGURES_DIR = os.path.join(PROJECT_ROOT, "figures")
