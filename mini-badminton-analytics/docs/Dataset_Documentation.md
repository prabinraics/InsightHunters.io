# Dataset Documentation

## Project

**Mini Badminton Analytics Dashboard**

---

# 1. Introduction

The quality of any analytics application depends heavily on the quality of the dataset it uses. For this project, a curated badminton match dataset was prepared to support data preprocessing, statistical analysis, and visualization.

The dataset contains historical badminton match information from multiple tournaments and includes details such as match dates, tournament stages, venues, participating players, scores, winners, and match duration. This information provides the foundation for generating meaningful insights through the analytics dashboard.

---

# 2. Dataset Overview

| Attribute     | Information                |
| ------------- | -------------------------- |
| Dataset Name  | badminton_matches_150.xlsx |
| Dataset Type  | Structured Sports Dataset  |
| File Format   | Microsoft Excel (.xlsx)    |
| Domain        | Sports Analytics           |
| Sport         | Badminton                  |
| Total Records | 150 Matches                |
| Total Columns | 15 Attributes              |

The dataset has been organized in a tabular format where each row represents a single badminton match and each column stores a specific attribute related to that match.

---

# 3. Dataset Source

The dataset was curated specifically for this academic project using publicly available badminton match information. The collected data was organized, standardized, and formatted into a structured Excel dataset to support data analysis and visualization.

---

# 4. Dataset Attributes

The following table describes each attribute used within the dataset.

| Column Name      | Description                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| match_id         | Unique identifier assigned to each badminton match                                                   |
| year             | Year in which the tournament was held                                                                |
| date             | Date of the match                                                                                    |
| stage            | Tournament stage (Group Stage, Quarter Final, Semi Final, Final, etc.)                               |
| stadium          | Stadium or arena where the match was played                                                          |
| city             | Host city of the tournament                                                                          |
| home_team        | First player or team participating in the match                                                      |
| away_team        | Second player or team participating in the match                                                     |
| home_score       | Score achieved by the first player/team                                                              |
| away_score       | Score achieved by the second player/team                                                             |
| tournament       | Tournament name                                                                                      |
| winner           | Winning player or team                                                                               |
| duration_minutes | Total match duration in minutes                                                                      |
| match_type       | Type of badminton match (Singles or Doubles)                                                         |
| category         | Competition category (Men's Singles, Women's Singles, Men's Doubles, Women's Doubles, Mixed Doubles) |

---

# 5. Data Types

The dataset consists of different types of data depending on the information stored.

| Data Type | Columns                                                                              |
| --------- | ------------------------------------------------------------------------------------ |
| Integer   | match_id, year, home_score, away_score, duration_minutes                             |
| Date      | date                                                                                 |
| String    | stage, stadium, city, home_team, away_team, tournament, winner, match_type, category |

Using appropriate data types improves processing efficiency and ensures accurate statistical calculations.

---

# 6. Dataset Features

The dataset includes information that supports various analytical operations within the application, including:

- Tournament analysis
- Player performance analysis
- Match duration analysis
- Venue analysis
- City-wise tournament distribution
- Score comparison
- Winner statistics
- Match category analysis

These features enable the dashboard to generate meaningful summaries and visual insights for users.

The dataset includes three engineered features that improve analytical capabilities:

- TotalScore
- ScoreDifference
- DurationHours

## These features support performance analysis, match competitiveness evaluation, and statistical visualization.

# 7. Data Quality Assessment

Before performing any analysis, the dataset was examined to evaluate its overall quality.

The following checks were carried out:

- Verification of missing values
- Duplicate record detection
- Validation of numerical values
- Date format verification
- Consistency of tournament names
- Consistency of player names

The assessment confirmed that the dataset was complete and suitable for preprocessing and further analysis.

---

# 8. Dataset Limitations

Although the dataset is sufficient for the objectives of this project, several limitations should be acknowledged:

- The dataset contains a limited number of matches.
- Only selected badminton tournaments are included.
- Player ranking information is not available.
- Live tournament updates are not supported.
- Match statistics such as aces, unforced errors, and rally counts are not included.

These limitations do not affect the primary objectives of the analytics dashboard but provide opportunities for future improvements.

---

# 9. Dataset Usage

The dataset is used throughout the application in multiple stages.

- Loading the raw dataset
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Statistical computations
- Visualization generation
- Dashboard presentation

Every analytical result displayed within the dashboard is generated from this dataset.

---

# 10. Expected Outputs

Using this dataset, the application generates:

- Summary statistics
- Tournament information
- Top winners
- Match duration analysis
- Score difference analysis
- Tournament distribution charts
- City-wise match statistics
- Stadium-wise match statistics

These outputs help users better understand badminton tournament data through an interactive dashboard.

---

# 11. Conclusion

The badminton match dataset serves as the foundation of the Mini Badminton Analytics Dashboard. Its structured format, complete records, and relevant match information make it suitable for data preprocessing, statistical analysis, and visualization.

By organizing match details such as tournaments, players, venues, scores, and durations into a consistent format, the dataset enables the application to transform raw badminton data into meaningful insights. Although the dataset has certain limitations, it successfully meets the requirements of this project and supports the overall objective of building an informative and user-friendly sports analytics dashboard.
