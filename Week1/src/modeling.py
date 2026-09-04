from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

def train_late_risk_model(df):
    features = [
        "Order Item Quantity",
        "Order Item Total",
        "Shipping Mode",
        "Market",
        "Category Name"
    ]

    target = "late_flag"

    available = [c for c in features + [target] if c in df.columns]
    if target not in available:
        raise ValueError("late_flag is not available.")

    features = [c for c in features if c in df.columns]

    model_df = df[features + [target]].dropna()

    if model_df[target].nunique() < 2:
        raise ValueError("Target must contain at least two classes.")

    X = model_df[features]
    y = model_df[target]

    numeric = [c for c in features if c in [
        "Order Item Quantity",
        "Order Item Total"
    ]]
    categorical = [c for c in features if c in [
        "Shipping Mode",
        "Market",
        "Category Name"
    ]]

    preprocess = ColumnTransformer([
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])

    pipeline = Pipeline([
        ("preprocess", preprocess),
        ("model", LogisticRegression(max_iter=1000))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    probabilities = pipeline.predict_proba(X_test)[:, 1]

    metrics = {
        "roc_auc": roc_auc_score(y_test, probabilities),
        "classification_report": classification_report(
            y_test, predictions, output_dict=True
        )
    }

    return pipeline, metrics
