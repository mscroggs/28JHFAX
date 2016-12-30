import threading
from time import sleep, time
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import pickle
import json
import config
import file_handler

# Update interval for weather data in seconds
interval = 1800

f_name = config.weather_f_name

def write_weather_data(file_location):
  try:
    try:
        with open("uk_coordinate_ids.txt") as f:
            ordered_ids = [line.rstrip('\n') for line in f]
    except:
        with open("/home/pi/ceefax/uk_coordinate_ids.txt") as f:
            ordered_ids = [line.rstrip('\n') for line in f]

    temps = [99 for i in range(len(ordered_ids))]
    # Loop over possible values instead of calling several times
    max_value = len(temps) / 100
    i = 0
    for j in range(max_value + 1):
        if j < max_value:
            url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[100 * j:100 * (j + 1)]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        else:
            url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[100 * j:]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)
        for city in data['list']:
            temps[i] = float(city['main']['temp'])
            i+=1

    # Save temp list with pickle
    file_handler.f_write_pickle(f_name, temps)
  except:
    pass

class weatherThread(threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)
        self.update = threading.Event()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            write_weather_data(f_name)
            self.update.wait(interval)

    def stop(self):
        self.stop_event.set()
        self.update.set()
