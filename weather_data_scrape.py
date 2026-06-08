import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Load weather page
driver.get('https://www.timeanddate.com/weather/')
item_list = driver.find_elements(By.CSS_SELECTOR, 'table.zebra.fw.tb-theme > tbody > tr')
#print(item_list)
results = []
for row in item_list:
    try:
        # Extract city name
        city= row.find_element(By.CSS_SELECTOR, 'td > a')
        #print(city.text)
        # Extract local city time
        city_time = row.find_element(By.CSS_SELECTOR,'td.r')
        #print(time.text)
        # Extract weather conditions 
        image = row.find_element(By.CSS_SELECTOR,'td.r > img[alt]')
        alt_text = image.get_attribute("alt")
        #print(alt_text)
        # Extract temperature for each city
        temperature = row.find_element(By.CSS_SELECTOR,'td.rbi')
        #print(temperature)
        items_dict = {
            'city': city.text,
            'city_time': city_time.text,
            'weather_condition': alt_text,
            'temperature': temperature.text
        }
        results.append(items_dict)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue
print(results)

# Create dataframe
df_raw = pd.DataFrame(results)
#print(df_raw)
df_raw.to_csv('weather_data_raw.csv', index=False)
driver.quit()


