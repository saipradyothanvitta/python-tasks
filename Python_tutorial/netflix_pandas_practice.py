
import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show top rows
print("Head:\n", df.head())

# Dataset info
print("\nInfo:")
df.info()

# Descriptive statistics
print("\nDescription:\n", df.describe(include='all'))

# Missing values
print("\nMissing Values:\n", df.isnull().sum())

# Count of Movies vs TV Shows
print("\nType Counts:\n", df['type'].value_counts())

# Top 10 countries with most titles
print("\nTop 10 Countries:\n", df['country'].value_counts().head(10))

# Top 10 directors with most titles
print("\nTop 10 Directors:\n", df['director'].value_counts().head(10))
