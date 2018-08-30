import json
import requests
import time
import datetime

# Key:  5e44fc29c13dfab6ac38068d3243692c
# Secret: 647eec5fe66142ef62122b7628b054d0
# Documentation can be found here: http://magicseaweed.com/developer/forecast-api
# Here's an example URL showing the forecast for The Wall: http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=369

key = '5e44fc29c13dfab6ac38068d3243692c'
secret = '647eec5fe66142ef62122b7628b054d0'

theWall = 'spot_id=369'
pointJudith = 'spot_id=376'

judithResponse = requests.get('http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=376&fields=localTimestamp,swell.absMinBreakingHeight,swell.absMaxBreakingHeight,swell.primary,swell.secondary,wind.speed,wind.compassDirection,condition.temperature')
theWallResponse = requests.get('http://magicseaweed.com/api/5e44fc29c13dfab6ac38068d3243692c/forecast/?spot_id=369&fields=localTimestamp,swell.absMinBreakingHeight,swell.absMaxBreakingHeight,swell.primary,swell.secondary,wind.speed,wind.compassDirection,condition.temperature')

judithForecast = json.loads(judithResponse.text)
theWallForecast = json.loads(theWallResponse.text)

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

todaysDate = datetime.date.today()
dateUnix = todaysDate.total_seconds()
print(todaysDate)
print(dateUnix)

# Print out a list of all Local Time Stamps in regular date format
times = []
for element in judithForecast:
	times.append(element['localTimestamp'])
for timeStamp in times:
	date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamp))


def printJudithForecast():
	for e in judithForecast:
		locTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(e['localTimestamp']))
		minHeight = e['swell']['absMinBreakingHeight']
		maxHeight = e['swell']['absMaxBreakingHeight']
		if minHeight >= 2:
			print("it's time to go! the min is {} and the max is {} on {}".format(minHeight, maxHeight, locTime))
		else:
			print("Man we ain't found shit. (point)")


def printTheWallForecast():
	for e in theWallForecast:
		locTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(e['localTimestamp']))
		minHeight = e['swell']['absMinBreakingHeight']
		maxHeight = e['swell']['absMaxBreakingHeight']
		if minHeight >= 2:
			print("it's time to go! the min is {} and the max is {} on {}".format(minHeight, maxHeight, locTime))
		else:
			print("Man we ain't found shit. (wall)")



printJudithForecast()
printTheWallForecast()


