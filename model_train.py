import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# 1. Load Data (Make sure insurance.csv is in this folder!)
df = pd.read_csv('insurance.csv')

# 2. Feature Engineering (Recreating your notebook logic)
df_feat = df.copy()
df_feat["bmi"] = df_feat["weight"] / (df_feat["height"] ** 2)

def age_group(age):
    if age < 25: return "young"
    elif age < 45: return "adult"
    elif age < 60: return "middle_aged"
    return "senior"

df_feat["age_group"] = df_feat["age"].apply(age_group)

def lifestyle_risk(row):
    if row["smoker"] and row["bmi"] > 30: return "high"
    elif row["smoker"] or row["bmi"] > 27: return "medium"
    return "low"

df_feat["lifestyle_risk"] = df_feat.apply(lifestyle_risk, axis=1)

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = ["Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Mysore", "Kota"] # Added Kota/Mysore from your sample

def city_tier(city):
    if city in tier_1_cities: return 1
    elif city in tier_2_cities: return 2
    return 3

df_feat["city_tier"] = df_feat["city"].apply(city_tier)

# 3. Prepare X and y
X = df_feat[["bmi", "age_group", "lifestyle_risk", "city_tier", "income_lpa", "occupation"]]
y = df_feat["insurance_premium_category"]

# 4. Pipeline Setup
categorical_features = ["age_group", "lifestyle_risk", "occupation", "city_tier"]
numeric_features = ["bmi", "income_lpa"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# 5. Train and Save
pipeline.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("SUCCESS: New model.pkl generated locally!")