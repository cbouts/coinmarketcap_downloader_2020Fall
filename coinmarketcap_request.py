# request file is similar to what we had before, but we request the site periodically, so some things are different.
import urllib.request
import os
import ssl
# just because of the certificate verification error i have
import datetime
# for you to form timestamp so file names are differentiated
import time
# for the sleep fn

if not os.path.exists("html_files"):
	os.mkdir("html_files")


for i in range(20):
	# number in range() is the amount of observations.
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	# strftime makes it a string from time
	# %Y%m%d%H%M%S is year, month, date, hour, minute, second. it gives the format for the time stamp.
	print(current_time_stamp)
	# tells us what we're downloading in real time.
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
	# wb writes it as binary
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
	# this response and context stuff is just because of the error that I had with verifying the certificate.
	# use the html to 
	html = response.read()
	# print(html)

	f.write(html)
	f.close()
	# makes the file
	time.sleep(140)
	# irl, don't do it for only 10 seconds. it should be like at least 60 (every minute) or so.
	# also, this doesn't download exactly 10 seconds apart. downloading takes time. so this isn't the method we should use for exact time gaps.
	# want to download it multiple times, like maybe once an hour.

	# if we kept writing this for a month, we could get a very detailed history of all info on the page.
	# tom says we need to test our program because finding bugs later requires us to restart and discard prior data. 
	# so there's little room for error.
	# also, it's better to use a server than your computer bc you would need to not shut down your computer as long as the program was running.
	# sleep function is super important. for websites (rather than api), the server may not be able to block you. if you do this, it can break the server and interrupt the use of others.
	# web scraping is getting public info, but should still be careful because we don't want to break others' computers. 
	# always put in longet times than you expect to need. you can lower it if you want to later. 


