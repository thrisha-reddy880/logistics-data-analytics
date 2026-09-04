# 📦 Logistics Week 1 — Strategic Planning and Data Exploration

## 📌 Project Overview

This project focuses on **strategic planning and data exploration in logistics and supply chain management**.

The objective is to analyze logistics data, identify delivery and shipping patterns, calculate important KPIs, and explore analytical approaches such as **regression, classification, clustering, and optimization**.

This project was developed as part of **Week 1 of a technical/data science internship**.

---

## 🎯 Project Objectives

- Understand logistics and supply chain operations.
- Explore and preprocess logistics data.
- Identify delivery and shipping patterns.
- Calculate important logistics KPIs.
- Analyze shipping modes and delivery performance.
- Perform Exploratory Data Analysis (EDA).
- Understand regression and classification approaches.
- Apply clustering for segmentation.
- Explore route optimization using Operations Research.
- Develop an end-to-end roadmap for logistics analytics.

---

## 📊 Dataset

The project uses the **DataCo Smart Supply Chain Dataset**, a publicly available logistics and supply-chain dataset.

**Dataset Source:**  
[Kaggle — DataCo SMART Supply Chain for Big Data Analysis](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

### Dataset Statistics

| Metric | Value |
|---|---:|
| Records | 180,519 |
| Columns | 53 |
| Duplicate Rows | 0 |
| Unique Orders | 65,752 |

### Data Quality Observations

Some columns contain missing values, particularly:

- Product Description
- Order Zipcode
- Customer Lname
- Customer Zipcode

The raw dataset is **not included in this repository** to keep the repository lightweight.

---

# 📈 Key Performance Indicators (KPIs)

The following KPIs were calculated during Week 1 analysis:

| KPI | Result |
|---|---:|
| Late Delivery Rate | **57.28%** |
| Average Actual Shipping Days | **3.50 days** |
| Average Scheduled Shipping Days | **2.93 days** |
| Average Shipping Variance | **0.57 days** |
| Unique Orders | **65,752** |

---

## 🚚 Shipping Mode Analysis

| Shipping Mode | Orders | Avg. Shipping Days | Late Rate |
|---|---:|---:|---:|
| First Class | 10,079 | 2.00 | 100.00% |
| Same Day | 3,571 | 0.48 | 47.83% |
| Second Class | 12,778 | 3.99 | 79.73% |
| Standard Class | 39,324 | 4.00 | 39.77% |

These results show that **delivery performance varies significantly across shipping modes**, making shipping-mode analysis an important area for further investigation.

---

# 📊 Exploratory Data Analysis

The Week 1 analysis generated the following visualizations.

## 🚚 Shipping Days Distribution

![Shipping Days Distribution](outputs/shipping_days_distribution.png)

This visualization shows the distribution of actual shipping days across the dataset.

---

## ⚠️ Late Delivery Rate by Shipping Mode

![Late Delivery Rate by Shipping Mode](outputs/late_rate_by_shipping_mode.png)

This visualization compares late delivery rates across different shipping modes.

---

## 🌍 Orders by Market

![Orders by Market](outputs/orders_by_market.png)

This visualization shows the distribution of orders across different global markets.

---

# 🔬 Analytical Methodologies

## 1. Exploratory Data Analysis

EDA is used to understand:

- Dataset structure
- Missing values
- Duplicate records
- Shipping patterns
- Market distribution
- Delivery performance
- Shipping-mode performance

---

## 2. Regression

Regression can be used to predict continuous logistics variables such as:

- Shipping duration
- Delivery time
- Sales
- Delivery cost

A future version of the project can use regression models to estimate expected delivery duration based on historical logistics information.

---

## 3. Classification

Classification can be used to predict whether an order is likely to be delivered late.

### Example

```text
Order Information
       ↓
Machine Learning Model
       ↓
Late Delivery Prediction
       ↓
     Yes / No
```

The project includes a **Logistic Regression baseline** for this type of prediction.

---

## 4. Clustering

Clustering can be used to identify groups with similar characteristics, such as:

- Customers
- Cities
- Markets
- Shipping patterns
- Order behavior

The project includes **K-Means clustering** as an initial segmentation approach.

---

## 5. Optimization

Route optimization can help determine efficient delivery routes while considering:

- Distance
- Delivery time
- Vehicle capacity
- Customer locations
- Time windows

The project includes an initial **Vehicle Routing Problem (VRP)** planning module using **Google OR-Tools**.

---

# 🗺️ End-to-End Logistics Analytics Roadmap

```text
Data Collection
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
KPI Calculation
       ↓
Statistical Analysis
       ↓
Regression / Classification
       ↓
Customer & Market Clustering
       ↓
Route Optimization
       ↓
Model Evaluation
       ↓
Dashboard / Reporting
       ↓
Business Decision Making
```

---

# 📁 Project Structure

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

# 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **Google OR-Tools**
- **OpenPyXL**
- **Git**
- **GitHub**

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/thrisha-reddy880/logistics-week1-data-analysis.git
```

## 2. Navigate to the Project

```bash
cd logistics-week1-data-analysis
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Add the Dataset

Download the DataCo Smart Supply Chain dataset and place the CSV file inside:

```text
data/
```

The dataset file should be named:

```text
DataCoSupplyChainDataset.csv
```

## 5. Run the Analysis

```bash
python notebooks/01_week1_exploration.py
```

The generated analysis results will be available inside:

```text
outputs/
```

---

# 💡 Key Business Problem

The analysis focuses on identifying factors that affect **logistics delivery performance**.

The major observed issue is the relatively high **late delivery rate of 57.28%**.

The analysis can help organizations investigate:

- Which shipping modes have higher delivery risks?
- Which markets have greater order volumes?
- Where are shipping delays occurring?
- Which customer or market segments behave similarly?
- How can delivery routes be optimized?
- How can predictive analytics support logistics planning?

---

# 📈 Expected Business Impact

The proposed analytics approach can help logistics organizations:

- Reduce delivery delays.
- Improve route planning.
- Optimize transportation resources.
- Identify high-risk deliveries.
- Improve customer satisfaction.
- Monitor operational KPIs.
- Support data-driven decision making.
- Improve supply-chain efficiency.

---

# 🚀 Future Enhancements

Future versions of the project can include:

- Advanced delivery-delay prediction.
- Random Forest and XGBoost models.
- Advanced customer segmentation.
- Real-world route optimization.
- Vehicle capacity constraints.
- Delivery time-window constraints.
- Interactive Power BI dashboard.
- Real-time logistics monitoring.
- Automated KPI reporting.
- Deployment using Flask or Streamlit.
- Integration with live logistics APIs.

---

# 📚 References

1. **DataCo SMART Supply Chain Dataset**  
   [Kaggle Dataset](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

2. **DataCo Supply Chain Dataset — Mendeley Data**  
   [Mendeley Data](https://data.mendeley.com/datasets/8gx2fvg2k6/5)

3. **Google OR-Tools**  
   [Google OR-Tools Documentation](https://developers.google.com/optimization)

4. **Vehicle Routing Problem**  
   [OR-Tools VRP Documentation](https://developers.google.com/optimization/routing/vrp)

5. **Vehicle Routing Problem with Time Windows**  
   [OR-Tools VRPTW Documentation](https://developers.google.com/optimization/routing/vrptw)

6. **Scikit-learn Clustering**  
   [Scikit-learn Clustering Documentation](https://scikit-learn.org/stable/auto_examples/cluster/index.html)

7. **Supply Chain KPIs**  
   [Shopify Supply Chain KPI Guide](https://www.shopify.com/in/blog/supply-chain-kpi/)

---

# ✅ Week 1 Deliverables

- [x] Background research
- [x] Logistics dataset identification
- [x] Data exploration
- [x] Data quality analysis
- [x] KPI calculation
- [x] Shipping-mode analysis
- [x] Market-level analysis
- [x] Exploratory visualizations
- [x] Regression methodology research
- [x] Clustering methodology research
- [x] Optimization methodology research
- [x] End-to-end logistics analytics roadmap
- [x] Strategic planning report
- [x] GitHub project structure

---

# 📌 Project Status

**Week 1 — Completed ✅**

The project currently contains the strategic planning, dataset exploration, KPI analysis, visualization outputs, analytical methodology, and roadmap required for the first week.

---

# 👩‍💻 Author

**K. Thrisha Reddy**

B.Tech — Computer Science and Engineering (Data Science)  
Vijaya Institute of Technology for Women  
Vijayawada, Andhra Pradesh, India

### 🔗 GitHub

https://github.com/thrisha-reddy880/logistics-week1-data-analysis

---

⭐ **If you find this project useful, consider giving the repository a star!**
