import streamlit as st  
import pandas as pd 
import sqlite3 
import plotly.express as px 
with sqlite3.connect("./db/weather.db") as conn:
       query = """
       SELECT 
       cities.city_name,
       weather.temperature,
       weather.weather_condition
       FROM cities
       JOIN weather ON cities.city_id = weather.city_id;
       """
       df = pd.read_sql(query, conn)
       #st.write(df.columns)
       #st.write(df.head())
# APP title
st.title("Weather Dashboard")
st.write("This dashboard shows weather data scraped from multiple cities.")

# Sidebar filter
st.sidebar.header("City Options")
selected_city = st.sidebar.selectbox('Select City', df['city_name'].unique()) 
filtered_df = df[df['city_name'] == selected_city] 
       
# Selected city info
st.subheader(f"Weather for {selected_city}")
st.metric("Temperature", f"{filtered_df['temperature'].iloc[0]}°F")
st.write(f"Condition: {filtered_df['weather_condition'].iloc[0]}")
      
# Bar chart for current temperature by city
st.subheader('Temperature Comparison Across Cities') 
bar_chart = px.bar(
    df, x='city_name', 
    y='temperature', 
    title="Weather Temperature by City",
    labels={"city_name": "City", "temperature": "Temperature (°F)"}

    )

st.plotly_chart(bar_chart)

# Scatter chart
scatter_chart = px.scatter(
    df, x="city_name", 
    y="temperature", 
    color="weather_condition", 
    title="Explore weather data from different cities", 
    hover_data=["city_name", "temperature", "weather_condition"],
    labels={"city_name": "City", "temperature": "Temperature (°F)", "weather_condition": "Condition"}
    )
st.plotly_chart(scatter_chart)
      
with sqlite3.connect("./db/weather.db") as conn:       
       query = """
       SELECT cities.city_name, weather.temperature
       FROM cities
       JOIN weather
       ON cities.city_id = weather.city_id
       WHERE temperature > 80
       ORDER BY weather.temperature DESC
       limit 5;
       """
       hot_df = pd.read_sql(query, conn)
hot_chart = px.bar(
    hot_df, 
    x="city_name", 
    y="temperature", 
    title="Cities with Temperature Above 80°F",
    labels={"city_name": "City", "temperature": "Temperature (°F)"},
    color="temperature",
    color_continuous_scale="Reds"
    )
st.plotly_chart(hot_chart)  
