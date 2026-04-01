import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# -----------------------------
# Step 1: Load Data
# -----------------------------
# Replace with your dataset file path
data = pd.read_csv("data.csv")

print("Original Data (Preview):")
print(data.head(10))  # show first 10 rows for clarity

# Save original column order
original_columns = data.columns

# -----------------------------
# Step 2: Identify Columns
# -----------------------------
numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
categorical_features = data.select_dtypes(include=['object']).columns

# -----------------------------
# Step 3: Create Pipelines
# -----------------------------
# Numeric: fill NaN with mean, then scale
numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical: fill NaN with 'Unknown'
categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown'))
])

# Combine pipelines
preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numeric_features),
    ('cat', categorical_pipeline, categorical_features)
])

# -----------------------------
# Step 4: Transform Data
# -----------------------------
processed_data = preprocessor.fit_transform(data)

# Convert to DataFrame
processed_df = pd.DataFrame(processed_data, columns=list(numeric_features) + list(categorical_features))

# Rearrange to match original column order
processed_df = processed_df[original_columns]

# Round numeric columns for readability
processed_df[numeric_features] = processed_df[numeric_features].round(4)

# -----------------------------
# Step 5: Console Preview (no warnings)
# -----------------------------
# Fill only categorical columns for display
display_df = processed_df.copy()
display_df[categorical_features] = display_df[categorical_features].fillna('Unknown')

print("\nProcessed Data (Preview):")
print(display_df.head(10))  # preview first 10 rows

# -----------------------------
# Step 6: Save Processed Data
# -----------------------------
processed_df.to_csv("processed_data_clean.csv", index=False)

print("\nETL Pipeline Completed Successfully!")
