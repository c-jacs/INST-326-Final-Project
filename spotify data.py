import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Function 1: Load CSV data
def load_data(file_path):
    """
    Load data from the CSV file.

    Parameters:
    - file_path: str, the path to the CSV file.

    Returns:
    - DataFrame containing the song data.
    """
    return pd.read_csv(file_path)

# Function 2: Preprocess data
def preprocess_data(data):
    """
    Preprocess the song data.

    Parameters:
    - data: DataFrame, the song data.

    Returns:
    - Processed DataFrame.
    """
    # Example preprocessing steps:

    # Drop rows with missing values
    data = data.dropna()

    # Convert text data to lowercase
    data['lyrics'] = data['lyrics'].str.lower()

    # Remove punctuation and special characters
    data['lyrics'] = data['lyrics'].str.replace('[^\w\s]', '')

    # Tokenization (split the text into words)
    data['lyrics'] = data['lyrics'].apply(lambda x: x.split())

    # Join the list of tokens into a string
    data['lyrics'] = data['lyrics'].apply(lambda x: ' '.join(x))

    # You might want to apply other specific preprocessing steps based on your data

    return data
