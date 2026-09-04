# Strategic Planning and Data Exploration in Logistics

## Week 1 Internship Project

A data science project focused on exploring logistics and supply-chain data to identify delivery delays, evaluate operational KPIs, understand shipping-mode performance, and establish a roadmap for predictive analytics and route optimization.

---

## 📌 Project Overview

Efficient logistics management is essential for reducing delivery delays, controlling transportation costs, and improving customer satisfaction.

This Week 1 project uses the **DataCo Smart Supply Chain Dataset** to perform exploratory data analysis and establish a strategic foundation for a logistics analytics solution.

### Project Focus

- Delivery Performance Analysis
- Logistics KPI Calculation
- Shipping Mode Comparison
- Market-Level Order Analysis
- Data Quality Assessment
- Predictive Modeling Planning
- Customer & Order Clustering
- Route Optimization Planning

---

## 🎯 Project Objectives

- Understand the structure and quality of logistics data.
- Identify major delivery-performance problems.
- Calculate meaningful logistics KPIs.
- Compare delivery performance across shipping modes.
- Explore order distribution across markets.
- Prepare the dataset for predictive analytics.
- Plan regression and classification models for delivery-risk prediction.
- Identify opportunities for customer and order segmentation.
- Design an optimization approach for transportation planning.
- Create a reproducible GitHub-ready workflow.

---

## 📊 Dataset

**Dataset:** DataCo Smart Supply Chain for Big Data Analysis

**Size:** ~180,519 records and 53 columns

### Dataset Setup

Place the dataset in:

```text
data/DataCoSupplyChainDataset.csv
```

### Dataset Sources

- Kaggle – DataCo Smart Supply Chain for Big Data Analysis
- Mendeley Data – DataCo Supply Chain Dataset

---

## 🔎 Week 1 Data Exploration

### Dataset Profile

| Metric | Result |
|----------|----------|
| Total Records | 180,519 |
| Total Columns | 53 |
| Duplicate Rows | 0 |
| Unique Orders | 65,752 |
| Missing Product Description Values | 180,519 |
| Missing Order Zipcode Values | 155,679 |

---

## 📈 Key Logistics KPIs

| KPI | Result |
|------|---------|
| Late Delivery Rate | 57.28% |
| Average Actual Shipping Days | 3.50 Days |
| Average Scheduled Shipping Days | 2.93 Days |
| Average Shipping Variance | 0.57 Days |
| Unique Orders | 65,752 |

### Initial Interpretation

- More than 57% of shipments are delivered late.
- Actual shipping duration exceeds scheduled shipping duration.
- Average variance is 0.57 days.

---

## 🚚 Shipping Mode Analysis

| Shipping Mode | Unique Orders | Avg Shipping Days | Late Rate |
|--------------|--------------|------------------|-----------|
| First Class | 10,079 | 2.00 | 100.00% |
| Same Day | 3,571 | 0.48 | 47.83% |
| Second Class | 12,778 | 3.99 | 79.73% |
| Standard Class | 39,324 | 4.00 | 39.77% |

### Observations

- Standard Class handles the highest order volume.
- First Class has the highest observed late-delivery rate.
- Same Day provides the fastest shipping duration.
- Further analysis should include customer, market, and product factors.

---

## 🌎 Market-Level Exploration

Markets analyzed:

- LATAM
- Europe
- Pacific Asia
- USA
- Africa

The market analysis identifies geographic concentrations of demand and supports region-specific logistics planning.

---

## 📊 Visualizations

### 1. Distribution of Actual Shipping Days

```text
outputs/shipping_days_distribution.png
```

### 2. Late Delivery Rate by Shipping Mode

```text
outputs/late_rate_by_shipping_mode.png
```

### 3. Orders by Market

```text
outputs/orders_by_market.png
```

---

## 🧠 Data Science Methodologies

### 1. Exploratory Data Analysis (EDA)

EDA helps understand:

- Data structure
- Missing values
- Duplicate records
- Variable distributions
- Shipping performance
- Market patterns

### 2. Regression

Potential targets:

- Actual shipping duration
- Delivery delay
- Transportation cost
- Expected delivery time

### 3. Classification

Predict whether an order is likely to be delivered late.

Baseline model:

- Logistic Regression

Future models:

- Random Forest
- XGBoost
- Gradient Boosting

### 4. Clustering

Potential clustering features:

- Order frequency
- Average order value
- Quantity
- Late-delivery rate

### 5. Optimization

Vehicle Routing Problem (VRP) planning using:

- Distance
- Delivery time
- Vehicle capacity
- Customer demand
- Time windows

Framework:

- Google OR-Tools

---

## 🗺️ End-to-End Project Roadmap

```text
Business Problem
       ↓
Data Collection
       ↓
Data Profiling
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
KPI Analysis
       ↓
Feature Engineering
       ↓
Predictive Modeling
       ↓
Customer / Order Clustering
       ↓
Route Optimization
       ↓
Model Validation
       ↓
Dashboard & Decision Support
```

---

## 📁 Project Structure

```text
logistics_week1_github_project/
│
├── README.md
├── PROJECT_STATUS.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── docs/
│   └── week1_strategic_planning_report.md
│
├── notebooks/
│   └── 01_week1_exploration.py
│
├── outputs/
│   ├── README.md
│   ├── kpi_summary.csv
│   ├── shipping_mode_analysis.csv
│   ├── shipping_days_distribution.png
│   ├── late_rate_by_shipping_mode.png
│   └── orders_by_market.png
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── data_loader.py
    ├── preprocessing.py
    ├── kpis.py
    ├── eda.py
    ├── modeling.py
    ├── clustering.py
    └── optimization.py
```

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Google OR-Tools
- VS Code
- Git
- GitHub

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd logistics_week1_github_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Dataset

```text
data/DataCoSupplyChainDataset.csv
```

### Run Analysis

```bash
python notebooks/01_week1_exploration.py
```

---

## 📌 Key Business Problem

The analysis identifies delivery delays as a major logistics concern.

Key questions:

- What factors contribute most to late deliveries?
- Which markets experience higher delivery risk?
- Which shipping modes require improvement?
- Can delays be predicted before shipment?
- Can clustering improve logistics planning?
- Can route optimization reduce inefficiencies?

---

## 💡 Expected Business Impact

A complete logistics analytics solution can help organizations:

- Reduce late deliveries
- Improve delivery prediction
- Optimize shipping-mode selection
- Improve route planning
- Increase resource utilization
- Identify high-risk orders
- Support data-driven decision making

---

## 🔮 Future Enhancements

- Random Forest & XGBoost models
- Delivery-time regression
- Customer segmentation
- Geographic route optimization
- Vehicle capacity constraints
- Power BI dashboard
- Streamlit application
- Real-time monitoring
- SHAP explainability
- Logistics decision-support platform

---

## 📝 Week 1 Deliverables

✅ Background Research

✅ Logistics Problem Definition

✅ Project Objectives

✅ KPI Identification

✅ Data Profiling

✅ Data Exploration

✅ KPI Calculation

✅ Shipping Mode Analysis

✅ Market Analysis

✅ Visualization Generation

✅ Regression Planning

✅ Classification Planning

✅ Clustering Planning

✅ Route Optimization Planning

✅ Strategic Roadmap

✅ Documentation

---

## 👩‍💻 Author

**K. Thrisha Reddy**

B.Tech – Computer Science and Engineering (Data Science)

Vijaya Institute of Technology for Women, Vijayawada

---

## ⭐ Project Status

### Week 1 – Strategic Planning and Data Exploration

**Status: COMPLETED ✅**

The project establishes the data foundation, identifies logistics KPIs, performs exploratory analysis, and defines the roadmap for predictive analytics, clustering, and optimization.
