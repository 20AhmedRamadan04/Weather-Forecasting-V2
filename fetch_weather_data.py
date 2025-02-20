# Import necessary libraries
import openmeteo_requests  # For interacting with the Open-Meteo API
import requests_cache  # For caching API requests to avoid redundant calls
import pandas as pd  # For data manipulation and analysis
from retry_requests import retry  # For retrying failed API requests

# Set up the Open-Meteo API client with caching and retry mechanisms
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)  # Cache never expires
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)  # Retry up to 5 times with exponential backoff
openmeteo = openmeteo_requests.Client(session=retry_session)  # Initialize the Open-Meteo client

# Define the API endpoint and parameters for historical data
url = "https://archive-api.open-meteo.com/v1/archive"  # Use the archive endpoint for historical data

# Define the parameters for the API request
params = {
    "latitude": 30.0444,  # Latitude of Cairo
    "longitude": 31.2357,  # Longitude of Cairo
    "start_date": (pd.Timestamp.now() - pd.Timedelta(days=365 * 3)).strftime('%Y-%m-%d'),  # Start date: 3 years ago
    "end_date": pd.Timestamp.now().strftime('%Y-%m-%d'),  # End date: today
    "hourly": [
        "temperature_2m",  # Temperature at 2 meters
        "relative_humidity_2m",  # Relative humidity at 2 meters
        "dew_point_2m",  # Dew point at 2 meters
        "apparent_temperature",  # Apparent temperature (feels-like)
        "precipitation",  # Total precipitation
        "rain",  # Rain
        "snowfall",  # Snowfall
        "snow_depth",  # Snow depth
        "weather_code",  # Weather condition code
        "pressure_msl",  # Pressure at mean sea level
        "surface_pressure",  # Surface pressure
        "cloud_cover",  # Total cloud cover
        "cloud_cover_low",  # Low-level cloud cover
        "cloud_cover_mid",  # Mid-level cloud cover
        "cloud_cover_high",  # High-level cloud cover
        "et0_fao_evapotranspiration",  # Reference evapotranspiration
        "vapour_pressure_deficit",  # Vapour pressure deficit
        "wind_speed_10m",  # Wind speed at 10 meters
        "wind_speed_100m",  # Wind speed at 100 meters
        "wind_direction_10m",  # Wind direction at 10 meters
        "wind_direction_100m",  # Wind direction at 100 meters
        "wind_gusts_10m",  # Wind gusts at 10 meters
        "soil_temperature_0_to_7cm",  # Soil temperature at 0-7 cm depth
        "soil_temperature_7_to_28cm",  # Soil temperature at 7-28 cm depth
        "soil_temperature_28_to_100cm",  # Soil temperature at 28-100 cm depth
        "soil_temperature_100_to_255cm",  # Soil temperature at 100-255 cm depth
        "soil_moisture_0_to_7cm",  # Soil moisture at 0-7 cm depth
        "soil_moisture_7_to_28cm",  # Soil moisture at 7-28 cm depth
        "soil_moisture_28_to_100cm",  # Soil moisture at 28-100 cm depth
        "soil_moisture_100_to_255cm"  # Soil moisture at 100-255 cm depth
    ],
    "timezone": "Africa/Cairo"  # Set the timezone to Cairo
}

# Send the API request and fetch the response
responses = openmeteo.weather_api(url, params=params)

# Process the first location (Cairo in this case)
response = responses[0]  # Get the first (and only) response
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")  # Print coordinates
print(f"Elevation: {response.Elevation()} m asl")  # Print elevation
print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")  # Print timezone
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()} s")  # Print UTC offset

# Extract hourly data from the response
hourly = response.Hourly()

# Create a dictionary to store hourly data
hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),  # Start time
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),  # End time
        freq=pd.Timedelta(seconds=hourly.Interval()),  # Frequency of data points
        inclusive="left"  # Include the start time but exclude the end time
    )
}

# Map each variable to its corresponding data
variables = [
    "temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature",
    "precipitation", "rain", "snowfall", "snow_depth", "weather_code", "pressure_msl",
    "surface_pressure", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high",
    "et0_fao_evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_speed_100m",
    "wind_direction_10m", "wind_direction_100m", "wind_gusts_10m", "soil_temperature_0_to_7cm",
    "soil_temperature_7_to_28cm", "soil_temperature_28_to_100cm", "soil_temperature_100_to_255cm",
    "soil_moisture_0_to_7cm", "soil_moisture_7_to_28cm", "soil_moisture_28_to_100cm",
    "soil_moisture_100_to_255cm"
]

# Add each variable's data to the dictionary
for i, var in enumerate(variables):
    hourly_data[var] = hourly.Variables(i).ValuesAsNumpy()

# Convert the dictionary to a Pandas DataFrame
hourly_dataframe = pd.DataFrame(data=hourly_data)

# Save the DataFrame to a CSV file for future use
hourly_dataframe.to_csv('cairo_historical_weather_3_years.csv', index=False)

# Print the DataFrame to verify the data
print(hourly_dataframe)