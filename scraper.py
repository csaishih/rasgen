import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
r = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')
params = {'divId':'ARTSC', 'deptId':'CSC'}
headers = {'Cookie':'kualiSessionId='+str(r.cookies['kualiSessionId'])+';JSESSIONID='+str(r.cookies['JSESSIONID'])}
response = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=params, headers=headers)

print(response.status_code)

