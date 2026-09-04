import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ---------------------------------------------------------
# WEEK 2: LOGISTICS DATA CLEANING & PREPROCESSING
# ---------------------------------------------------------

INPUT_FILE = "logistics_data_raw.csv"
OUTPUT_FILE = "logistics_data_cleaned.csv"


# ---------------------------------------------------------
# 1. LOAD RAW DATA
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("\n========================================")
print("RAW LOGISTICS DATA")
print("========================================")

print(df.head())
print("\nDataset Shape:", df.shape)


# ---------------------------------------------------------
# 2. INITIAL DATA QUALITY CHECK
# ---------------------------------------------------------

print("\n========================================")
print("MISSING VALUES BEFORE CLEANING")
print("========================================")

print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# ---------------------------------------------------------
# 3. REMOVE DUPLICATE RECORDS
# ---------------------------------------------------------

df = df.drop_duplicates()

print("\nDuplicate rows removed successfully.")


# ---------------------------------------------------------
# 4. CONVERT DATA TYPES
# ---------------------------------------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

numeric_columns = [
    "Delivery_Days",
    "Distance_km",
    "Freight_Cost",
    "Quantity"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ---------------------------------------------------------
# 5. STANDARDIZE CATEGORICAL VALUES
# ---------------------------------------------------------

categorical_columns = [
    "Shipping_Mode",
    "Customer_Segment",
    "Delivery_Status"
]

for column in categorical_columns:

    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.title()
    )


print("\nCategorical values standardized.")


# ---------------------------------------------------------
# 6. BUSINESS RULE VALIDATION
# ---------------------------------------------------------

# Delivery days cannot be negative
df.loc[
    df["Delivery_Days"] < 0,
    "Delivery_Days"
] = pd.NA


# Distance cannot be negative
df.loc[
    df["Distance_km"] < 0,
    "Distance_km"
] = pd.NA


# Freight cost cannot be negative
df.loc[
    df["Freight_Cost"] < 0,
    "Freight_Cost"
] = pd.NA


# Quantity must be greater than zero
df.loc[
    df["Quantity"] <= 0,
    "Quantity"
] = pd.NA


print("Invalid values converted to missing values.")


# ---------------------------------------------------------
# 7. HANDLE MISSING NUMERICAL VALUES
# ---------------------------------------------------------

for column in numeric_columns:

    median_value = df[column].median()

    df[column] = df[column].fillna(
        median_value
    )


print("\nNumerical missing values filled using median.")


# ---------------------------------------------------------
# 8. HANDLE MISSING CATEGORICAL VALUES
# ---------------------------------------------------------

for column in categorical_columns:

    if df[column].isna().any():

        mode_value = df[column].mode()[0]

        df[column] = df[column].fillna(
            mode_value
        )


print("Categorical missing values filled using mode.")


# ---------------------------------------------------------
# 9. OUTLIER DETECTION USING IQR
# ---------------------------------------------------------

def cap_iqr(data, column):

    Q1 = data[column].quantile(0.25)

    Q3 = data[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)

    upper_bound = Q3 + (1.5 * IQR)

    outliers = (
        (data[column] < lower_bound) |
        (data[column] > upper_bound)
    ).sum()

    print(
        f"{column}: {outliers} potential outliers detected"
    )

    data[column] = data[column].clip(
        lower=lower_bound,
        upper=upper_bound
    )

    return data


print("\n========================================")
print("OUTLIER DETECTION")
print("========================================")

outlier_columns = [
    "Delivery_Days",
    "Distance_km",
    "Freight_Cost"
]

for column in outlier_columns:

    df = cap_iqr(
        df,
        column
    )


# ---------------------------------------------------------
# 10. ONE-HOT ENCODING
# ---------------------------------------------------------

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True,
    dtype=int
)

print("\nCategorical variables encoded successfully.")


# ---------------------------------------------------------
# 11. MIN-MAX NORMALIZATION
# ---------------------------------------------------------

scaler = MinMaxScaler()

df[numeric_columns] = scaler.fit_transform(
    df[numeric_columns]
)


print("Numerical variables normalized successfully.")


# ---------------------------------------------------------
# 12. SAVE CLEANED DATA
# ---------------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ---------------------------------------------------------
# 13. FINAL QUALITY CHECK
# ---------------------------------------------------------

print("\n========================================")
print("FINAL CLEANED DATA")
print("========================================")

print(df.head())

print("\nFinal Dataset Shape:", df.shape)

print("\nMissing Values After Cleaning:")

print(df.isnull().sum())

print(
    "\nDuplicate Rows After Cleaning:",
    df.duplicated().sum()
)

print("\n========================================")
print("PREPROCESSING COMPLETED SUCCESSFULLY")
print("========================================")

print(
    f"\nCleaned dataset saved as: {OUTPUT_FILE}"
)
