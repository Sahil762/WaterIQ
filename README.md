# WaterIQ
This project aims to predict water quality based on various features using machine learning techniques. The primary model used is a Random Forest Classifier.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Usage](#usage)

## Introduction

The objective of this project is to develop a machine learning model to predict the quality of water. The model is trained using a dataset containing various water quality indicators.

## Project Structure
```sh
WaterIQ/
│
├── data/
│   └── Water Quality Prediction.csv
│
├── notebooks/
│   └── Water_Quality_Prediction.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── model_training.py
│   └── evaluation.py
│
├── README.md
├── requirements.txt
└── LICENSE
```


## Dataset

The dataset used in this project is `Water Quality Prediction.csv`, which includes features such as pH, Chloride, and other chemical properties of water samples. The target variable is the water quality classification.

## Preprocessing

1. **Handling Missing Values:** 
   - For numerical columns, missing values are filled with the mean.
   - For categorical columns, missing values are filled with the mode.
   
2. **Encoding Categorical Variables:**
   - Categorical variables are encoded using Label Encoding.
   
3. **Feature Scaling:**
   - Numerical features are scaled using Standard Scaler.

4. **Feature Selection:**
   - Features relevant to the target variable are selected for model training.

## Model Training

A Random Forest Classifier is used for training the model. The data is split into training and testing sets with an 80-20 split.

## Evaluation

The model is evaluated using the following metrics:
- Accuracy
- Confusion Matrix
- Classification Report

## Usage

To run the notebook and train the model, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/water-quality-prediction.git
   cd water-quality-prediction
2. Open this notebook
   ```sh
   jupyter notebook notebooks/Water_Quality_Prediction.ipynb
