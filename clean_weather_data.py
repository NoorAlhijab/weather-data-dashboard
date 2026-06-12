import pandas as pd
# Load raw weather data 
df = pd.read_csv('data/raw/weather_data_raw.csv')
print('Raw data shape: ')
print(df.shape)
#print(df.head())
# Check the data 
df.info()
# Check for duplicate rows
print('Duplicate rows: ')
print(df.duplicated().sum())

# Check missing values
print('Missing values: ')
print(df.isna().sum())

# Data cleaning and transformation

# Clean 'temperature' column and convert to integer
df['temperature'] =df['temperature'].str.replace(r'[°F\s]', '', regex=True)
df['temperature'] = pd.to_numeric(df['temperature'], errors="coerce")
#print(df['temperature'])

# Preview cleaned data
print(df.head())

print('Cleaned data shape: ')
print(df.shape)

# Save cleaned data
df.to_csv('data/clean/clean_weather_data.csv', index=False)
