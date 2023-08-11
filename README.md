# PM2.5-CMD-Line

1. Introduction

This Python script is designed to calculate the average PM2.5 (Particulate Matter 2.5) air pollutant values over a specified period of time for stations within a given map bound. It utilizes the AQICN (Air Quality Index) API to retrieve real-time PM2.5 data from different geographical locations and computes the average value.

2. Script Structure

The script is structured into several functions to perform specific tasks:

•	 `get_pm25_data(latitude, longitude, api_key)`: This function takes latitude, longitude, and an API key as parameters and makes a request to the AQICN API to retrieve PM2.5 data for the specified geographical coordinates. It returns the PM2.5 value.

•	`calculate_average(pm25_values)`: This function takes a list of PM2.5 values as input and calculates the average value.

•	`main()`: The main function handles command-line arguments, coordinates, and API key input. It orchestrates the data retrieval and calculation processes.

3. Command-Line Arguments

The script uses the `argparse` library to handle command-line arguments. The following arguments are supported:

•	`latitude1`, `longitude1`, `latitude2`, `longitude2`: Coordinates representing the two pairs of latitudes and longitudes that define the map bound.

•	 `--period`: Sampling period in minutes. Default is set to 5 minutes.

•	 `--rate`: Sampling rate in samples/minute. Default is set to 1 sample/minute.

•	`--apikey`: The API key required to authenticate requests to the AQICN API.

4. Coordinate Sorting

The script sorts the latitude and longitude values to ensure that the correct map bound is defined, regardless of input order.

5. Data Retrieval and Calculation

•	 The total number of samples is calculated as the product of the sampling period and the sampling rate.

•	The script iterates over the latitude and longitude combinations within the map bound.

•	For each combination, it makes repeated API requests to retrieve PM2.5 data, following the specified sampling rate.

•	Retrieved PM2.5 values are appended to a list.

•	 The calculated average PM2.5 value over the specified time period is computed using the `calculate_average` function.

6. Output

•	The script prints the individual PM2.5 sampled values for each station.

•	It prints the overall average PM2.5 value for all stations over the specified time period.

7. Usage

To run the script, provide the required command-line arguments, including coordinates and the API key:
Assuming bash shell:
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python main.py latitude1 longitude1 latitude2 longitude2 --apikey INSERT_API_KEY_HERE

8. Conclusion

This Python script offers a flexible way to retrieve and analyze PM2.5 data within a specific map bound using the AQICN API. It showcases how to use command-line arguments, API requests, and data manipulation to calculate average pollutant values for given locations over a defined time interval.
