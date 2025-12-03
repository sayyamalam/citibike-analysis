import os
from pathlib import Path

# Projektroot relativ zur Position dieser Datei
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Datenverzeichnisse
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DATA_RAW = os.path.join(DATA_DIR, "data_raw")
DATA_PROCESSED = os.path.join(DATA_DIR, "data_processed")
DATA_SPATIAL = os.path.join(DATA_DIR, "data_spatial")
DATA_TEMPORAL = os.path.join(DATA_DIR, "data_temporal")
DATA_HYPOTHESIS = os.path.join(DATA_DIR, "data_hypothesis")

# Abbildungsverzeichnis
FIGURES_DIR = os.path.join(PROJECT_ROOT, "figures")
