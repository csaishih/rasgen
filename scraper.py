import os
import cPickle
import argparse
from pymongo import MongoClient

parser = argparse.ArgumentParser()
parser.add_argument('-u', dest='flag', nargs='?', help='Generate/Update courses.dat', const='u', default='')
args = parser.parse_args()

if __name__ == '__main__':
	if (args.flag == 'u' or not os.path.isfile('courses.dat')):
		print('Generating courses.dat ...')
		try:
			os.system('python gen_data.py')
			print('OK\n')
		except Exception:
			print('FAIL\n')

	try:
		courses = cPickle.load(open('courses.dat', 'rb'))
		client = MongoClient('localhost', 27017)
		#Insert courses into MongoDB

	except IOError:
		print("Error: Cannot find courses.dat\nPlease run 'python scraper.py -u'")
