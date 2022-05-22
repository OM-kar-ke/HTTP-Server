import socket
import sys
from threading import Thread
import threading
import os
import mimetypes
from configparser import ConfigParser
from HttpRequest import *

file='config.ini'
config=ConfigParser()
config.read(file)


Avalaible_Content_Encoding_on_server = ['gzip', 'deflate']

server_root = str(config['http']['server_root'])

#Dictionary contains Headers and their default values
headers = {    
		'Server': 'http-server',
		'Accept-Ranges': 'bytes',
		'Date' : '01/01/2000',
		'Content-Language': 'en-US'
	}


#Dictionary contains status codes
status_codes = {
		200: 'OK',
		201: 'Created',
  		202: 'Accepted',
		204: 'No Content',
		206: 'Partial Content',
  		304: 'Not Modified',
		404: 'Not Found',
		406: 'Not Acceptable',
  		412: 'Precondition Failed',
		416: 'Range Not Satisfiable',
		501: 'Not Implemented'
	}


