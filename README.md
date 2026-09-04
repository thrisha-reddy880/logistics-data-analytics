Strategic Planning and Data Exploration in Logistics

Week 1 Internship Project

A data science project focused on exploring logistics and supply-chain
data to identify delivery delays, evaluate operational KPIs, understand
shipping-mode performance, and establish a roadmap for predictive
analytics and route optimization.

📌 Project Overview

Efficient logistics management is essential for reducing delivery
delays, controlling transportation costs, and improving customer
satisfaction.

This Week 1 project uses the DataCo Smart Supply Chain dataset to
perform exploratory data analysis and establish a strategic foundation
for a logistics analytics solution.

The project focuses on:

Delivery performance analysis

Logistics KPI calculation

Shipping-mode comparison

Market-level order analysis

Data quality assessment

Predictive modeling planning

Customer/order clustering

Route optimization planning

🎯 Project Objectives

Understand the structure and quality of logistics data.

Identify major delivery-performance problems.

Calculate meaningful logistics KPIs.

Compare delivery performance across shipping modes.

Explore order distribution across markets.

Prepare the dataset for predictive analytics.

Plan regression and classification models for delivery-risk
prediction.

Identify opportunities for customer/order segmentation using
clustering.

Design an optimization approach for transportation and route
planning.

Create a reproducible GitHub-ready data science workflow.

📊 Dataset

Dataset: DataCo Smart Supply Chain for Big Data Analysis

The dataset contains approximately 180,519 records and 53 columns
covering orders, customers, products, shipping, delivery performance,
sales, and market information.

The raw dataset is intentionally not included in this GitHub
repository because it is a large public dataset. Download it from the
original public source and place it locally in:

data/DataCoSupplyChainDataset.csv

The repository's .gitignore prevents accidental uploading of the raw
dataset.

Dataset Sources

Kaggle: DataCo Smart Supply Chain for Big Data Analysis

Mendeley Data: DataCo Supply Chain Dataset

🔎 Week 1 Data Exploration

Dataset Profile

Metric                                                 Result

Total records                                     180,519
Total columns                                          53
Duplicate rows                                          0
Unique orders                                      65,752
Completely missing Product Description values     180,519
Missing Order Zipcode values                      155,679

The missing-value analysis is retained as part of the data-quality
assessment. Fields with extensive missingness should be evaluated before
being used in future modeling.

📈 Key Logistics KPIs

KPI                                        Result

Late Delivery Rate                     57.28%
Average Actual Shipping Days        3.50 days
Average Scheduled Shipping Days     2.93 days
Average Shipping Variance           0.57 days
Unique Orders                          65,752

Initial Interpretation

The analysis indicates a significant delivery-performance issue. The
late-delivery rate is 57.28%, meaning more than half of the analyzed
records are flagged as late.

Actual shipping time is also higher than scheduled shipping time:

Actual average: 3.50 days

Scheduled average: 2.93 days

Average variance: 0.57 days

These findings provide a clear starting point for further predictive and
optimization analysis.

🚚 Shipping Mode Analysis

Shipping Mode      Unique Orders   Avg. Shipping Days     Late Rate

First Class               10,079                 2.00   100.00%
Same Day                   3,571                 0.48    47.83%
Second Class              12,778                 3.99    79.73%
Standard Class            39,324                 4.00    39.77%

Observations

Standard Class has the largest number of orders.

First Class has the highest observed late-delivery rate in this
dataset.

Second Class also has a high late-delivery rate.

Same Day has the lowest average shipping duration among the
analyzed modes.

Shipping-mode performance should be investigated further together
with market, product, customer, and operational factors.

Note: These observations are descriptive findings from the dataset and
do not by themselves establish causation.

🌎 Market-Level Exploration

The project also analyzes order distribution across five markets:

LATAM

Europe

Pacific Asia

USA

Africa

The generated market visualization helps identify where order volume is
concentrated and can support future market-specific logistics planning.

📊 Visualizations

The project generates the following charts:

1. Distribution of Actual Shipping Days

Shows the frequency of different actual shipping durations.



2. Late Delivery Rate by Shipping Mode

Compares delivery-delay rates across shipping modes.



3. Orders by Market

Shows the distribution of records across geographic markets.



🧠 Data Science Methodologies

1. Exploratory Data Analysis (EDA)

EDA is used to understand:

Data structure

Missing values

Duplicate records

Variable distributions

Shipping performance

Market patterns

Shipping-mode behavior

2. Regression

Regression can be used in future stages to predict continuous logistics
outcomes such as:

Actual shipping duration

Shipping delay

Transportation-related cost

Expected delivery time

3. Classification

A classification model can predict whether an order is likely to
experience a late delivery.

The project includes a baseline Logistic Regression implementation that
can be extended with additional features and model comparison.

4. Clustering

K-Means clustering can be used to identify groups of customers or order
patterns based on variables such as:

Order frequency

Average order value

Quantity

Late-delivery rate

5. Optimization

Vehicle Routing Problem (VRP) techniques can be used to optimize
delivery routes while considering:

Distance

Delivery time

Vehicle capacity

Customer demand

Time windows

Google OR-Tools is included as the planned optimization framework.

🗺️ End-to-End Project Roadmap

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

📁 Project Structure

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

⚙️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

Google OR-Tools

VS Code

Git & GitHub

🚀 How to Run the Project

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd logistics_week1_github_project

2. Install dependencies

pip install -r requirements.txt

3. Add the dataset

Download the DataCo dataset and place the main CSV at:

data/DataCoSupplyChainDataset.csv

4. Run the Week 1 analysis

python notebooks/01_week1_exploration.py

5. View generated outputs

The analysis creates files inside:

outputs/

including KPI tables and visualization images.

📌 Key Business Problem

The initial analysis highlights delivery delays as a major logistics
problem.

With a late-delivery rate of 57.28%, the next stages of the project
should investigate:

What factors contribute most to late delivery?

Which markets experience higher delivery risk?

Which shipping modes require operational improvement?

Can late deliveries be predicted before shipment?

Can customer/order segments help improve logistics planning?

Can route optimization reduce delivery time and transportation
inefficiency?

💡 Expected Business Impact

A complete logistics analytics solution can help an organization:

Reduce late deliveries

Improve delivery-time prediction

Select appropriate shipping modes

Optimize transportation routes

Improve resource utilization

Identify high-risk orders

Segment customers and demand patterns

Support data-driven logistics decisions

🔮 Future Enhancements

Future versions of this project can include:

Advanced classification models such as Random Forest, XGBoost, or
Gradient Boosting.

Regression models for delivery-time prediction.

Customer segmentation using K-Means or hierarchical clustering.

Geographic route optimization using real coordinates.

Vehicle capacity and time-window constraints.

Interactive Power BI or Streamlit dashboard.

Real-time logistics monitoring.

Automated alerts for high-risk shipments.

Model explainability using feature importance or SHAP.

Deployment as a web-based logistics decision-support application.

📚 References and Resources

DataCo Smart Supply Chain dataset --- public Kaggle dataset

Mendeley Data --- DataCo Supply Chain Dataset

Google OR-Tools documentation --- vehicle routing and optimization

Scikit-learn documentation --- clustering and machine learning

Supply-chain KPI references from industry resources

📝 Week 1 Deliverables

Background research

Logistics problem definition

Project objectives

KPI identification

Public dataset research

Data profiling

Data exploration

KPI calculation

Shipping-mode analysis

Market analysis

Visualization generation

Regression/classification planning

Clustering planning

Route optimization planning

Python implementation

Strategic roadmap

Week 1 documentation

👩‍💻 Author

K. Thrisha Reddy

B.Tech --- Computer Science and Engineering (Data Science)

Vijaya Institute of Technology for Women, Vijayawada

⭐ Project Status

Week 1 --- Strategic Planning and Data Exploration: COMPLETED

The current version establishes the data foundation, identifies
important logistics KPIs, performs exploratory analysis, and defines the
roadmap for predictive analytics, clustering, and optimization.