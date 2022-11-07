from datetime import datetime
import time
import hashlib
from urllib.request import urlopen, Request


class website_check():

	url = Request('https://youtube.com/',
								headers={'User-Agent': 'Mozilla/5.0'})

	# to perform a GET request and load the
	# content of the website and store it in a var
	response = urlopen(url).read()
	currentHash = hashlib.sha224(response).hexdigest()
	print("running")
	time.sleep(10)
	while True:
			try:
					# perform the get request and store it in a var
					response = urlopen(url).read()
					currentHash = hashlib.sha224(response).hexdigest()
					time.sleep(30)
					response = urlopen(url).read()
					newHash = hashlib.sha224(response).hexdigest()
					if newHash == currentHash:
							continue
					else:
							print("something changed")
							response = urlopen(url).read()
							currentHash = hashlib.sha224(response).hexdigest()
							time.sleep(30)
							continue
			except Exception as e:
					print("error")

hey = startit(3)

hey.time()