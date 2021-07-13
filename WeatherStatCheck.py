from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

#You have to write your API from openweathermap.org

owm = OWM('25dfe919dbcf7ebf8e8e26dbc08e7c96')
mgr = owm.weather_manager()

place = input("Your city ")

observation = mgr.weather_at_place(place)
w = observation.weather

halfTemp = round(w.temperature('celsius')["temp"]) + 1

print(w.detailed_status + " " + str(round(w.temperature('celsius')["temp"]))
	 + "-" + str(halfTemp) + "C*" + " " + str(w.wind()["speed"]) + " speed of wind")