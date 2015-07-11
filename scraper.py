import requests
from lxml import html
from pymongo import MongoClient
from Department import Department

#define constants
TRIM_FRONT = 72
TRIM_BACK = 21

def parseElements(element):
	starting_index = element.value.find('searchForCourseByDept') + TRIM_FRONT
	ending_index = len(element.value) - TRIM_BACK
	dept_data = element.value[starting_index : ending_index]
	dept_data = dept_data.replace(',', '')
	dept_data = dept_data.replace("' '", "|")
	dept_data = dept_data.replace("''", "|")
	return dept_data.split('|')

def getHeader(res):
	return {'Cookie':'kualiSessionId='+str(res.cookies['kualiSessionId'])+';JSESSIONID='+str(res.cookies['JSESSIONID'])}

def getElements(res):
	element = html.fromstring(res.text)
	return element.xpath('//input[@name="script"]')

def getDepartments(elements):
	dept_list = []
	for i in range(0, len(elements)):
			if 'searchForCourseByDept' in elements[i].value:
				parsed_elements = parseElements(elements[i])
				dept_list.append(Department(parsed_elements[0], parsed_elements[1], parsed_elements[2], parsed_elements[3]))
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