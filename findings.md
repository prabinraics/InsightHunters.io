# Findings

## Average House Price

Average House Price: NPR 406,442,810,870.62

Median House Price: NPR 8,000,000.00

The average house price is much higher than the median because a small number of extremely expensive properties significantly increase the average value. Therefore, the median provides a better representation of a typical property price.

---

## Price Distribution

The distribution of house prices is right-skewed. Most properties fall within the lower and middle price ranges, while a relatively small number of listings have extremely high prices.

A total of 142 price outliers were identified.

---

## Top 3 Municipalities by Listings

| Rank | Municipality | Listings |
| ---- | ------------ | -------- |
| 1    | Kathmandu    | 1483     |
| 2    | Lalitpur     | 432      |
| 3    | Bhaktapur    | 85       |

Kathmandu has the highest number of property listings, indicating that most properties in the dataset are located there.

---

## Reflection

Some analysis results should be interpreted carefully.

The average house price may not accurately represent the market because it is strongly influenced by extremely expensive properties. Price outliers also affect the scatter plot and correlation analysis.

Although missing values were handled using the median and mode, these methods may slightly reduce the natural variation in the data.

---

## Recommendations

Before using this dataset for business analysis or predictive modelling, the following improvements are recommended:

- Standardize all area measurement units.
- Validate unrealistic property prices.
- Standardize categorical values such as city names and road types.
- Verify missing values using the original data source whenever possible.
- Review extreme outliers before building predictive models.

---

# Visualization Summary

### Chart 1 – House Price Distribution

A histogram was selected because it clearly shows the distribution of house prices and helps identify skewness and outliers.

### Chart 2 – Top 10 Cities by Property Listings

A bar chart was chosen because it provides an easy comparison of the number of property listings across different cities.

### Chart 3 – House Price vs Area

A scatter plot was selected to observe the relationship between property area and house price while also highlighting unusual values.

---

---

# System Thinking

## Possible Data Sources

The housing dataset may have been collected from:

- Real estate agents
- Property listing websites through web scraping
- Manual data entry
- Government property records

## Possible Errors Before Receiving the Data

The dataset may contain human entry mistakes, duplicate property listings, inconsistent units (such as Aana and square feet), missing information, outdated listings, and incorrect property prices. These issues can reduce the reliability of the analysis.

## Risks of Using Raw Data

If the dataset is used directly in dashboards without cleaning, it may produce misleading visualizations, incorrect average prices, and inaccurate business insights. This could result in poor investment or business decisions.

## Scalability Challenges

As the dataset grows, maintaining consistent formatting and high data quality becomes more difficult. Automated validation, standardization, and ETL (Extract, Transform, Load) processes should be implemented to improve scalability and maintain reliable analysis.

---

# Sprint Review

## What did we discover?

We discovered that the dataset contains missing values, inconsistent area units, formatting inconsistencies, and several price outliers. These issues required cleaning before reliable analysis could be performed.

## What surprised us?

Although no duplicate records were found, the dataset contained many extreme price values that greatly affected the average house price. This demonstrated the importance of checking for outliers before interpreting statistical results.

## What would we fix before using this data?

- Verify extreme prices.
- Improve data validation during collection.
- Standardize all categorical values.
- Use consistent measurement units.
- Validate missing information using original sources whenever possible.
