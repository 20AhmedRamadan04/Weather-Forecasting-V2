# **Cairo Historical Weather Data Collection**

This project collects **3 years of historical weather data for Cairo, Egypt** using the **Open-Meteo API**. The data is fetched, processed, and saved into a CSV file for further analysis and modeling, particularly for **climate risk prediction using LSTM models**.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Code Overview](#code-overview)
4. [Data Description](#data-description)
5. [How to Use](#how-to-use)
6. [Next Steps](#next-steps)
7. [Current Weather Data](#Current-Weather-Data)

---

## **Introduction**
This script fetches **hourly historical weather data** for Cairo, Egypt, over the past **3 years**. The data includes various meteorological parameters such as temperature, humidity, precipitation, wind speed, and soil conditions. The collected data is saved in a CSV file (`cairo_historical_weather_3_years.csv`) for use in machine learning models, particularly **LSTM-based climate risk prediction**.

---

## **Features**
The script collects the following weather variables:
- **Temperature**: `temperature_2m`, `apparent_temperature`, `dew_point_2m`
- **Humidity**: `relative_humidity_2m`, `vapour_pressure_deficit`
- **Precipitation**: `precipitation`, `rain`, `snowfall`, `snow_depth`
- **Pressure**: `pressure_msl`, `surface_pressure`
- **Cloud Cover**: `cloud_cover`, `cloud_cover_low`, `cloud_cover_mid`, `cloud_cover_high`
- **Wind**: `wind_speed_10m`, `wind_speed_100m`, `wind_direction_10m`, `wind_direction_100m`, `wind_gusts_10m`
- **Soil Data**: Soil temperature and moisture at various depths.

---

## **Code Overview**
The script is written in Python and uses the following libraries:
- `openmeteo_requests`: To interact with the Open-Meteo API.
- `requests_cache`: To cache API requests for faster repeated access.
- `pandas`: To process and store the data in a structured format.
- `retry_requests`: To handle failed API requests with retries.

### **Key Steps**
1. **Set Up API Client**:
   - A cached session is created to avoid redundant API calls.
   - Retry logic is added to handle failed requests.

2. **Define API Parameters**:
   - The latitude and longitude of Cairo are specified.
   - The date range is set to the past 3 years.
   - The required weather variables are listed.

3. **Fetch Data**:
   - The API request is sent, and the response is processed.

4. **Process Data**:
   - The hourly data is extracted and stored in a dictionary.
   - The dictionary is converted into a Pandas DataFrame.

5. **Save Data**:
   - The DataFrame is saved as a CSV file (`cairo_historical_weather_3_years.csv`).

---

## **Data Description**
The collected data includes the following columns:
- **Date**: Timestamp for each hourly record.
- **Temperature**: Temperature at 2 meters above ground.
- **Humidity**: Relative humidity at 2 meters above ground.
- **Precipitation**: Total precipitation, rain, snowfall, and snow depth.
- **Pressure**: Atmospheric pressure at mean sea level and surface pressure.
- **Wind**: Wind speed, direction, and gusts at 10m and 100m heights.
- **Cloud Cover**: Total, low, mid, and high cloud cover percentages.
- **Soil Data**: Temperature and moisture at various soil depths.

---

## **How to Use**
1. **Install Dependencies**:
   Ensure you have the required Python libraries installed:
   ```bash
   pip install openmeteo-requests requests-cache pandas retry-requests
2. **Run the Script**:
   Execute the script to fetch and save the data:
   ```bash
   python fetch_weather_data.py
3. **Output**:
   The script will generate a CSV file (cairo_historical_weather_3_years.csv) containing the historical weather data.
## **Next Steps**
1. **Data Preprocessing**:
   - Handle missing values (e.g., using interpolation or dropping rows).
   - Normalize or standardize the data for better LSTM performance.

2. **Feature Engineering**:
   - Create additional features like:
     - `temperature_change`: Change in temperature over time.
     - `precipitation_intensity`: Intensity of precipitation.

3. **Model Training**:
   - Use the preprocessed data to train an **LSTM model** for climate risk prediction.

4. **Visualization**:
   - Visualize trends in the data (e.g., temperature, precipitation) using libraries like `matplotlib` or `seaborn`.

---

## **Contributing**
Feel free to contribute to this project by:
- Adding more features to the dataset.
- Improving the data preprocessing pipeline.
- Enhancing the LSTM model for better predictions.

## **Current Weather Data**
To fetch **current weather data** for Cairo, use the following script. This script collects the same weather variables as the historical data but focuses on the **latest available data**.

### **How to Use**
1. **Install Dependencies**:
   Ensure you have the required Python libraries installed:
   ```bash
   pip install openmeteo-requests requests-cache pandas retry-requests
2. Run the Script:
   Execute the script to fetch and save the current weather data:
   python fetch_current_weather.py
3. Output:
   The script will generate a CSV file (cairo_current_weather.csv) containing the latest weather data.

### **Contributing**
Feel free to contribute to this project by:

Adding more features to the dataset.

Improving the data preprocessing pipeline.

Enhancing the LSTM model for better predictions.
