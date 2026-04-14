import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

# -------------------
# TITLE
# -------------------
st.title("Gold Price Prediction App")

# -------------------
# LOAD DATA
# -------------------
df = pd.read_csv("Gold Price.csv")

# CLEAN DATA
for col in ['Price','Open','High','Low']:
    df[col] = df[col].astype(str).str.replace(',','')
    df[col] = df[col].astype(float)

def convert_volume(v):
    v = str(v)
    if 'K' in v:
        return float(v.replace('K','')) * 1e3
    elif 'M' in v:
        return float(v.replace('M','')) * 1e6
    return float(v)

df['Volume'] = df['Volume'].apply(convert_volume)
df['Chg%'] = df['Chg%'].astype(str).str.replace('%','').astype(float)

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# -------------------
# SHOW DATA
# -------------------
st.subheader("Dataset")
st.write(df.head())

# -------------------
# VISUALIZATION
# -------------------
st.subheader("Price Trend")
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Price'])
st.pyplot(fig)

# -------------------
# PREPARE MODEL
# -------------------
df['Date'] = df['Date'].map(pd.Timestamp.toordinal)

X = df[['Date','Open','High','Low','Volume','Chg%']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -------------------
# SELECT MODEL
# -------------------
model_name = st.selectbox(
    "Choose Model",
    ["Random Forest", "Gradient Boosting", "XGBoost"]
)

# -------------------
# TRAIN BUTTON
# -------------------
if st.button("Train Model"):

    if model_name == "Random Forest":
        model = RandomForestRegressor(n_estimators=100)

    elif model_name == "Gradient Boosting":
        model = GradientBoostingRegressor()

    else:
        model = XGBRegressor(objective='reg:squarederror')

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.subheader("Results")
    st.write(f"RMSE: {rmse:.2f}")
    st.write(f"MAE: {mae:.2f}")
    st.write(f"R2: {r2:.4f}")

    # Plot
    fig, ax = plt.subplots()
    ax.plot(y_test.values, label="Actual")
    ax.plot(y_pred, label="Predicted")
    ax.legend()
    st.pyplot(fig)
