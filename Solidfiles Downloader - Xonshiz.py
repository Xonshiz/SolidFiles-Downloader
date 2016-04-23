#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Xonshiz"

'''


Script Info :

Author : Xonshiz
Github : https://github.com/Xonshiz
Website : http://www.psychoticelites.com
Email ID: x@psychoticelites.com


-------------------------------------------------------------------------
				Info About The Latest Updated Script
-------------------------------------------------------------------------

--> Re-wrote the whole script with function calls for better work flow.
--> If the file doesn't exist, the script gives the respective error(s).
--> Slow download speed issue fixed.

There shouldn't be any BUGS, but, if there are, then please write to me at x@psychoticelites.com or open an issue on GitHub.


'''




from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import requests
from tqdm import tqdm
import time


#Link = 'http://www.solidfiles.com/v/VVWePGrGWPXBG'
#Link = 'http://www.solidfiles.com/d/d1c50f9322/'



print '-------------------------------------------------------------------'
print '                  Xonshiz SolidFiles Downloader                    '
print '-------------------------------------------------------------------'


def Link_Input():
	try:
		Link = raw_input("Please enter your Link : ")
		return Link
		if not Link:
			raise ValueError('Please Enter A Link To The Video. This Application Will now Exit in 5 Seconds.')
	except ValueError as e:
		print(e)
    	time.sleep(5)
    	exit()

	

def Link_Opener(Link):
	try:
		#opener = urllib2.build_opener()
		#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		#response = opener.open('http://www.stackoverflow.com')
		page = urllib2.urlopen(Link)
	except urllib2.HTTPError, e:
		#print e.code
		#print e.msg
		return
		exit()
	soup = BeautifulSoup(page,"lxml")
	return soup


def File_Lookup(soup):
	try:
		subtitles = soup.find_all('a',{'id':'download-btn'}) #The links were in the tag a, with 'id' as 'download-btn'
		stringsubtitles = str(subtitles)
		for link in subtitles:
			for a in subtitles:
				try:
					ddl = str(a['href'])
					if not ddl:
						raise ValueError("Seems Like I couldn't find the Download Link. Please check manually and notify Xonshiz at x@psychoticelites.com")
				except ValueError as e:
					print(e)
					time.sleep(5)
					exit()
				return ddl


		if not stringsubtitles:
			raise ValueError("Seems Like I couldn't find the Download Link. Please check manually and notify Xonshiz at x@psychoticelites.com")        
	except Exception, e:
		print(e)
		time.sleep(5)
        exit()


def Title_Lookup(soup):
	title1 = str(soup.title) #Title of the solidfile's web page
	titleclean = title1.replace('<title>','').replace('</title>','').replace(' | Solidfiles','').replace('_',' ') #Let's remove that un-needed shit
	return titleclean




def File_Downloader(ddl,titleclean):
	dlr = requests.get(ddl, stream=True) #Downloading the content using python.
	with open(titleclean, "wb") as handle:
		for data in tqdm(dlr.iter_content(chunk_size=1024)): #Added chunk size to speed up the downloads
			handle.write(data)
	print 'Download has been completed.' #Viola		





Link = Link_Input()

soup = Link_Opener(Link)
if not soup:
	print "Seems Like I couldn't find the Download Link. Please check manually and notify Xonshiz at x@psychoticelites.com"
	exit()

titleclean = Title_Lookup(soup)
ddl = File_Lookup(soup)


File_Downloader(ddl,titleclean)