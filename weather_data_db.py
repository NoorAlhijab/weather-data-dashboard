import pandas as pd
import sqlalchemy as sa
import sqlite3
import os 
if os.path.exists("weather.db"):
    answer = input("The database exists.  Do you want to recreate it (y/n)?")
    if answer.lower() != 'y':
        exit(0)
    os.remove("weather.db")

# Load cleaned csvs datasets
city_df = pd.read_csv('data/clean/city_data_clean.csv')
weather_df = pd.read_csv('data/clean/weather_data_clean.csv')

# Connect to sqlite database
with sqlite3.connect('weather.db') as conn:
    conn.execute("PRAGMA foreign_keys = 1") 
    cursor = conn.cursor()
    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY,
        city_name TEXT,
        city_time TEXT,
        day_of_week TEXT,
        local_time  TEXT         
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        weather_id INTEGER PRIMARY KEY,
        city_id INTEGER,
        temperature TEXT NOT NULL,
        weather_condition TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(city_id)

    )
    """)
    # Create a database engine
    engine = sa.create_engine('sqlite:///weather.db')
    # Insert data into tables
    city_df.to_sql('cities', engine, if_exists='append', index=False) 
    weather_df.to_sql('weather', engine, if_exists='append', index=False)