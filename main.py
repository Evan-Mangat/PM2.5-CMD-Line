import requests
import argparse
import time

def get_station_data(map_bounds, api_key):
    url = f'https://api.waqi.info/map/bounds/?latlng={map_bounds}&token={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['data']

def calculate_average(pm25_values):
    return sum(pm25_values) / len(pm25_values)

def main():
    parser = argparse.ArgumentParser(description='Calculate average PM2.5 over n minutes for stations within map bounds')
    parser.add_argument('latitude1', type=float, help='Latitude of the first corner')
    parser.add_argument('longitude1', type=float, help='Longitude of the first corner')
    parser.add_argument('latitude2', type=float, help='Latitude of the second corner')
    parser.add_argument('longitude2', type=float, help='Longitude of the second corner')
    parser.add_argument('--period', type=int, default=5, help='Sampling period in minutes (default = 5)')
    parser.add_argument('--rate', type=int, default=1, help='Sampling rate in samples/minute (default = 1)')
    parser.add_argument('--apikey', required=True, help='API key for AQICN API')

    args = parser.parse_args()

    map_bounds = f'{args.latitude1},{args.longitude1},{args.latitude2},{args.longitude2}'
    api_key = args.apikey

    total_samples = args.period * args.rate
    pm25_values = []

    station_data = get_station_data(map_bounds, api_key)

    for station in station_data:
        for _ in range(total_samples):
            pm25 = int(station['aqi'])
            pm25_values.append(pm25)
            time.sleep(60 / args.rate)

    avg_pm25 = calculate_average(pm25_values)

    print("PM2.5 sampled values:")
    for pm25 in pm25_values:
        print(pm25)

    print(f"Overall PM2.5 average over {args.period} minutes: {avg_pm25}")

if __name__ == '__main__':
    main()
