import pandas as pd
import sqlite3
with sqlite3.connect('weather.db') as conn:
       query = """
       SELECT * FROM cities LIMIT 5;
       """
       print(pd.read_sql(query, conn))

       query = """
       SELECT *
       FROM cities
       JOIN weather ON cities.city_id = weather.city_id;
       """
       print(pd.read_sql(query, conn))
       
       query = """
       SELECT city_name, temperature
       FROM cities
       JOIN weather
       ON cities.city_id = weather.city_id
       WHERE temperature > 80;
       """
       print(pd.read_sql(query, conn))

       query = """
       SELECT 
       cities.city_name,
       weather.temperature
       FROM cities
       JOIN weather ON cities.city_id = weather.city_id;
       """
       print(pd.read_sql(query, conn))
      