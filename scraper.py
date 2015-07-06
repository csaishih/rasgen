import urllib2
from pymongo import MongoClient

f = urllib2.urlopen('http://coursefinder.utoronto.ca/')
client = MongoClient()
client = MongoClient('localhost', 27017)