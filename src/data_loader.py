import pandas as pd

# Global variable to store the dataset
df = None

def load_data():
    global df
    if df is None:
        df = pd.read_csv('data/flights_dataset.csv')
        df = df.drop(df.columns[0], axis=1)
        df['price'] = df['price'].div(83).round(2)
    return df

# Load the data once when the module is imported
load_data()