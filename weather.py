import requests
with open('weather_api', 'r') as file:
	passwd = file.read().replace('\n', '')

city = "4297983"
units = "Imperial"
unit_key = "F"
api_key = str(passwd)

req = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}".format(city, api_key, units))

if req.status_code == 200:
	current = req.json()["weather"][0]["description"].capitalize()
	category = req.json()["weather"][0]["main"].capitalize()
	dayornight = req.json()["weather"][0]["icon"].capitalize()
	temp = int(float(req.json()["main"]["temp"]))
else: 
 	print("Err:weath")

if category == "Thunderstorm":
	icon = ""
elif category == "Drizzle":
	icon = ""
elif category == "Rain":
	icon = ""
elif category == "Snow":
	icon = ""
elif category == "Clear":
	if dayornight[-1] == "d":
		icon = ""
	else:
		icon = ""
elif category == "Clouds":
	icon = ""
else: 
	icon = ""

 
print("{} {}°F".format(icon, temp))

# print("     ") 

# material
# 
#
