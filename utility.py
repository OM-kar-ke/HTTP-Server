import datetime
from datetime import timedelta


#To get the value for Date Header Field
def get_date_and_time(today=True) :
    
    months = {'01':"Jan", '02':"Feb" , '03':"Mar", '04':"Apr", '5':"May", '06':"Jun", '07':"Jul", '08':"Aug", '09':"Sep",  '10':"Oct",  '11':"Nov",  '12':"Dec"}
    
    week_days = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    
    current_time = datetime.datetime.now() 
    
    if (today == False):
        current_time = current_time + timedelta(days=1)
    
    weekday = datetime.datetime.today().weekday()
    
    if (today == False):
        weekday += 1
        weekday = weekday % 7
    weekday = week_days[weekday].encode()
    
    
    day = current_time.day
    day=str(day).encode()
    month = current_time.month
    # print(month)
    month = months[str(month)].encode()
    year = str(current_time.year).encode()
        
        
    hour = current_time.hour
    if (hour <10):
        hour = "0" + str(hour)
    else :
        hour = str(hour)
    hour = hour.encode()
    
    minutes = current_time.minute
    if (minutes <10):
        minutes = "0" + str(minutes)
    else :
        minutes = str(minutes)
    minutes = minutes.encode()
    
    seconds = current_time.second
    if (seconds <10):
        seconds = "0" + str(seconds)
    else :
        seconds = str(seconds)
    seconds = seconds.encode()
    
       
    return b"".join([weekday, b", ", day, b" ", month, b" ", year, b" ", hour, b":", minutes, b":", seconds, b" ", b"GMT"])


#To get the value for Last-Modified Header Field
def last_modified(path) :
    
	path = path.strip("/")
	fileStatsObj = os.stat (path)
	modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
	l = modificationTime.split(" ")
	msg = l[0] + ", " + l[2] + " " + l[1] + " " + l[4] + " "+ l[3] + " GMT"
 
	return msg
