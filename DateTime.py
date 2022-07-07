import datetime
import time

def Date():
    date = datetime.datetime.now()
    current_date = date.strftime("%d-%b-%y")
    return str(current_date)

def Time():
    t = time.localtime()
    current_time = time.strftime("%H:%M %p", t)
    return str(current_time)
