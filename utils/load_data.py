import os
import glob
import pandas as pd
import sys
sys.path.append("../..")
from utils.paths import DATA_RAW, DATA_RAW_PROCESSED

def load_citibike_raw(root=None, outpath=None):
    """
    Lädt alle CitiBike-CSV-Dateien rekursiv, vereinheitlicht kritische Spaltentypen,
    konkateniert den Datensatz und speichert ihn als Parquet.
    Falls die Ausgabedatei bereits existiert, wird sie direkt geladen.
    """

    # Standardpfade verwenden, falls nicht explizit angegeben
    root = root or os.path.join(DATA_RAW, "2023-citibike-tripdata")
    outpath = outpath or os.path.join(DATA_RAW_PROCESSED, "citibike_raw_concat.parquet")

    # Falls die fertige Datei bereits existiert wird sie direkt geladen
    if os.path.exists(outpath):
        print(f"CitiBike-Daten aus bestehender Datei geladen: {os.path.basename(outpath)}")
        return pd.read_parquet(outpath)

    print("Erstelle CitiBike-Datensatz...")

    # Alle CSV-Dateien im Ordner (inkl. Unterordner) finden
    files = glob.glob(os.path.join(root, "**/*.csv"), recursive=True)
    print(f"Anzahl gefundener CSV-Dateien: {len(files)}")

    # Problemspalten: sollen immer als String vorliegen
    dtype_fix = {
        "start_station_id": "string",
        "end_station_id": "string",
        "start_station_name": "string",
        "end_station_name": "string",
    }

    dfs = []

    # Jede CSV-Datei einzeln einlesen
    for f in sorted(files):
        print(f"Lade Datei: {os.path.basename(f)}")
        
        # Einlesen mit festen Typvorgaben
        df_tmp = pd.read_csv(f, low_memory=False, dtype=dtype_fix)

        # Fehlende Spalten nachträglich anlegen und Typ erzwingen
        for col, dt in dtype_fix.items():
            if col not in df_tmp.columns:
                df_tmp[col] = pd.NA
            df_tmp[col] = df_tmp[col].astype(dt)

        dfs.append(df_tmp)

    # Alles zusammenführen
    df_all = pd.concat(dfs, ignore_index=True)
    print(f"Gesamtzahl geladener Zeilen: {len(df_all)}")

    # Zielordner anlegen (falls nicht vorhanden)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    # Speichern als Parquet
    df_all.to_parquet(outpath, index=False)
    print(f"CitiBike-Daten gespeichert: {os.path.basename(outpath)}")

    return df_all


def load_nypd_raw(src=None, outpath=None):
    """
    Lädt den NYPD-Datensatz und speichert ihn unverändert als Parquet.
    Falls die Datei existiert, wird sie direkt geladen.
    """

    src = src or os.path.join(DATA_RAW, "nypd_data", "Motor_Vehicle_Collisions_-_Crashes_20251122.csv")
    outpath = outpath or os.path.join(DATA_RAW_PROCESSED, "nypd_raw.parquet")

    if os.path.exists(outpath):
        print(f"NYPD-Daten aus bestehender Datei geladen: {os.path.basename(outpath)}")
        return pd.read_parquet(outpath)

    print("Erstelle NYPD-Datensatz...")

    df = pd.read_csv(src, low_memory=False)
    print(f"Anzahl geladener Zeilen: {len(df)}")

    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    df.to_parquet(outpath, index=False)

    print(f"NYPD-Daten gespeichert: {os.path.basename(outpath)}")

    return df
