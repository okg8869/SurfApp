import json
import requests
import time
import datetime
from datetime import datetime
from twilio.rest import Client
import os
import config

# Documentation can be found here: http://magicseaweed.com/developer/forecast-api
# Here's an example URL showing the forecast for The Wall: http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=369

key = surfConfig.key
secret = surfConfig.secret

theWall = 'spot_id=369'
pointJudith = 'spot_id=376'

# judithResponse = requests.get('http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=376&fields=localTimestamp,swell.absMinBreakingHeight,swell.absMaxBreakingHeight,swell.primary,swell.secondary,wind.speed,wind.compassDirection,condition.temperature')
# theWallResponse = requests.get('http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=369&fields=localTimestamp,swell.absMinBreakingHeight,swell.absMaxBreakingHeight,swell.primary,swell.secondary,wind.speed,wind.compassDirection,condition.temperature')

# judithForecast = json.loads(judithResponse.text)
# theWallForecast = json.loads(theWallResponse.text)

					# Sample Response:
					# 	{
					# 	'localTimestamp': 1534906800, 
					# 	'swell': 
					# 		{'minBreakingHeight': 2, 'maxBreakingHeight': 3}, 
					# 	'wind': 
					#		{'speed': 4, 'compassDirection': 'ESE'}, 
					# 	'condition': 
					#		{'temperature': 63}
					#	}


judith = '[{"localTimestamp":1535587200,"swell":{"absMinBreakingHeight":1.34,"absMaxBreakingHeight":2.09},"wind":{"speed":8,"compassDirection":"SW"},"condition":{"temperature":76}},{"localTimestamp":1535598000,"swell":{"absMinBreakingHeight":1.34,"absMaxBreakingHeight":2.09},"wind":{"speed":6,"compassDirection":"WSW"},"condition":{"temperature":76}},{"localTimestamp":1535608800,"swell":{"absMinBreakingHeight":1.32,"absMaxBreakingHeight":2.06},"wind":{"speed":8,"compassDirection":"W"},"condition":{"temperature":80}},{"localTimestamp":1535619600,"swell":{"absMinBreakingHeight":1.3,"absMaxBreakingHeight":2.04},"wind":{"speed":6,"compassDirection":"W"},"condition":{"temperature":88}},{"localTimestamp":1535630400,"swell":{"absMinBreakingHeight":1.22,"absMaxBreakingHeight":1.91},"wind":{"speed":5,"compassDirection":"WNW"},"condition":{"temperature":90}},{"localTimestamp":1535641200,"swell":{"absMinBreakingHeight":1.11,"absMaxBreakingHeight":1.74},"wind":{"speed":4,"compassDirection":"ENE"},"condition":{"temperature":84}},{"localTimestamp":1535652000,"swell":{"absMinBreakingHeight":1.01,"absMaxBreakingHeight":1.58},"wind":{"speed":8,"compassDirection":"ENE"},"condition":{"temperature":74}},{"localTimestamp":1535662800,"swell":{"absMinBreakingHeight":0.91,"absMaxBreakingHeight":1.42},"wind":{"speed":7,"compassDirection":"NE"},"condition":{"temperature":70}},{"localTimestamp":1535673600,"swell":{"absMinBreakingHeight":0.78,"absMaxBreakingHeight":1.22},"wind":{"speed":8,"compassDirection":"NE"},"condition":{"temperature":69}},{"localTimestamp":1535684400,"swell":{"absMinBreakingHeight":0.78,"absMaxBreakingHeight":1.21},"wind":{"speed":10,"compassDirection":"ENE"},"condition":{"temperature":70}},{"localTimestamp":1535695200,"swell":{"absMinBreakingHeight":0.85,"absMaxBreakingHeight":1.33},"wind":{"speed":12,"compassDirection":"ENE"},"condition":{"temperature":70}},{"localTimestamp":1535706000,"swell":{"absMinBreakingHeight":1.18,"absMaxBreakingHeight":1.84},"wind":{"speed":11,"compassDirection":"ENE"},"condition":{"temperature":74}},{"localTimestamp":1535716800,"swell":{"absMinBreakingHeight":1.27,"absMaxBreakingHeight":1.98},"wind":{"speed":12,"compassDirection":"E"},"condition":{"temperature":79}},{"localTimestamp":1535727600,"swell":{"absMinBreakingHeight":1.4,"absMaxBreakingHeight":2.19},"wind":{"speed":11,"compassDirection":"E"},"condition":{"temperature":75}},{"localTimestamp":1535738400,"swell":{"absMinBreakingHeight":1.37,"absMaxBreakingHeight":2.13},"wind":{"speed":9,"compassDirection":"E"},"condition":{"temperature":69}},{"localTimestamp":1535749200,"swell":{"absMinBreakingHeight":1.26,"absMaxBreakingHeight":1.97},"wind":{"speed":9,"compassDirection":"ENE"},"condition":{"temperature":67}},{"localTimestamp":1535760000,"swell":{"absMinBreakingHeight":1.13,"absMaxBreakingHeight":1.77},"wind":{"speed":8,"compassDirection":"ENE"},"condition":{"temperature":67}},{"localTimestamp":1535770800,"swell":{"absMinBreakingHeight":1.04,"absMaxBreakingHeight":1.62},"wind":{"speed":8,"compassDirection":"ENE"},"condition":{"temperature":66}},{"localTimestamp":1535781600,"swell":{"absMinBreakingHeight":1.02,"absMaxBreakingHeight":1.6},"wind":{"speed":8,"compassDirection":"ENE"},"condition":{"temperature":68}},{"localTimestamp":1535792400,"swell":{"absMinBreakingHeight":0.96,"absMaxBreakingHeight":1.5},"wind":{"speed":7,"compassDirection":"E"},"condition":{"temperature":76}},{"localTimestamp":1535803200,"swell":{"absMinBreakingHeight":0.95,"absMaxBreakingHeight":1.48},"wind":{"speed":9,"compassDirection":"SE"},"condition":{"temperature":79}},{"localTimestamp":1535814000,"swell":{"absMinBreakingHeight":0.95,"absMaxBreakingHeight":1.49},"wind":{"speed":8,"compassDirection":"SE"},"condition":{"temperature":76}},{"localTimestamp":1535824800,"swell":{"absMinBreakingHeight":0.86,"absMaxBreakingHeight":1.35},"wind":{"speed":6,"compassDirection":"SE"},"condition":{"temperature":68}},{"localTimestamp":1535835600,"swell":{"absMinBreakingHeight":0.87,"absMaxBreakingHeight":1.36},"wind":{"speed":4,"compassDirection":"SE"},"condition":{"temperature":67}},{"localTimestamp":1535846400,"swell":{"absMinBreakingHeight":0.96,"absMaxBreakingHeight":1.5},"wind":{"speed":2,"compassDirection":"ESE"},"condition":{"temperature":67}},{"localTimestamp":1535857200,"swell":{"absMinBreakingHeight":1.01,"absMaxBreakingHeight":1.57},"wind":{"speed":3,"compassDirection":"E"},"condition":{"temperature":69}},{"localTimestamp":1535868000,"swell":{"absMinBreakingHeight":1.04,"absMaxBreakingHeight":1.62},"wind":{"speed":4,"compassDirection":"ESE"},"condition":{"temperature":70}},{"localTimestamp":1535878800,"swell":{"absMinBreakingHeight":1.3,"absMaxBreakingHeight":2.03},"wind":{"speed":8,"compassDirection":"SSE"},"condition":{"temperature":78}},{"localTimestamp":1535889600,"swell":{"absMinBreakingHeight":0.99,"absMaxBreakingHeight":1.54},"wind":{"speed":10,"compassDirection":"S"},"condition":{"temperature":80}},{"localTimestamp":1535900400,"swell":{"absMinBreakingHeight":0.94,"absMaxBreakingHeight":1.47},"wind":{"speed":10,"compassDirection":"S"},"condition":{"temperature":79}},{"localTimestamp":1535911200,"swell":{"absMinBreakingHeight":0.92,"absMaxBreakingHeight":1.44},"wind":{"speed":7,"compassDirection":"S"},"condition":{"temperature":73}},{"localTimestamp":1535922000,"swell":{"absMinBreakingHeight":1.06,"absMaxBreakingHeight":1.65},"wind":{"speed":7,"compassDirection":"SSW"},"condition":{"temperature":73}},{"localTimestamp":1535932800,"swell":{"absMinBreakingHeight":1.05,"absMaxBreakingHeight":1.64},"wind":{"speed":6,"compassDirection":"SW"},"condition":{"temperature":72}},{"localTimestamp":1535943600,"swell":{"absMinBreakingHeight":1.07,"absMaxBreakingHeight":1.67},"wind":{"speed":6,"compassDirection":"SW"},"condition":{"temperature":72}},{"localTimestamp":1535954400,"swell":{"absMinBreakingHeight":1.07,"absMaxBreakingHeight":1.67},"wind":{"speed":7,"compassDirection":"SW"},"condition":{"temperature":76}},{"localTimestamp":1535965200,"swell":{"absMinBreakingHeight":1.07,"absMaxBreakingHeight":1.67},"wind":{"speed":8,"compassDirection":"SW"},"condition":{"temperature":84}},{"localTimestamp":1535976000,"swell":{"absMinBreakingHeight":1.07,"absMaxBreakingHeight":1.67},"wind":{"speed":11,"compassDirection":"SW"},"condition":{"temperature":87}},{"localTimestamp":1535986800,"swell":{"absMinBreakingHeight":1.02,"absMaxBreakingHeight":1.6},"wind":{"speed":11,"compassDirection":"SW"},"condition":{"temperature":84}},{"localTimestamp":1535997600,"swell":{"absMinBreakingHeight":1,"absMaxBreakingHeight":1.56},"wind":{"speed":8,"compassDirection":"SW"},"condition":{"temperature":73}},{"localTimestamp":1536008400,"swell":{"absMinBreakingHeight":1,"absMaxBreakingHeight":1.57},"wind":{"speed":7,"compassDirection":"WSW"},"condition":{"temperature":73}}]'
wall = '[{"localTimestamp":1535587200,"swell":{"absMinBreakingHeight":0.6,"absMaxBreakingHeight":0.95},"wind":{"speed":5,"compassDirection":"WSW"},"condition":{"temperature":75}},{"localTimestamp":1535598000,"swell":{"absMinBreakingHeight":0.58,"absMaxBreakingHeight":0.91},"wind":{"speed":4,"compassDirection":"W"},"condition":{"temperature":73}},{"localTimestamp":1535608800,"swell":{"absMinBreakingHeight":0.58,"absMaxBreakingHeight":0.91},"wind":{"speed":6,"compassDirection":"WNW"},"condition":{"temperature":77}},{"localTimestamp":1535619600,"swell":{"absMinBreakingHeight":0.52,"absMaxBreakingHeight":0.82},"wind":{"speed":6,"compassDirection":"N"},"condition":{"temperature":79}},{"localTimestamp":1535630400,"swell":{"absMinBreakingHeight":0.45,"absMaxBreakingHeight":0.7},"wind":{"speed":4,"compassDirection":"ENE"},"condition":{"temperature":86}},{"localTimestamp":1535641200,"swell":{"absMinBreakingHeight":0.7,"absMaxBreakingHeight":1.09},"wind":{"speed":5,"compassDirection":"E"},"condition":{"temperature":78}},{"localTimestamp":1535652000,"swell":{"absMinBreakingHeight":0.71,"absMaxBreakingHeight":1.11},"wind":{"speed":2,"compassDirection":"E"},"condition":{"temperature":69}},{"localTimestamp":1535662800,"swell":{"absMinBreakingHeight":0.68,"absMaxBreakingHeight":1.07},"wind":{"speed":4,"compassDirection":"NNE"},"condition":{"temperature":65}},{"localTimestamp":1535673600,"swell":{"absMinBreakingHeight":1.06,"absMaxBreakingHeight":1.66},"wind":{"speed":5,"compassDirection":"NNE"},"condition":{"temperature":61}},{"localTimestamp":1535684400,"swell":{"absMinBreakingHeight":1.59,"absMaxBreakingHeight":2.48},"wind":{"speed":6,"compassDirection":"NE"},"condition":{"temperature":62}},{"localTimestamp":1535695200,"swell":{"absMinBreakingHeight":1.87,"absMaxBreakingHeight":2.92},"wind":{"speed":8,"compassDirection":"NE"},"condition":{"temperature":64}},{"localTimestamp":1535706000,"swell":{"absMinBreakingHeight":1.98,"absMaxBreakingHeight":3.1},"wind":{"speed":9,"compassDirection":"ENE"},"condition":{"temperature":71}},{"localTimestamp":1535716800,"swell":{"absMinBreakingHeight":1.93,"absMaxBreakingHeight":3.02},"wind":{"speed":9,"compassDirection":"E"},"condition":{"temperature":73}},{"localTimestamp":1535727600,"swell":{"absMinBreakingHeight":1.68,"absMaxBreakingHeight":2.62},"wind":{"speed":7,"compassDirection":"E"},"condition":{"temperature":69}},{"localTimestamp":1535738400,"swell":{"absMinBreakingHeight":1.4,"absMaxBreakingHeight":2.18},"wind":{"speed":4,"compassDirection":"E"},"condition":{"temperature":63}},{"localTimestamp":1535749200,"swell":{"absMinBreakingHeight":1.19,"absMaxBreakingHeight":1.85},"wind":{"speed":4,"compassDirection":"E"},"condition":{"temperature":64}},{"localTimestamp":1535760000,"swell":{"absMinBreakingHeight":0.9,"absMaxBreakingHeight":1.4},"wind":{"speed":3,"compassDirection":"NE"},"condition":{"temperature":59}},{"localTimestamp":1535770800,"swell":{"absMinBreakingHeight":1.35,"absMaxBreakingHeight":2.1},"wind":{"speed":4,"compassDirection":"NE"},"condition":{"temperature":58}},{"localTimestamp":1535781600,"swell":{"absMinBreakingHeight":1.31,"absMaxBreakingHeight":2.05},"wind":{"speed":5,"compassDirection":"NE"},"condition":{"temperature":64}},{"localTimestamp":1535792400,"swell":{"absMinBreakingHeight":1.25,"absMaxBreakingHeight":1.95},"wind":{"speed":6,"compassDirection":"E"},"condition":{"temperature":70}},{"localTimestamp":1535803200,"swell":{"absMinBreakingHeight":1.17,"absMaxBreakingHeight":1.83},"wind":{"speed":8,"compassDirection":"ESE"},"condition":{"temperature":75}},{"localTimestamp":1535814000,"swell":{"absMinBreakingHeight":1.1,"absMaxBreakingHeight":1.71},"wind":{"speed":7,"compassDirection":"SE"},"condition":{"temperature":73}},{"localTimestamp":1535824800,"swell":{"absMinBreakingHeight":1.39,"absMaxBreakingHeight":2.17},"wind":{"speed":5,"compassDirection":"ESE"},"condition":{"temperature":63}},{"localTimestamp":1535835600,"swell":{"absMinBreakingHeight":1.46,"absMaxBreakingHeight":2.29},"wind":{"speed":3,"compassDirection":"SSE"},"condition":{"temperature":62}},{"localTimestamp":1535846400,"swell":{"absMinBreakingHeight":1.74,"absMaxBreakingHeight":2.72},"wind":{"speed":3,"compassDirection":"SSW"},"condition":{"temperature":62}},{"localTimestamp":1535857200,"swell":{"absMinBreakingHeight":1.79,"absMaxBreakingHeight":2.79},"wind":{"speed":3,"compassDirection":"SW"},"condition":{"temperature":61}},{"localTimestamp":1535868000,"swell":{"absMinBreakingHeight":1.63,"absMaxBreakingHeight":2.55},"wind":{"speed":3,"compassDirection":"S"},"condition":{"temperature":66}},{"localTimestamp":1535878800,"swell":{"absMinBreakingHeight":1.49,"absMaxBreakingHeight":2.33},"wind":{"speed":6,"compassDirection":"SSW"},"condition":{"temperature":80}},{"localTimestamp":1535889600,"swell":{"absMinBreakingHeight":1.36,"absMaxBreakingHeight":2.13},"wind":{"speed":7,"compassDirection":"S"},"condition":{"temperature":82}},{"localTimestamp":1535900400,"swell":{"absMinBreakingHeight":1.29,"absMaxBreakingHeight":2.02},"wind":{"speed":8,"compassDirection":"SSE"},"condition":{"temperature":82}},{"localTimestamp":1535911200,"swell":{"absMinBreakingHeight":1.26,"absMaxBreakingHeight":1.97},"wind":{"speed":7,"compassDirection":"S"},"condition":{"temperature":76}},{"localTimestamp":1535922000,"swell":{"absMinBreakingHeight":1.3,"absMaxBreakingHeight":2.04},"wind":{"speed":7,"compassDirection":"SSW"},"condition":{"temperature":73}},{"localTimestamp":1535932800,"swell":{"absMinBreakingHeight":1.33,"absMaxBreakingHeight":2.07},"wind":{"speed":6,"compassDirection":"SSW"},"condition":{"temperature":71}},{"localTimestamp":1535943600,"swell":{"absMinBreakingHeight":1.31,"absMaxBreakingHeight":2.04},"wind":{"speed":5,"compassDirection":"SW"},"condition":{"temperature":70}},{"localTimestamp":1535954400,"swell":{"absMinBreakingHeight":1.21,"absMaxBreakingHeight":1.88},"wind":{"speed":6,"compassDirection":"SW"},"condition":{"temperature":73}},{"localTimestamp":1535965200,"swell":{"absMinBreakingHeight":1.08,"absMaxBreakingHeight":1.68},"wind":{"speed":6,"compassDirection":"W"},"condition":{"temperature":87}},{"localTimestamp":1535976000,"swell":{"absMinBreakingHeight":1,"absMaxBreakingHeight":1.57},"wind":{"speed":6,"compassDirection":"WSW"},"condition":{"temperature":93}},{"localTimestamp":1535986800,"swell":{"absMinBreakingHeight":0.93,"absMaxBreakingHeight":1.46},"wind":{"speed":3,"compassDirection":"WSW"},"condition":{"temperature":91}},{"localTimestamp":1535997600,"swell":{"absMinBreakingHeight":1,"absMaxBreakingHeight":1.56},"wind":{"speed":3,"compassDirection":"NW"},"condition":{"temperature":81}},{"localTimestamp":1536008400,"swell":{"absMinBreakingHeight":0.98,"absMaxBreakingHeight":1.53},"wind":{"speed":4,"compassDirection":"NW"},"condition":{"temperature":75}}]'

judithForecast = json.loads(judith)
theWallForecast = json.loads(wall)

todaysDate = datetime.now()
dateUnix = time.mktime(todaysDate.timetuple())
# Grabbing today's date and Unix based date (still in GMT for now because same day is all I need)

# Print out a list of all Local Time Stamps in regular date format
times = []
for element in judithForecast:
	times.append(element['localTimestamp'])
for timeStamp in times:
	date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamp))

judithHits = []
def printJudithForecast():
	for e in judithForecast:
		minHeight = e['swell']['absMinBreakingHeight']
		maxHeight = e['swell']['absMaxBreakingHeight']
		if minHeight >= 2 and todayUTC < e['localTimestamp']:
			judithHits.append(
				{
					"waveMax" : maxHeight,
					"waveMin": minHeight,
					"temp": e['condition']['temperature'],
					"time": time.strftime('%Y-%m-%d %l:%M %p', time.localtime(e['localTimestamp']))
				}
			)
			

wallHits = []
def printTheWallForecast():
	for e in theWallForecast:
		minHeight = e['swell']['absMinBreakingHeight']
		maxHeight = e['swell']['absMaxBreakingHeight']
		if minHeight >= 2 and todayUTC < e['localTimestamp']:
			wallHits.append(
				{
					"waveMax" : maxHeight,
					"waveMin": minHeight,
					"temp": e['condition']['temperature'],
					"time": time.strftime('%Y-%m-%d %l:%M %p', time.localtime(e['localTimestamp']))
				}
			)	



printJudithForecast()
printTheWallForecast()

print(todaysDate)
print(dateUnix)

if len(wallHits) == 0:
	print ("no wall surf")
if len(judithHits) == 0:
	print ("no judith surf")



#Twilio Code below for texting

# Your Account SID from twilio.com/console
account_sid = twilioConfig.accountSid
# Your Auth Token from twilio.com/console
auth_token  = twilioConfig.authToken

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18434226842", 
    from_="+17075129228",
    body="Hello from Python!")

print(message.sid)