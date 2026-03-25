import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    train = pd.read_csv("../data/train.csv")
    test = pd.read_csv("../data/test.csv")

    df = pd.concat([train, test])

    # Drop missing values
    df = df.dropna()

    # Handle target column
    if 'attack_cat' in df.columns:
        df['label'] = df['attack_cat'].apply(lambda x: 0 if x == 'Normal' else 1)
        df = df.drop('attack_cat', axis=1)

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])

    return df