# Data Audit Report – Nepal Housing Dataset

## 1. Dataset Overview

The Nepal Housing Dataset (nepalhousing.csv) was analyzed to assess its quality before performing data analysis and visualization. The dataset contains information about residential properties, including price, location, land area, number of bedrooms, bathrooms, parking, road details, and other property attributes.

### Dataset Information

- Dataset Name: Nepali Housing Price Dataset (nepalhousing.csv)
- Total Rows: 2211
- Total Columns: 18

After preprocessing, two additional columns (Area_Value and Area_sqft) were created, resulting in a cleaned dataset with 20 columns.

---

## 2. Initial Data Analysis

### Missing Values

The following columns contained missing values:

| Column    | Missing Values |
| --------- | -------------: |
| Floors    |           1172 |
| Year      |           1629 |
| Road Type |            785 |

### Handling Missing Values

- Numerical columns were filled using the median.
- Categorical columns were filled using the mode.
- After preprocessing, no missing values remained.

---

## 3. Duplicate Records

No duplicate records were found in the dataset.

- Duplicate Rows: 0

Therefore, no duplicate rows were removed during preprocessing.

---

## 4. Data Quality Issues

| Issue                        | Example                           | Impact                                      |
| ---------------------------- | --------------------------------- | ------------------------------------------- |
| Missing Values               | Floors, Year, Road Type           | May reduce completeness and affect analysis |
| Inconsistent Area Units      | Area stored in different units    | Makes comparison difficult                  |
| Unrealistic Prices           | Extremely high price values       | Can distort averages and visualizations     |
| Inconsistent Text Formatting | City names and categorical values | Creates incorrect grouping during analysis  |
| Outliers                     | 142 price outliers detected       | Strongly influences statistical measures    |

---

## 5. Data Cleaning Summary

The following preprocessing steps were completed:

- Loaded the dataset.
- Inspected dataset structure.
- Checked missing values.
- Checked duplicate records.
- Converted Price into numeric format.
- Extracted Area values.
- Converted area measurements into square feet.
- Created Area_Value and Area_sqft columns.
- Filled missing values.
- Standardized text formatting.
- Identified unrealistic prices and outliers.
- Saved the cleaned dataset.

---

## 6. Conclusion

The dataset required several preprocessing steps before analysis because it contained missing values, inconsistent area units, formatting inconsistencies, and price outliers. After cleaning, the dataset became suitable for exploratory analysis.

However, the dataset should not be used directly for dashboards or decision-making without proper validation. Implementing a reliable data pipeline with automated validation, data cleaning, and standardized formats would improve the quality and reliability of future analyses.
