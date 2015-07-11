import requests
from lxml import html
from pymongo import MongoClient
from Department import Department
from Course import Course

#define constants
JSON_OBJECT_NAME = "aaData"
OFFSET_TRIM_FRONT = 72
OFFSET_TRIM_BACK = 21
OFFSET_COURSE_LINK = 27
OFFSET_LINK_LENGTH = 14

def parseElements(element):
	starting_index = element.value.index('searchForCourseByDept') + OFFSET_TRIM_FRONT
	ending_index = len(element.value) - OFFSET_TRIM_BACK
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

def getCourse(headers, param):
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=param, headers=headers)
	try:
		courses = res.json()[JSON_OBJECT_NAME]	
		for i in range(0, len(courses)):
			course = courses[i]
			starting_index = course[1].index('courseSearch/coursedetails/') + OFFSET_COURSE_LINK
			ending_index = starting_index + OFFSET_LINK_LENGTH

			link = course[1][starting_index : ending_index]
			code = link[:8]
			title = course[2].encode('ascii', 'ignore')
			credits = course[3]
			campus = course[4]
			dept = course[5]
			year = course[6].split(' ')[0]
			semester = course[6].split(' ')[1]
			semester_code = link[8]
			faculty = course[7]

			print(Course(link, code, title, credits, campus, dept, year, semester, semester_code, faculty))
			print('\n')
			
	except ValueError:
		pass


def getData():	
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')
	headers = getHeader(res)
	elements = getElements(res)
	departments = getDepartments(elements)
	params = getParams(departments)
	for i in range(0, len(params)):
		getCourse(headers, params[i])

if __name__ == '__main__':
	getData()
	client = MongoClient('localhost', 27017)
