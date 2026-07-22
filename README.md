# Mini Badminton Analytics

## Project Overview

The Mini Badminton Analytics is a Flask-based web application developed to analyze badminton match data through exploratory data analysis (EDA), statistical analysis, and data visualization. The application processes badminton match records and presents meaningful insights through summary statistics, charts, and an interactive dashboard.

The project demonstrates the integration of data preprocessing, statistical analysis, and web development to provide an organized and user-friendly analytics platform.

---

## Features

The application provides the following features:

- Dashboard summary statistics
  - Total matches
  - Total winners
  - Total tournaments
  - Average match duration

- Exploratory Data Analysis (EDA)
  - Dataset summary
  - Missing value analysis
  - Duplicate record analysis

- Statistical analysis
  - Winner statistics
  - Tournament statistics
  - Match duration analysis
  - Score difference analysis

- Data visualizations
  - Top 10 Winners
  - Tournament Match Distribution
  - Match Duration Distribution
  - Score Difference Histogram
  - Top Match Hosting Cities
  - Top Match Hosting Stadiums

- Interactive dashboard
  - Tournament filtering
  - Recent matches table
  - Responsive user interface

---

## Technologies Used

| Category             | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python 3.12              |
| Backend Framework    | Flask                    |
| Data Processing      | Pandas, NumPy            |
| Data Visualization   | Matplotlib, Seaborn      |
| Excel Processing     | OpenPyXL                 |
| Frontend             | HTML5, Bootstrap 5, CSS3 |
| Version Control      | Git and GitHub           |

---

## Project Structure

```text
mini-badminton-analytics/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   ├── eda.py
│   │   ├── statistics.py
│   │   └── visualizations/
│   │       ├── generate.py
│   │       ├── geography.py
│   │       ├── tournament.py
│   │       └── helper.py
│   │
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   │       └── plots/
│   │
│   └── templates/
│       └── index.html
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── DATASET_DOCUMENTATION.md
│   ├── DATA_PREPROCESSING_REPORT.md
│   ├── SYSTEM_DESIGN_REPORT.md
│   └── FINAL_PROJECT_REPORT.md
│
├── config.py
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

## Installation

### Prerequisites

Before running the application, ensure that Python 3.10 or later is installed on your system.

### Clone the Repository

```bash
git clone https://github.com/prabinraics/InsightHunters.io.git
```

### Create a Virtual Environment

**Windows**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

1. Place the badminton dataset in the appropriate data folder.
2. Start the Flask application.

```bash
python run.py
```

3. Open a web browser and navigate to:

```text
http://127.0.0.1:5000/
```

---

## Dashboard Overview

The dashboard presents badminton match data through summary statistics, analytical insights, and visualizations. Users can explore tournament information, player performance, match duration, score distribution, and venue statistics using the available charts and tables.

---

## Team Roles

| Role                     | Responsibility                                                                 |
| ------------------------ | ------------------------------------------------------------------------------ |
| Data Engineer            | Data collection, preprocessing, and preparation                                |
| Data Analytics Validator | Exploratory data analysis and statistical validation                           |
| System Designer          | Flask application development, dashboard design, and visualization integration |
| Documentation Lead       | Project documentation, reports, README, and project coordination               |

---

## Documentation

Additional project documentation is available in the `docs` folder.

- DATASET_DOCUMENTATION.md
- DATA_PREPROCESSING_REPORT.md
- SYSTEM_DESIGN_REPORT.md
- FINAL_PROJECT_REPORT.md

---

## License

This project was developed for academic purposes as part of a university coursework project.
