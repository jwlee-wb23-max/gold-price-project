3.1.1 Date& open
Figure 1: Historical price trends of gold (2014-2026)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Gold Price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Price', color='blue', label='Price')
plt.title('Historical price trends of gold (2014-2026)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

Figure 2: Daily Opening Price Fluctuations (2014-2026)
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Open', color='orange', label='Open')
plt.title('Daily Opening Price Fluctuations (2014-2026)')
plt.xlabel('Date')
plt.ylabel('Open')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

Figure 3: Comparison of Open and Price Trajectories (2014-2026)
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Open'], label='Open', color='orange', alpha=0.7)
plt.plot(df['Date'], df['Price'], label='Price', color='blue', alpha=0.5)
plt.title('Comparison of Open and Price Trajectories (2014-2026)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()


Figure 4: Correlation between Open and Price
plt.figure(figsize=(8, 8))
sns.regplot(data=df, x='Open', y='Price', scatter_kws={'alpha':0.3, 's':10}, line_kws={'color':'red'})
plt.title('Correlation between Open and Price')
plt.xlabel('Open')
plt.ylabel('Price')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()



3.1.2 High&Low
High & Low
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/kaggle/input/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series/Gold Price.csv")

print(df.head())
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
#HIGH
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='High', label='High')

plt.title('Daily Highest Price of Gold (2014–2026)')
plt.xlabel('Date')
plt.ylabel('High Price')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('figure_2_13_high.png')
plt.show()
#LOW
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Low', label='Low', color = 'red')

plt.title('Daily Lowest Price of Gold (2014–2026)')
plt.xlabel('Date')
plt.ylabel('Low Price')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('figure_2_14_low.png')
plt.show()


3.1.3 Volume & Chg%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("Downloads/Gold Price.csv")
plt.figure()
plt.plot(df["Date"],df["Volume"])

plt.title("Gold Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")

plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

plt.show()
df["Date"]=pd.to_datetime(df["Date"])
df=df.sort_values("Date")

plt.figure()
plt.plot(df["Date"],df["Volume"])

plt.title("Gold Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
plt.figure()
sns.histplot(df["Chg%"],bins=30)

plt.title("Distribution of Gold Price Percentage Change")
plt.xlabel("Percentage Change")
plt.ylabel("Frequency")

plt.show()
plt.figure()
plt.scatter(df["Volume"],df["Price"])

plt.title("Relationship Between Volume and Gold Price")
plt.xlabel("Volume")
plt.ylabel("Price")
plt.show()




3.2 Price
Figure 1: Summary Statistics of Gold Closing Price (2014–2026)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Gold Price.csv")
df['Date'] = pd.to_datetime(df['Date'])

print("Figure 1:Summary Statistics of Gold Price (2014–2026)")
summary = df['Price'].describe()
summary_df = pd.DataFrame(summary).rename(columns={'Price':'Value'})
print(price_summary)

Figure 2: Daily Gold Price Trend from 2014 to 2026
plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Price'], color='gold')
plt.title("Figure 2: Daily Gold Price Trend from 2014 to 2026")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("figure2_gold_price_trend.png")
plt.show()

Figure 3: Distribution of Daily Gold Prices
plt.figure(figsize=(8,5))
plt.hist(df['Price'], bins=30, color='orange', edgecolor='black')
plt.title("Figure 3: Distribution of Daily Gold Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figure3_gold_price_distribution.png")
plt.show()

Figure 4: Minimum and Maximum Daily Gold Prices

min_price = df['Price'].min()
max_price = df['Price'].max()

plt.figure(figsize=(6,4))
plt.bar(['Minimum Price','Maximum Price'], [min_price, max_price], color=['green','red'])
plt.title("Figure 4: Minimum and Maximum Daily Gold Prices")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("figure4_gold_price_range.png")
plt.show()

4.0 Data Cleaning
import pandas as pd
df=pd.read_csv("/kaggle/input/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series/Gold Price.csv")
df.head()
df.isnull().sum()

4.3 Data Combination
Figure 5: Gold Price Time Series with Merged Holiday Events
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('future.no_silent_downcasting', True)

try:
    df = pd.read_csv('Gold Price.csv')
    df['Date'] = pd.to_datetime(df['Date'])
except FileNotFoundError:
    print("Error: 'Gold Price.csv' not found.")

df = df.sort_values('Date')

holiday_dates = [
    '2014-01-31','2015-02-19','2016-02-08','2017-01-28',
    '2018-02-16','2019-02-05','2020-01-25','2021-02-12',
    '2022-02-01','2023-01-22','2024-02-10','2025-01-29','2026-02-17',
    '2014-12-25','2015-12-25','2016-12-25','2017-12-25',
    '2018-12-25','2019-12-25','2020-12-25','2021-12-25',
    '2022-12-25','2023-12-25','2024-12-25','2025-12-25','2026-12-25'
]

holiday_dates = pd.to_datetime(holiday_dates)

df['Is_Holiday'] = df['Date'].apply(
    lambda x: any(abs((x - d).days) <= 1 for d in holiday_dates)
)

df['Day_Type'] = df['Is_Holiday'].map({
    True: 'Holiday',
    False: 'Normal Day'
})

df['Abs_Chg'] = df['Price'].pct_change().abs() * 100

df['Daily_Volatility'] = df['High'] - df['Low']

summary = df.groupby('Day_Type').agg({
    'Abs_Chg': 'mean',
    'Daily_Volatility': 'mean',
    'Volume': 'mean'
})

print("\n=== Summary Comparison ===")
print(summary)

sns.set_style("whitegrid")

plt.figure(figsize=(15, 6))
plt.plot(df['Date'], df['Price'], color='#E0E0E0', linewidth=1, label='Daily Gold Price')

holidays = df[df['Is_Holiday']]
plt.scatter(holidays['Date'], holidays['Price'], color='red', s=30, label='Holiday')

plt.title('Gold Price Time Series with Holiday Events')
plt.legend()
plt.show()

Figure 6: Average Daily Price Range (High - Low)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

order = ['Holiday', 'Normal Day']

sns.barplot(
    data=df,
    x='Day_Type',
    y='Abs_Chg',
    hue='Day_Type',
    palette='Oranges',
    order=order,
    ax=ax1,
    errorbar=None,
    legend=False
)

ax1.set_title('Average Absolute Price Fluctuation (%)')
ax1.set_ylabel('|Price Change| (%)')
ax1.set_xlabel('Day Type')

sns.barplot(
    data=df,
    x='Day_Type',
    y='Daily_Volatility',
    hue='Day_Type',
    palette='Blues',
    order=order,
    ax=ax2,
    errorbar=None,
    legend=False
)

ax2.set_title('Average Daily Price Range (High - Low)')
ax2.set_ylabel('Volatility')
ax2.set_xlabel('Day Type')

plt.suptitle('Market Volatility Comparison')
plt.tight_layout()
plt.show()

Figure 7: Average Trading Volume Comparison
plt.figure(figsize=(8, 6))

sns.barplot(
    data=df,
    x='Day_Type',
    y='Volume',
    hue='Day_Type',
    palette='viridis',
    errorbar=None,
    legend=False
)

plt.title('Average Trading Volume Comparison')
plt.ylabel('Average Volume')
plt.xlabel('Day Type')
plt.tight_layout()
plt.show()

4.3 data transformation
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv("Gold Price.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Price'] = df['Price'].ffill()
scaler = MinMaxScaler()
df['Price_Normalized'] = scaler.fit_transform(df[['Price']])
df['Price_Log'] = np.log(df['Price'])
df.head()
Random forest 
3.
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

df = pd.read_csv('Gold Price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

df['Lag1'] = df['Price'].shift(1)
df['Price_Diff'] = df['Price'] - df['Lag1']
df = df.dropna().reset_index(drop=True)

X = df[['Lag1']]
y = df['Price_Diff']

split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]
actual_price = df['Price'].iloc[split:]

rf = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42)
rf.fit(X_train, y_train)

pred_diff = rf.predict(X_test)
final_pred = X_test['Lag1'] + pred_diff

mae_manual = np.mean(np.abs(actual_price - final_pred))
rmse_manual = np.sqrt(np.mean((actual_price - final_pred)**2))

ss_res = np.sum((actual_price - final_pred)**2)
ss_tot = np.sum((actual_price - np.mean(actual_price))**2)
r2_manual = 1 - (ss_res / ss_tot)

mape_manual = np.mean(np.abs((actual_price - final_pred) / actual_price)) * 100

mae_sk = mean_absolute_error(actual_price, final_pred)

mse_val = mean_squared_error(actual_price, final_pred)
rmse_sk = np.sqrt(mse_val) 

r2_sk = r2_score(actual_price, final_pred)
mape_sk = mean_absolute_percentage_error(actual_price, final_pred) * 100

print("=== METRICS COMPARISON (RANDOM FOREST) ===")
print(f"{'Metric':<10} | {'Manual (Numpy)':<18} | {'Default (Sklearn)':<18}")
print("-" * 55)

print(f"{'MAE':<10} | {mae_manual:<18.6f} | {mae_sk:<18.6f}")
print(f"{'RMSE':<10} | {rmse_manual:<18.6f} | {rmse_sk:<18.6f}")
print(f"{'R2':<10} | {r2_manual:<18.6f} | {r2_sk:<18.6f}")
print(f"{'MAPE (%)':<10} | {mape_manual:<18.6f} | {mape_sk:<18.6f}")


Gradient boosting 
!pip install pandas numpy scikit-learn xgboost
import pandas as pd

file_path = r"C:\Users\Kitty Lim\Downloads\Gold Price.csv"
df = pd.read_csv(file_path)

df.head()
import numpy as np

for col in ['Price','Open','High','Low']:
    df[col] = df[col].astype(str).str.replace(',','', regex = False)
    df[col] = df[col].astype(float)
    # as to remove "," change to float

def convert_volume(v):
    v = str(v)
    if 'K' in v:
        return float (v.replace('K',''))* 1e3
    elif 'M' in v:
        return float (v.replace('M',''))* 1e6
    else:
        return float(v)

df['Volume'] = df['Volume'].apply(convert_volume)
    # as to process volume (K=thousand, M= million) 

df['Chg%'] = df['Chg%'].astype(str).str.replace('%','', regex = False)
df['Chg%'] = df['Chg%'].astype(float)
    # as to process Chg%

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
    # as to process Date to Time then change to number

df.head
X = df[['Date','Open','High','Low','Volume','Chg%']]

y = df['Price']

from sklearn.model_selection import train_test_split, GridSearchCV

X_train, X_test, y_train, y_test = train_test_split (
    X, y, test_size = 0.2, random_state = 42)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error
import numpy as np

def evaluate(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score (y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true))* 100

    return rmse, mae, r2, mape
from sklearn.ensemble import GradientBoostingRegressor

print ("- - - - Gradient Boosting - - - -")

gb_default = GradientBoostingRegressor(random_state = 42)
gb_default.fit(X_train, y_train)
y_pred_gb_default = gb_default.predict(X_test)

rmse_gb_default = np.sqrt(mean_squared_error(y_test, y_pred_gb_default))
mae_gb_default = mean_absolute_error(y_test, y_pred_gb_default)
r2_gb_default = r2_score(y_test, y_pred_gb_default)
mape_gb_default = mean_absolute_percentage_error(y_test, y_pred_gb_default)
print(f"Default GB -> RMSE: {rmse_gb_default:.2f}, MAE: {mae_gb_default:.2f}, R²: {r2_gb_default:.4f}, MAPE: {mape_gb_default:.2f}%")

gb_manual = GradientBoostingRegressor(n_estimators=150, learning_rate=0.5, max_depth=4, random_state=42)
gb_manual.fit(X_train, y_train)
y_pred_gb_manual = gb_manual.predict(X_test)

rmse_gb_manual = np.sqrt(mean_squared_error(y_test, y_pred_gb_manual))
mae_gb_manual = mean_absolute_error(y_test, y_pred_gb_manual)
r2_gb_manual = r2_score(y_test, y_pred_gb_manual)
mape_gb_manual = mean_absolute_percentage_error(y_test, y_pred_gb_manual)
print(f"Manual Tuned GB -> RMSE: {rmse_gb_manual:.2f}, MAE: {mae_gb_manual:.2f}, R²: {r2_gb_manual:.4f}, MAPE: {mape_gb_manual:.2f}%")

param_grid_gb = {
    'n_estimators': [100, 150, 200],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 4, 5]
}

grid_gb = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid_gb, cv=3, scoring='neg_mean_squared_error')
grid_gb.fit(X_train, y_train)

best_gb = grid_gb.best_estimator_
y_pred_gb_best = best_gb.predict(X_test)

rmse_gb_best = np.sqrt(mean_squared_error(y_test, y_pred_gb_best))
mae_gb_best = mean_absolute_error(y_test, y_pred_gb_best)
r2_gb_best = r2_score(y_test, y_pred_gb_best)
mape_gb_best = mean_absolute_percentage_error(y_test, y_pred_gb_best)

print(f"Best GB Params: {grid_gb.best_params_}")
print(f"Best GB -> RMSE: {rmse_gb_best:.2f}, MAE: {mae_gb_best:.2f}, R²: {r2_gb_best:.4f}, MAPE: {mape_gb_best:.2f}%")


from xgboost import XGBRegressor

print("\n----- XGBoost -----")

xgb_default = XGBRegressor(random_state=42, objective='reg:squarederror')
xgb_default.fit(X_train, y_train)
y_pred_xgb_default = xgb_default.predict(X_test)

rmse_xgb_default = np.sqrt(mean_squared_error(y_test, y_pred_xgb_default))
mae_xgb_default = mean_absolute_error(y_test, y_pred_xgb_default)
r2_xgb_default = r2_score(y_test, y_pred_xgb_default)
mape_xgb_default = mean_absolute_percentage_error(y_test, y_pred_xgb_default)
print(f"Default XGB -> RMSE: {rmse_xgb_default:.2f}, MAE: {mae_xgb_default:.2f}, R²: {r2_xgb_default:.4f}, MAPE: {mape_xgb_default:.2f}%")

xgb_manual = XGBRegressor(n_estimators=150, learning_rate=0.5, max_depth=4, random_state=42)
xgb_manual.fit(X_train, y_train)
y_pred_xgb_manual = xgb_manual.predict(X_test)

rmse_xgb_manual = np.sqrt(mean_squared_error(y_test, y_pred_xgb_manual))
mae_xgb_manual = mean_absolute_error(y_test, y_pred_xgb_manual)
r2_xgb_manual = r2_score(y_test, y_pred_xgb_manual)
mape_xgb_manual = mean_absolute_percentage_error(y_test, y_pred_xgb_manual)
print(f"Manual Tuned XGB -> RMSE: {rmse_xgb_manual:.2f}, MAE: {mae_xgb_manual:.2f}, R²: {r2_xgb_manual:.4f}, MAPE: {mape_xgb_manual:.2f}%")

param_grid_xgb = {
    'n_estimators': [100, 150, 200],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 4, 5]
}

grid_xgb = GridSearchCV(XGBRegressor(random_state=42, objective='reg:squarederror'), param_grid_xgb, cv=3, scoring='neg_mean_squared_error')
grid_xgb.fit(X_train, y_train)

best_xgb = grid_xgb.best_estimator_
y_pred_xgb_best = best_xgb.predict(X_test)

rmse_xgb_best = np.sqrt(mean_squared_error(y_test, y_pred_xgb_best))
mae_xgb_best = mean_absolute_error(y_test, y_pred_xgb_best)
r2_xgb_best = r2_score(y_test, y_pred_xgb_best)
mape_xgb_best = mean_absolute_percentage_error(y_test, y_pred_xgb_best)

print(f"Best XGB Params: {grid_xgb.best_params_}")
print(f"Best XGB -> RMSE: {rmse_xgb_best:.2f}, MAE: {mae_xgb_best:.2f}, R²: {r2_xgb_best:.4f}, MAPE: {mape_xgb_best:.2f}%")
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train,y_train)
y_pred_gbr = gbr.predict(X_test)

from xgboost import XGBRegressor
xgb = XGBRegressor (random_state=42, objective= 'reg:squarederror')
xgb.fit(X_train,y_train)
y_pred_xgb = xgb.predict(X_test)

# Gradient Boosting
rmse_gbr, mae_gbr, r2_gbr, mape_gbr = evaluate (y_test, y_pred_gbr)

print("Gradient Boosting Results:")
print(f"RMSE:{rmse_gbr:.4f}")
print(f"MAE:{mae_gbr:.4f}")
print(f"R2:{r2_gbr:.4f}")
print(f"MAPE:{mape_gbr:.4f}")

# XGBoost
rmse_xgb, mae_xgb, r2_xgb, mape_xgb = evaluate(y_test, y_pred_xgb)

print("\nXGBoost Results:")
print(f"RMSE:{rmse_xgb:.4f}")
print(f"MAE:{mae_xgb:.4f}")
print(f"R2:{r2_xgb:.4f}")
print(f"MAPE:{mape_xgb:.4f}")
import pandas as pd

results = pd.DataFrame({
    'Model': ['XGBoost','Gradient Boosting'],
    'RMSE': [rmse_xgb,rmse_gbr],
    'MAE': [mae_xgb,mae_gbr],
    'R2' : [r2_xgb,r2_gbr],
    'MAPE': [mape_xgb, mape_xgb]
})

results.round(4)
import pandas as pd

results = pd.DataFrame({
    'Model': ['GB Default', 'GB Manual', 'XGB Default', 'XGB Manual'],
    'RMSE': [rmse_gb_default, rmse_gb_manual, rmse_xgb_default, rmse_xgb_manual],
    'MAE': [mae_gb_default, mae_gb_manual, mae_xgb_default, mae_xgb_manual],
    'R2': [r2_gb_default, r2_gb_manual, r2_xgb_default, r2_xgb_manual],
    'MAPE': [mape_gb_default, mape_gb_manual, mape_xgb_default, mape_xgb_manual]
})

print(results)


LSTM
LSTM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
df=pd.read_csv("/kaggle/input/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series/Gold Price.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
data = df['Price'].values.reshape(-1,1)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)
def create_sequences(data, time_step=60):
    X, y = [], []
    for i in range(time_step, len(data)):
        X.append(data[i-time_step:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

time_step = 60
X, y = create_sequences(data_scaled, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)  

train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

model = Sequential()
model.add(Input(shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=25, batch_size=32, verbose=1)
y_pred = model.predict(X_test)

y_pred_inv = scaler.inverse_transform(y_pred)
y_test_inv = scaler.inverse_transform(y_test.reshape(-1,1))
rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))

mae = mean_absolute_error(y_test_inv, y_pred_inv)

r2 = r2_score(y_test_inv, y_pred_inv)

mape = np.mean(np.abs((y_test_inv - y_pred_inv) / y_test_inv))

print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")
print("MAPE:", mape)
#Manual MAPE
epoch_list = [10, 20, 25]
unit_list = [50, 100]

results = []

for epochs in epoch_list:
    for units in unit_list:

        model = Sequential()
        model.add(Input(shape=(time_step,1)))
model.add(LSTM(units, return_sequences=True))
model.add(LSTM(units))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=epochs, batch_size=32, verbose=0)

y_pred = model.predict(X_test)
y_pred_inv = scaler.inverse_transform(y_pred)
y_test_inv = scaler.inverse_transform(y_test.reshape(-1,1))
        
mape = np.mean(np.abs((y_test_inv - y_pred_inv) / y_test_inv))

results.append((epochs, units, mape))

print(f"Epochs: {epochs}, Units: {units}, MAPE: {mape:.6f}")
plt.figure(figsize=(12,6))
plt.plot(df['Date'][len(df)-len(y_test_inv):], y_test_inv, color='blue', label='Actual Price')
plt.plot(df['Date'][len(df)-len(y_test_inv):], y_pred_inv, color='red', label='Predicted Price')
plt.title('LSTM Predicted vs Actual Daily Gold Price')
plt.xlabel('Date')
plt.ylabel('Price (RM)')
plt.legend()
plt.grid(True)
plt.show()


Hybrid (Random forest + lstm)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

#Load Data
df = pd.read_csv('Gold Price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

data = df['Price'].values.reshape(-1,1)

#LSTM Preprocessing
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

def create_sequences(data, time_step=60):
    X, y = [], []
    for i in range(time_step, len(data)):
        X.append(data[i-time_step:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

time_step = 60
X_lstm, y_lstm = create_sequences(data_scaled, time_step)

X_lstm = X_lstm.reshape(X_lstm.shape[0], X_lstm.shape[1], 1)

split = int(len(X_lstm) * 0.8)

X_train_lstm = X_lstm[:split]
X_test_lstm  = X_lstm[split:]

y_train_lstm = y_lstm[:split]
y_test_lstm  = y_lstm[split:]

#Build LSTM Model
model = Sequential()
model.add(Input(shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

model.fit(X_train_lstm, y_train_lstm, epochs=20, batch_size=32, verbose=1)



# LSTM Predictions (for hybrid & standalone plot)
lstm_pred = model.predict(X_lstm)
lstm_pred_inv = scaler.inverse_transform(lstm_pred).flatten()

#Align dataframe with LSTM output
df_lstm = df.iloc[time_step:].copy()

# Create LSTM dataframe with Date
lstm_df = pd.DataFrame({
    'Date': df_lstm['Date'].values,
    'LSTM_Pred': lstm_pred_inv
})

# Merge safely
df_hybrid = df.merge(lstm_df, on='Date', how='inner')
# Create RF Features
df_hybrid['Lag1'] = df_hybrid['Price'].shift(1)
df_hybrid['Price_Diff'] = df_hybrid['Price'] - df_hybrid['Lag1']

df_hybrid = df_hybrid.dropna()

X = df_hybrid[['Lag1', 'LSTM_Pred']]
y = df_hybrid['Price_Diff']

split = int(len(X) * 0.8)

X_train_rf = X.iloc[:split]
X_test_rf  = X.iloc[split:]

y_train_rf = y.iloc[:split]
y_test_rf  = y.iloc[split:]

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train_rf, y_train_rf)

# Hybrid Predictions
pred_diff = rf.predict(X_test_rf)

final_pred = X_test_rf['Lag1'] + pred_diff
actual = df_hybrid['Price'].iloc[split:]

#Evaluation
rmse = np.sqrt(mean_squared_error(actual, final_pred))
mae = mean_absolute_error(actual, final_pred)
r2 = r2_score(actual, final_pred)

#FORCE both to pure NumPy arrays (this is the key fix)
actual_np = actual.to_numpy()
pred_np = np.array(final_pred)

# Default MAPE
mape = np.mean(np.abs((actual_np - pred_np) / actual_np)) * 100

# Manual MAPE
errors = []
for i in range(len(actual_np)):
    if actual_np[i] != 0:
        error = abs((actual_np[i] - pred_np[i]) / actual_np[i])
        errors.append(error)

mape_manual = (sum(errors) / len(errors)) * 100

print("\n=== METRICS COMPARISON (HYBRID MODEL) ===")
print(f"{'Metric':<10} | {'Manual (Numpy)':<18} | {'Default (Sklearn)':<18}")
print("-"*55)
print(f"{'MAE':<10} | {mae:<18.6f} | {mae:<18.6f}")
print(f"{'RMSE':<10} | {rmse:<18.6f} | {rmse:<18.6f}")
print(f"{'R2':<10} | {r2:<18.6f} | {r2:<18.6f}")
print(f"{'MAPE (%)':<10} | {mape:<18.6f} | {mape:<18.6f}")

#Hybrid Graph
plt.figure(figsize=(12,6))
plt.plot(df_hybrid['Date'].iloc[split:], actual, label='Actual')
plt.plot(df_hybrid['Date'].iloc[split:], final_pred, label='Hybrid Prediction')
plt.legend()
plt.title("Hybrid Model (LSTM + RF)")
plt.show()

