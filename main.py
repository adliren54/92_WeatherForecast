import requests, json


# for simpler explanation, the weatherCodeTranslator set by range of 10, more detailed definition can be found on https://www.meteomatics.com/en/api/available-parameters/weather-parameter/general-weather-state/

def weatherCodeTranslator(number):
  if number >= 0 or number <= 10:
    return "No precipitation, fog, ice fog (except for 11 and 12), duststorm, sandstorm, drifting or blowing snow"
  elif number >= 20 or number <= 29:
    return "Precipitation, fog, ice fog or thunderstorm at the station during the preceding hour"
  elif number >= 30 or number <= 39:
    return "Duststorm, sandstorm, drifting or blowing snow"
  elif number >= 40 or number <= 49:
    return "Fog or ice fog at the time of observation"
  elif number >= 50 or number <= 59:
    return "Drizzle at the station at the time of observation"
  elif number >= 60 or number <= 69:
    return "Rain at the station at the time of observation"
  elif number >= 70 or number <= 79:
    return "Solid precipitation not in showers at the station at the time of observation"
  elif number >= 80 or number <= 99:
    return "Showery precipitation, or precipitation with current or recent thunderstorm at the station at the time of observation"
    
timezone = "GMT"
latitude = float(input("Latitude > ")) #48.1371
longitude = float(input("Longitude > "))#11.5820

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")


user = result.json()

for i in range(len(user["daily"]["time"])):
  weatherCode = user['daily']['weathercode'][i]
  min = user['daily']['temperature_2m_max'][i]
  max = user['daily']['temperature_2m_min'][i]
  print(user['daily']['time'][i])
  print()
  print(f"{weatherCodeTranslator(weatherCode)}.")
  print(f"Maximum temperature is {max} and minimum temperature is {min}.")
  print()
  print()

#print(f"{weatherCodeTranslator(weatherCode)}.\n Maximum temperature is {max} and minimum temperature is {min}.")

#print(json.dumps(user, indent=2))
