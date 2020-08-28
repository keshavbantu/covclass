#this module pushes and updates dates to the grabber.py file so it can grab the right pdf file for data processing. 
#this program is also meant to get triggered at a certain time
#instead of writing a trigger logic, ill be using a cronjob on AWS
 
import datetime

global Pass
def refresh():
    today=datetime.datetime.now()
    if (today.month<10 and today.day<10):
        Pass="0"+str(today.day-1)+"-0"+str(today.month)+"-"+str(today.year)
    elif today.day<10:
        Pass="0"+str(today.day-1)+"-"+str(today.month)+"-"+str(today.year)
    elif today.month<10:
        Pass=str(today.day-1)+"-0"+str(today.month)+"-"+str(today.year)
    else:
        Pass=str(today.day-1)+"-"+str(today.month)+"-"+str(today.year)
    return Pass   

newDate=refresh()

#today.day-1 for program run in all times except night
#file uploaded at night to karnataka website
#today.day for cron job running at night of every day