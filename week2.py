# Import Libraries
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_excel("badminton_matches_150.xlsx")

print("Dataset Loaded Successfully!")

# Dataset Overview
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print(f"\nTotal Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

# Check Missing Values
print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Remove Duplicate Records
duplicates = df.duplicated().sum()
print(f"\nDuplicate Records: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

# Clean Text Columns
text_columns = [
    "stage",
    "stadium",
    "city",
    "home_team",
    "away_team",
    "tournament",
    "winner",
    "match_type",
    "category"
]

for col in text_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

print("\nText columns cleaned.")

# Convert Date Column
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Handle Missing Values

numeric_columns = df.select_dtypes(include=["number"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

object_columns = df.select_dtypes(include=["object"]).columns

for col in object_columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# Check Invalid Scores
print("\nRows with Negative Scores")

if "home_score" in df.columns and "away_score" in df.columns:
    invalid_scores = df[
        (df["home_score"] < 0) |
        (df["away_score"] < 0)
    ]

    print(invalid_scores)

# Feature Engineering

if "home_score" in df.columns and "away_score" in df.columns:

    df["TotalScore"] = (
        df["home_score"] +
        df["away_score"]
    )

    df["ScoreDifference"] = (
        abs(df["home_score"] - df["away_score"])
    )

if "duration_minutes" in df.columns:

    df["DurationHours"] = (
        df["duration_minutes"] / 60
    )

# Summary Statistics
print("\nSummary Statistics")
print(df.describe(include="all"))

# Basic Analysis

print("\nTop 5 Cities")
if "city" in df.columns:
    print(df["city"].value_counts().head())

print("\nTop 5 Winners")
if "winner" in df.columns:
    print(df["winner"].value_counts().head())

print("\nAverage Match Duration")
if "duration_minutes" in df.columns:
    print(df["duration_minutes"].mean())

print("\nTournament Distribution")
if "tournament" in df.columns:
    print(df["tournament"].value_counts())

# Validate Dataset

print("\nValidation")

print("Remaining Missing Values")
print(df.isnull().sum().sum())

print("Remaining Duplicate Rows")
print(df.duplicated().sum())

# Save Clean Dataset
df.to_excel(
    "badminton_matches_cleaned.xlsx",
    index=False
)

print("\nCleaned dataset saved successfully.")

# Final Summary

print("\nDATA ENGINEERING SUMMARY")

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Duplicate Rows Removed: {duplicates}")

if "duration_minutes" in df.columns:
    print(f"Average Match Duration: {df['duration_minutes'].mean():.2f} minutes")

if "city" in df.columns:
    print(f"Top City: {df['city'].value_counts().idxmax()}")

if "winner" in df.columns:
    print(f"Most Successful Winner: {df['winner'].value_counts().idxmax()}")

print("Clean Dataset: badminton_matches_cleaned.xlsx")