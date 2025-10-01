import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_auc_score
import joblib

def train():
    df = pd.read_csv("backend/app/ml/student_features.csv")
    X = df.drop(columns=["dropped_out"])
    y = df["dropped_out"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)
    preds = model.predict_proba(X_val)[:,1]
    print("AUC:", roc_auc_score(y_val, preds))
    joblib.dump(model, "backend/app/ml/risk_xgb_demo.joblib")
    print("model saved to risk_xgb_demo.joblib")

if __name__ == "__main__":
    train()
