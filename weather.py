import requests

city = "4297983"
api_key = "11bc9641b84fcb54bd4f64e66924816e"
units = "Imperial"
unit_key = "F"

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
