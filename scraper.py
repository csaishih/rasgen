import requests
from lxml import html
from pymongo import MongoClient
from Department import Department

#define constants
REMOVE_SEARCH_FOR_COURSE_BY_DEPT = 72
REMOVE_RETURN_FALSE = 21

def getHeader(res):
	return {'Cookie':'kualiSessionId='+str(res.cookies['kualiSessionId'])+';JSESSIONID='+str(res.cookies['JSESSIONID'])}

def getElements(res):
	element = html.fromstring(res.text)
	return element.xpath('//input[@name="script"]')

def getDepartments(elements):
	dept_list = []
	for i in range(0, len(elements)):
			if 'searchForCourseByDept' in elements[i].value:
				dept_data = (elements[i].value[elements[i].value.find('searchForCourseByDept') + REMOVE_SEARCH_FOR_COURSE_BY_DEPT:len(elements[i].value) - REMOVE_RETURN_FALSE]).replace(',', '').replace("' '", "|").replace("''", "|").split('|')
				dept_list.append(Department(dept_data[0], dept_data[1], dept_data[2], dept_data[3]))
	return dept_list

def getParams(departments):
	params = []
	for i in range (0, len(departments)):
		p = {'deptId': departments[i].code.strip(), 'divId': departments[i].faculty_code.strip()}	
		params.append(p)
	return params

def getCourses(headers, param):
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=param, headers=headers)
	print(res.json())

def getData():	
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')
	headers = getHeader(res)
	elements = getElements(res)
	departments = getDepartments(elements)
	params = getParams(departments)

	#for i in range(0, len(params)):
		#getCourses(headers, params[i])
	getCourses(headers, params[18])

if __name__ == '__main__':
	getData()
	client = MongoClient('localhost', 27017)