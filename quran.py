import requests
from bs4 import BeautifulSoup
import urllib2
import re
import subprocess
import wget


r = requests.get("http://quranicaudio.com/")

soup = BeautifulSoup(r.content, "lxml")

soup.prettify()
soup.find_all("a")
for link in soup.find_all("a"):
    "<a href = '%s'> %s </a>" % (link.get("href"), link.text)


myList = [link.get("href") for link in soup.find_all("a")]
URL=urllib2.urlopen('http://quranicaudio.com/' + str(link.get("href"))+'/')
choice = raw_input("Enter the Recitor's URL:")

'''
if choice in myList:
filename = wget.download(url)
 '''

url = 'http://quranicaudio.com/quran/108'
filename = wget.download(url, link.text)










