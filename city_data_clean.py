import pandas as pd
# Load raw weather data 
df = pd.read_csv('data/raw/city_data_raw.csv')
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

# Split 'City_time' into 'day_of_week' and 'local_time' columns
df[['day_of_week', 'local_time']] = df['city_time'].str.split(' ', n=1, expand=True)

# Preview cleaned data
print(df.head())

print('Cleaned data shape: ')
print(df.shape)

# Save cleaned data
df.to_csv('data/clean/city_data_clean.csv', index=False)
