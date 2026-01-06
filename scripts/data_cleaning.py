import pandas as pd
import numpy as np

# Load raw dataset
df = pd.read_excel("raw_data.xlsx")

# Remove metadata rows and fix headers
df = df.iloc[3:].reset_index(drop=True)
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# Convert data types
df['date'] = pd.to_datetime(df['date'])
df['price_per_kg'] = pd.to_numeric(df['price_per_kg'])
df['weight_kg'] = pd.to_numeric(df['weight_kg'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Feature engineering
df['total_sales'] = df['price_per_kg'] * df['weight_kg']
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Standardize text
df['product_name'] = df['product_name'].str.strip().str.title()

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
