import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

params = {'divId':'ARTSC', 'deptId':'CSC'}
headers = {'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'en-US,en;q=0.8','Connection':'keep-alive','Cookie':'kualiSessionId=fc7ab2ef-ebad-48c0-9318-051277e73b8c; JSESSIONID=6C14BDCE1E08C9EE17BEA0EC0DB06995.w1','Host':'coursefinder.utoronto.ca','Referer':'http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36','X-Requested-With':'XMLHttpRequest'}

response = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=params, headers=headers)

print(response.request.headers)
print(response.status_code)
print(response.text)

#Cookie might expire, acquire new cookies
#GetALLTHECOOKIES
#NomNomNom
