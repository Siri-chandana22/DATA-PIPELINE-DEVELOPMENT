# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: YARLAGADDA SIRI CHANDANA

*INTERN ID*: CT4MDR3097

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 MONTHS

*MENTOR*: NEELA SANTOSH

# ETL Pipeline for Data Preprocessing, Transformation, and Loading

This repository contains a Python-based ETL (Extract, Transform, Load) pipeline developed to automate the preprocessing, transformation, and loading of tabular data using popular data science libraries, namely pandas and scikit-learn. The pipeline is designed to handle missing values, standardize numerical features, and clean categorical features, ensuring the dataset is ready for downstream analytics, machine learning modeling, or reporting.

# Overview of the Pipeline

The ETL pipeline is implemented in six major steps, beginning with loading the dataset and ending with saving the cleaned and transformed data to a CSV file. The pipeline is highly modular, making it easy to adapt to different datasets with minimal changes.

## 1. Loading the Data:

The first step involves loading the dataset using pandas.read_csv(). The dataset used for this demonstration contains a mix of numerical and categorical features, including Name, Age, Gender, Salary, Department, and Experience. The dataset intentionally contains missing values (NaN) in both numeric and categorical columns to demonstrate how the pipeline handles incomplete data. Immediately after loading, the first ten rows are printed for preview, giving the user an overview of the raw, unprocessed data.

## 2. Identifying Feature Types:

To apply appropriate preprocessing steps, the code automatically identifies numerical and categorical columns. Numerical features (int64 and float64) include columns like Age, Salary, and Experience, whereas categorical features (object) include Name, Gender, and Department. This distinction allows for targeted preprocessing: scaling for numerical data and filling missing values for categorical data.

## 3. Creating Preprocessing Pipelines:

Two separate preprocessing pipelines are created using scikit-learn’s Pipeline and ColumnTransformer:
### Numerical Pipeline: 
Missing numerical values are imputed using the mean of the column via SimpleImputer(strategy='mean'). Once imputation is complete, StandardScaler is applied to standardize the numerical features, transforming them to have a mean of zero and a standard deviation of one. Standardization is critical for algorithms sensitive to the scale of input features, such as logistic regression, k-nearest neighbors, and neural networks.
### Categorical Pipeline: 
Missing categorical values are replaced with the string 'Unknown' using SimpleImputer(strategy='constant', fill_value='Unknown'). This ensures that the categorical columns do not contain NaN values, which can cause errors in downstream processing or analysis.

## 4. Combining Pipelines and Transforming the Data:

The numerical and categorical pipelines are combined using ColumnTransformer. This allows the simultaneous transformation of multiple columns with different preprocessing rules while preserving the dataset’s structure. The combined transformer is then applied to the dataset using fit_transform(), producing a fully processed NumPy array.

## 5. Creating a Processed DataFrame:

The transformed data is converted back into a pandas DataFrame. Numeric columns are rounded to four decimal places to improve readability, and the original column order is preserved. For console preview, the categorical columns are explicitly filled with 'Unknown' wherever missing values are present. This ensures the preview matches the final CSV output, while avoiding pandas’ future warnings related to type downcasting.

## 6. Saving the Processed Dataset:

Finally, the cleaned and transformed dataset is saved as processed_data_clean.csv using to_csv(). The CSV contains no missing values, numeric features are scaled, and categorical features are clean, making it ready for machine learning or reporting applications.

# Key Features and Advantages

## Automatic Handling of Missing Values:
Both numeric and categorical missing values are handled intelligently. Mean imputation for numeric columns and 'Unknown' imputation for categorical columns prevent errors and data loss.
## Scaling of Numeric Features: 
Standardization ensures numerical columns are on a comparable scale, which is essential for many machine learning algorithms.
## Preservation of Original Column Order: 
The pipeline retains the original order of columns, which is useful for reporting and model feature alignment.
## Console Preview Consistency: 
The console preview now matches the CSV output, including 'Unknown' in place of missing categorical values.
# Modular and Adaptable: 
The pipeline is modular, using scikit-learn pipelines and transformers, which makes it reusable across multiple datasets with minimal changes.

# Conclusion

This ETL pipeline demonstrates best practices in data preprocessing by integrating missing value handling, feature scaling, and categorical data cleaning into a single, automated workflow. It is a robust foundation for any data science project where clean and standardized input data is essential for analysis, visualization, or model building. This pipeline is particularly useful for internship and real-world applications where datasets are often incomplete, unstandardized, and messy, ensuring high-quality, reproducible data processing.
