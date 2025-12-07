import os
import zipfile
import pandas as pd

# Ruta al ZIP (dentro del repo, pero ignorado por git)
ZIP_PATH = os.path.join("data", "csiro-biomass.zip")
EXTRACT_DIR = os.path.join("data", "csiro-biomass")

def unzip_biomass():
    """Descomprime el ZIP de CSIRO Biomass en data/csiro-biomass."""
    if not os.path.exists(ZIP_PATH):
        raise FileNotFoundError(f"No se encontró el archivo ZIP en: {ZIP_PATH}")

    os.makedirs(EXTRACT_DIR, exist_ok=True)

    print(f"Descomprimiendo {ZIP_PATH} en {EXTRACT_DIR}...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        zf.extractall(EXTRACT_DIR)
    print("✓ Descompresión completa.")

def load_data():
    """Carga train.csv y test.csv si existen."""
    train_path = os.path.join(EXTRACT_DIR, "train.csv")
    test_path  = os.path.join(EXTRACT_DIR, "test.csv")

    if not os.path.exists(train_path):
        raise FileNotFoundError(f"No se encontró train.csv en {train_path}. ¿Ya descomprimiste el ZIP?")

    train = pd.read_csv(train_path)
    print("Train shape:", train.shape)

    test = None
    if os.path.exists(test_path):
        test = pd.read_csv(test_path)
        print("Test shape:", test.shape)
    else:
        print("⚠ No se encontró test.csv, solo se cargó train.csv")

    return train, test

if __name__ == "__main__":
    # Ejecuta esto solo si corres: python import.py
    unzip_biomass()
    train, test = load_data()
    print(train.head())
