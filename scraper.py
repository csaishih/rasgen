import requests
from lxml import html
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
r = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')

tree = html.fromstring(r.text)
t = tree.xpath('//input[@name="script"]')

a = []

for i in range(0, len(t)):
	if 'searchForCourseByDept' in t[i].value:
		a.append(t[i])
		print(t[i].value)

params = {'divId':'ARTSC', 'deptId':'CSC'}
headers = {'Cookie':'kualiSessionId='+str(r.cookies['kualiSessionId'])+';JSESSIONID='+str(r.cookies['JSESSIONID'])}

res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=params, headers=headers)

#print('Status Code: ' + str(res.status_code))
#print(res.json()['aaData'][0])
