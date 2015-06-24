
import json
import requests
import optparse
from pprint import pprint

def print_weather(w, i):
    print('{} - {}'.format(w[i]['weather'][0]['main'], 
                         w[i]['weather'][0]['description']))
    print('')


def main():
    parser = optparse.OptionParser(usage='%prog -l <location>', version='0.1')
    parser.add_option('-l',
                      dest='location',
                      type='string',
                      help='To insert location')

    (options, args) = parser.parse_args()
    
    # TODO: Download the JSON data from OpenWeatherMap.org's API.
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3'.format(options.location)
    response = requests.get(url)
    response.raise_for_status()
    
    # TODO: Load JSON data into a Python variable.
    weatherData = json.loads(response.text)
    pprint(weatherData)
    print('')
    
    # Print weather descriptions.
    w = weatherData['list']
    print('Current weather in {}:'.format(options.location))
    
    for i, item in enumerate(w):
        if i == 0:
            print_weather(w, i)
        if i == 1:
            print('Tomorrow:')
            print_weather(w, i)
        if i == 2:
            print('Day after tomorrow:')
            print_weather(w, i)
    
if __name__ == '__main__':
    main()