import os
import datetime
from datetime import timedelta
import time
import stat
import string    
import random # To generate random alphanumeric string (for cookie)
import json
import gzip
import zlib

#This function appends new header and its value to already existing headers
def append_additional_header(headers, additional_header_name, additional_header_value):
    
    headers = headers.decode()
    headers += "%s: %s\r\n" % (additional_header_name, additional_header_value)
    return headers.encode()



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


#To parse Range header. And storing the list of ranges i.e.[start, end] in a list.
def parse_range(value):
    
	value=value.split('=',1)
	value = value[1]
	value=value.split(',')

	res=[]
	#3 cases are possible here st-end , st- , -end
	for i in value :
		i=i.split('-')
		i[0] = i[0].strip()
		i[1] = i[1].strip()
		res.append([i[0],i[1]])

	#returning list of ranges(also a list of length 2)
	return res


#TO DO : validate the ranges by : check if any 2 pair of range overlap or not,
# check if range lies in 0 - length_of_resource
def validate_ranges(pairs_of_ranges, lenth_of_resource):
    
	
	return True
	
 
#Compares dates, return true when date1 < date2 else false 
def compare_dates(date1, date2):
    #TO DO : complete the function
    return True


#This functions carry out the encoding passed as parameter on the body and returns the encoded body.
def Content_Encoding(response, encoding):
    
    if (encoding == 'gzip'):
        response = gzip.compress(response)
    
    elif (encoding == 'deflate'):
        response = zlib.compress(response)
        
    # print(response)
    return response

