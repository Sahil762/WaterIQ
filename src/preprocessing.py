import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def handle_missing_values(data):
    for col in data.columns:
        if data[col].dtype in ['int64', 'float64']:
            data[col] = data[col].fillna(data[col].mean())
        else:
            data[col] = data[col].fillna(data[col].mode()[0])
    return data

def encode_categorical(data):
    le = LabelEncoder()
    data['Month'] = le.fit_transform(data['Month'])
    return data

def scale_features(features):
    scaler = StandardScaler()
    numerical_cols = features.select_dtypes(include=['int64', 'float64']).columns
    features[numerical_cols] = scaler.fit_transform(features[numerical_cols])
    return features
