# CitiBike & NYPD Crash Analysis

Dieses Projekt analysiert CitiBike-Fahrten in New York City in Kombination mit den öffentlich verfügbaren NYPD-Unfalldaten.  
Ziel ist die Untersuchung räumlicher und zeitlicher Risikomuster sowie der Aufbau eines Modells zur Schätzung von Unfallraten pro Fahrt.

---

## Projektstruktur

```text
citibike-analysis
│
├── data/
│   ├── data_model/          # Modellfertige aggregierte Datensätze
│   ├── data_raw/            # Rohdaten (nicht im Repository enthalten)
│   ├── data_raw_processed/  # vorbereitete, große Datensätze
│   ├── data_spatial/        # räumliche Aggregationen
│   └── data_temporal/       # zeitliche Aggregationen
│
├── figures/
│
├── notebooks/
│   ├── eda/
│   │   ├── 02A_citibike_data_preparation.ipynb
│   │   ├── 02A_nypd_data_preparation.ipynb
│   │   ├── 02B_spatial_exploration.ipynb
│   │   └── 02B_temporal_exploration.ipynb
│   │
│   └── modeling/
│       ├── 03_hypothesis_validation.ipynb
│       └── 04_risk_modeling_glm.ipynb
│
├── utils/
│   ├── load_data.py
│   ├── model_summary.py
│   └── paths.py
│
└── README.md

```

---

## Daten und Reproduzierbarkeit

Die CitiBike-Rohdaten (mehrere GB) sowie die vollständigen NYPD-Kollisionsdaten werden nicht im Repository versioniert.
Um das Projekt vollständig zu reproduzieren, ist der Zugriff auf diese Daten notwendig.
Bei Bedarf bitte direkt den Entwickler kontaktieren.

---

## Setup & Installation

Das Projekt verwendet eine Conda-Umgebung, um alle benötigten Abhängigkeiten reproduzierbar und isoliert zu verwalten.

Voraussetzung:
Eine funktionierende Conda-Installation (Anaconda oder Miniconda).
Download & Installation: https://docs.conda.io/en/latest/miniconda.html

**1. Conda-Umgebung erstellen**

```bash
conda create -n citibike python=3.11
```

**2. Umgebung aktivieren**

```bash
conda activate citibike
```

**3. Kernabhängigkeiten installieren**

```bash
pip install \
    pandas \
    numpy==1.26.4 \
    matplotlib \
    seaborn \
    ipykernel \
    pyarrow \
    contextily \
    pyproj \
    scipy \
    statsmodels
```

**4. Jupyter-Kernel registrieren**

Dieser Schritt muss nur **einmal** ausgeführt werden.
```bash
python -m ipykernel install --user --name citibike --display-name "Citibike Env"
```

---

## Verwendete Datenquellen

CitiBike Trip Data: https://s3.amazonaws.com/tripdata/index.html

NYPD Motor Vehicle Collisions: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

---
