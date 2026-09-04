# Week 1 Strategic Planning Report

## 1. Project Definition

### Scenario

An e-commerce logistics company wants to improve delivery reliability, reduce operational inefficiencies and make better transportation/resource-allocation decisions.

The analysis uses the DataCo SMART Supply Chain dataset to study order, shipping, product, market and geographic patterns.

### Core Questions

1. What factors are associated with late delivery?
2. Which shipping modes and markets show the highest delivery risk?
3. Which operational segments behave similarly?
4. How can route planning be optimized under capacity and time constraints?

## 2. KPIs

- Late Delivery Rate
- Average Actual Shipping Days
- Average Scheduled Shipping Days
- Shipping Variance
- Order Fulfilment Rate
- Profit per Order

## 3. Research and Methodology

### EDA
Use descriptive statistics and visualizations to understand distributions, missing data, outliers and group-level performance.

### Classification
Use Logistic Regression as an interpretable baseline for late-delivery risk.

### Regression
Future extension: predict continuous delivery duration or transportation cost.

### Clustering
Use K-Means to segment cities/customers/regions into operational groups.

### Optimization
Use Google OR-Tools to formulate a Vehicle Routing Problem using vehicle capacity, distance and time-window constraints.

## 4. Roadmap

```text
Problem Definition
        ↓
Data Collection
        ↓
Data Profiling
        ↓
Cleaning
        ↓
EDA
        ↓
KPI Analysis
        ↓
Feature Engineering
        ↓
Prediction
        ↓
Clustering
        ↓
Optimization
        ↓
Validation
        ↓
Recommendations
```

## 5. Data Leakage Control

For a pre-delivery prediction model, only information available at the prediction time should be used. Actual post-delivery outcomes must not be used as predictors.

## 6. Expected Impact

The final system is intended to help logistics managers identify high-risk orders, understand regional/shipping bottlenecks, prioritize interventions, and improve resource utilization.

## 7. References

- DataCo SMART Supply Chain: https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis
- Mendeley Data: https://data.mendeley.com/datasets/8gx2fvg2k6/5
- Google OR-Tools: https://developers.google.com/optimization
- scikit-learn: https://scikit-learn.org/
