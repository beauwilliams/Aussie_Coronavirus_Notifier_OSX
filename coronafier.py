import sys
print(sys.executable)
import datetime #for reading present date
import time
import requests #for retreiving coronavirus data from web
# from pyler import EulerProblem
from plyer import notification


# let there is no data initially
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

#if we fetched data
if (covidData != None):
    #converting data into JSON format
    data = covidData.json()['Success']

    #repeating the loop for multiple times
    while(True):
        notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            #the body of the notification
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = "Paomedia-Small-N-Flat-Bell.ico",
            # the notification stays for 50sec
            timeout  = 50
        )
        #HARD CODING A 30 SECOND RATE LIMIT SO WE DONT MAKE THE API SAD :)
        time.sleep(30)
