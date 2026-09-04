# Week 2 – Data Collection, Cleaning & Preprocessing for Logistics Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Preprocessing-F7931E)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This project represents **Week 2 of the Logistics Data Analytics Project**.

The main objective of this week is to simulate a complete data preprocessing pipeline for logistics analysis. Raw logistics data is collected, inspected, cleaned, transformed, and prepared for further analytics and decision-making.

The project focuses on common data-quality problems found in logistics and supply-chain datasets, including missing values, duplicate records, inconsistent categorical values, invalid numerical values, and outliers.

The preprocessing process ensures that the dataset becomes reliable, consistent, and suitable for further statistical analysis, visualization, and machine learning.

---

## 🎯 Objectives

The main objectives of Week 2 are:

- Simulate logistics data collection.
- Inspect the quality of raw logistics data.
- Identify missing values.
- Remove duplicate records.
- Correct inappropriate data types.
- Standardize categorical values.
- Identify and correct invalid values.
- Detect outliers using the IQR method.
- Handle extreme values through outlier capping.
- Encode categorical variables.
- Normalize numerical variables.
- Generate a cleaned dataset for further analysis.

---

## 📊 Dataset

A simulated logistics dataset is used for this project.

The dataset contains information related to orders, delivery performance, transportation distance, freight cost, shipping method, customer segment, and delivery status.

### Dataset Attributes

| Column | Description |
|---|---|
| `Order_ID` | Unique identification number of the order |
| `Order_Date` | Date on which the order was placed |
| `Delivery_Days` | Number of days required for delivery |
| `Shipping_Mode` | Shipping method used for the order |
| `Distance_km` | Delivery distance in kilometers |
| `Freight_Cost` | Freight/transportation cost |
| `Quantity` | Number of units in the order |
| `Customer_Segment` | Type of customer |
| `Delivery_Status` | Current delivery status |

---

## ⚠️ Data Quality Issues

The raw dataset intentionally contains several realistic data-quality problems.

### 1. Missing Values

Some records contain missing values in numerical and categorical columns.

Examples:

- Missing delivery days
- Missing freight cost
- Missing distance
- Missing customer segment

### 2. Duplicate Records

Duplicate order records are included in the raw dataset to demonstrate duplicate detection and removal.

### 3. Inconsistent Categorical Values

Some categorical values contain:

- Different capitalization
- Unnecessary spaces
- Inconsistent formatting

For example:

```text
standard class
 Standard Class 
Standard Class
