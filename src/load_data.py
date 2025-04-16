import pandas as pd
from src import config

def load_raw_data():
    return pd.read_csv(config.RAW_DATA_PATH)