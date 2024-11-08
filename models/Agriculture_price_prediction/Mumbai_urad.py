import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Step 1: Load Data from Excel
file_path = 'Mumbai_urad_.xlsx'  # Replace with your file path
df = pd.read_excel(file_path, engine='openpyxl')  # Use xlrd for .xls files

# Ensure the columns exist in the data
assert 'min_price' in df.columns, "min_price column is missing in the data"
assert 'max_price' in df.columns, "max_price column is missing in the data"
assert 'modal_price' in df.columns, "modal_price column is missing in the data"
assert 'date' in df.columns, "date column is missing in the data"

# Step 2: Prepare the Data
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')  # Adjust format if needed
df = df[['date', 'modal_price']]
df.columns = ['ds', 'y']  # Rename columns for Prophet

# Step 3: Initialize and Train Prophet Model
model = Prophet()
model.fit(df)

# Step 4: Make Future DataFrame
future = model.make_future_dataframe(periods=90)  # Adjust period as needed for future predictions

# Step 5: Forecast
forecast = model.predict(future)

# Step 6: Plot Results
fig = model.plot(forecast)
plt.show()