import pandas as pd
import sqlite3 

# Load weather data 
df = pd.read_csv('weather_data_clean.csv')

# Connect to sqlite database
with sqlite3.connect('weather.db') as conn:
    # Create sqlite table and load dataframe into database
    df.to_sql('weather', conn, if_exists='replace', index=False)

    query = """
    SELECT * FROM weather
    LIMIT 5;
    """
    print(pd.read_sql(query, conn))
    
    # 
    query = """
    SELECT 
    city,
    temperature
    FROM weather
    WHERE temperature > 75;
    """
    print(pd.read_sql(query, conn))