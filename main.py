import requests
import argparse
import time

def get_pm25_data(latitude, longitude, api_key):
    url = f'https://api.waqi.info/feed/geo:{latitude};{longitude}/?token={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['data']['aqi']

def calculate_average(pm25_values):
    return sum(pm25_values) / len(pm25_values)

def main():
    parser = argparse.ArgumentParser(description='Calculate average PM2.5 over n minutes for specified map bounds')
    parser.add_argument('latitude1', type=float, help='Latitude of the first corner')
    parser.add_argument('longitude1', type=float, help='Longitude of the first corner')
    parser.add_argument('latitude2', type=float, help='Latitude of the second corner')
    parser.add_argument('longitude2', type=float, help='Longitude of the second corner')
    parser.add_argument('--period', type=int, default=5, help='Sampling period in minutes (default = 5)')
    parser.add_argument('--rate', type=int, default=1, help='Sampling rate in samples/minute (default = 1)')
    parser.add_argument('--apikey', required=True, help='API key for AQICN API')

    args = parser.parse_args()

    latitudes = [args.latitude1, args.latitude2]
    longitudes = [args.longitude1, args.longitude2]

    latitudes.sort()
    longitudes.sort()

    api_key = args.apikey

    total_samples = args.period * args.rate
    pm25_values = []

    for lat in latitudes:
        for lon in longitudes:
            for _ in range(total_samples):
                pm25 = get_pm25_data(lat, lon, api_key)
                pm25_values.append(pm25)
                time.sleep(60 / args.rate)

    avg_pm25 = calculate_average(pm25_values)

    print("PM2.5 sampled values:")
    for pm25 in pm25_values:
        print(pm25)

    print(f"Overall PM2.5 average over {args.period} minutes: {avg_pm25}")

if __name__ == '__main__':
    main()
