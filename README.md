# E-Commerce Customer Analytics & Intelligence Platform

An end-to-end analytics platform built on the modern data stack, combining data engineering, analytics engineering, machine learning, and business intelligence to drive customer insights for an e-commerce business.

## Project Overview

This project analyzes 100K+ orders from a Brazilian e-commerce marketplace to answer critical business questions:

- **Which customers are at risk of churning?** → Churn prediction model (XGBoost + SHAP)
- **What is the predicted lifetime value of each customer?** → CLV model (BG/NBD + Gamma-Gamma)
- **Which orders will miss their delivery deadline?** → Delivery delay prediction (LightGBM)
- **What are customers saying in reviews?** → NLP sentiment analysis (multilingual BERT)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Cloud Data Warehouse | Snowflake |
| Data Transformation | dbt Core |
| Programming Language | Python 3.12, SQL |
| Machine Learning | Scikit-learn, XGBoost, LightGBM, Transformers |
| BI & Visualization | Power BI |
| Version Control | Git / GitHub |
| Data Source | Olist Brazilian E-Commerce Dataset (Kaggle) |

## Architecture
Kaggle CSVs → Python Ingestion → Snowflake (RAW)
↓
dbt Staging (cleaned)
↓
dbt Intermediate (joined)
↓
dbt Marts (business models)
↓    ↓
Power BI   ML Models
↓
ML Scores → Snowflake
## Project Structure
ecommerce-analytics-platform/
├── ingestion/           # Python scripts to load data into Snowflake
├── dbt_project/         # dbt models (staging, intermediate, marts)
├── ml/
│   ├── notebooks/       # Jupyter notebooks for EDA and ML
│   ├── models/          # Saved model artifacts (.joblib)
│   └── utils/           # Shared feature engineering and evaluation code
├── power_bi/            # Power BI dashboard file
├── data/raw/            # Raw CSV files (not in Git)
├── docs/                # Documentation and sprint retros
├── tests/               # Integration and validation tests
├── requirements.txt     # Python dependencies
└── README.md
## Data Source

**Olist Brazilian E-Commerce Dataset**
- Source: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Size: ~100K orders across 8 relational tables
- Period: October 2016 – August 2018

## How to Reproduce

```bash
# Clone the repo
git clone https://github.com/varre1v/ecommerce-analytics-platform.git
cd ecommerce-analytics-platform

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate    # Windows (Git Bash)
# source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

## Roadmap

- [x] Sprint 1: Project setup and data ingestion
- [ ] Sprint 2: dbt staging and intermediate models
- [ ] Sprint 3: dbt mart models (RFM, cohorts, SLA)
- [ ] Sprint 4: Feature engineering and EDA
- [ ] Sprint 5: ML — Churn prediction and CLV
- [ ] Sprint 6: ML — Delivery prediction and NLP sentiment
- [ ] Sprint 7: Power BI dashboard
- [ ] Sprint 8: Testing, documentation, and polish

## License

MIT
