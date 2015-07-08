import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

r = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')

params = {'divId':'ARTSC', 'deptId':'CSC'}

headers = {'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'en-US,en;q=0.8','Connection':'keep-alive','Cookie':'kualiSessionId='+str(r.cookies['kualiSessionId'])+'; JSESSIONID='+str(r.cookies['JSESSIONID']),'Host':'coursefinder.utoronto.ca','Referer':'http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36','X-Requested-With':'XMLHttpRequest'}

response = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=params, headers=headers)

print(response.status_code)

