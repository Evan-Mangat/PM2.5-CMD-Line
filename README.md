# PM2.5-CMD-Line

This Python command-line program calculates the average PM2.5 (Particulate Matter 2.5) air pollutant values over a specified period of time for stations within a given map bound. It utilizes the AQICN (Air Quality Index) API to retrieve real-time PM2.5 data from different geographical locations and computes the average value.

Features
* Retrieves PM2.5 data for stations within a specified map bound.
* Supports customization of sampling period and rate.
* Calculates and displays individual sampled PM2.5 values.
* Outputs the overall average PM2.5 value for all stations.
  
Installation
* Ensure you have Python 3.x installed on your system.
* Set up a virtual environment (if nessecary) using:
  python -m venv venv
  source venv/bin/activate
* Install the required packages using the following command:
  pip install -r requirements.txt

Usage
Run the script with the following command-line arguments:
python script_name.py latitude1 longitude1 latitude2 longitude2 --apikey YOUR_ACTUAL_API_KEY

optionally, one can adjust the period and rate within the command line by typing something that follows this format:
python script_name.py latitude1 longitude1 latitude2 longitude2 --period INSERT_PERIOD_NUM --rate INSERT_RATE_NUM --apikey YOUR_ACTUAL_API_KEY

where:
* latitude1, longitude1: Latitude and longitude of the first corner of the map bound.
* latitude2, longitude2: Latitude and longitude of the second corner of the map bound.
* --period: Sampling period in minutes (default = 5).
* --rate: Sampling rate in samples/minute (default = 1).
* --apikey: API key for AQICN API (required).

Example
To calculate the average PM2.5 values for stations within a map bound, use the following example (assuming one wants the default values for period at 5 minutes and rate at 1 sample:
python script_name.py 49.28234795142009 -123.12047325624289 40.70726141581518 -74.0208910538649 --apikey YOUR_ACTUAL_API_KEY

Notes
* The script utilizes the requests library to interact with the AQICN API.
* The AQICN API key is required for authentication; make sure to replace YOUR_ACTUAL_API_KEY with your API key.
* The calculated average PM2.5 values are based on the specified sampling period and rate.

Acknowledgements
This script was developed by Evan Mangat as a demonstration of using the AQICN API to calculate average PM2.5 values within a map bound.
