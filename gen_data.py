import requests
import cPickle
from lxml import html
from pymongo import MongoClient
from Department import Department
from Course import Course

from random import randint

#define constants
JSON_OBJECT_NAME = 'aaData'
COURSE_LINK_HEADER = 'http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId='
OFFSET_TRIM_FRONT = 72
OFFSET_TRIM_BACK = 21
OFFSET_COURSE_LINK = 27
OFFSET_LINK_LENGTH = 14
ID_DESCRIPTION = 'u32'
ID_PREREQ = 'u50'
ID_COREQ = 'u59'
ID_EXCLUSION = 'u68'
ID_RECOMMENDED_PREP = 'u77'
ID_UTSC_BREADTH = 'u104'
ID_UTM_DISTRIBUTION = 'u113'
ID_BREADTH = 'u122'
ID_APSC_ELECTIVES = 'u140'

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

def getElements(res, tag, attribute, value, text=''):
	path = '//' + tag + '[@' + attribute + '="' + value + '"]' + text
	element = html.fromstring(res.text)
	return element.xpath(path)

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

def getData(res, id):
	element = getElements(res, 'span', 'id', id, '/text()')
	if element:
		return element[0]
	else:
		return ''

def getCourse(headers, param):
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=param, headers=headers)
	try:
		courses = res.json()[JSON_OBJECT_NAME]
		course_list = []
		w = randint(0, 3)
		for i in range(w, w + 1):
			course = courses[i]
			starting_index = course[1].index('courseSearch/coursedetails/') + OFFSET_COURSE_LINK
			ending_index = starting_index + OFFSET_LINK_LENGTH

			link = COURSE_LINK_HEADER  + course[1][starting_index : ending_index]
			semester = course[6].split(' ')[1]
			semester_code = link[136]

			if semester == 'Summer' and semester_code != 'Y':
				link += semester_code

			res = requests.get(link)
			code = link[128:136]
			title = course[2].encode('ascii', 'ignore')
			credits = course[3]
			campus = course[4]
			dept = course[5]
			year = course[6].split(' ')[0]
			faculty = course[7]
			courselvl = course[9]
			description = getData(res, ID_DESCRIPTION)
			prereq = getData(res, ID_PREREQ)
			coreq = getData(res, ID_COREQ)
			exclusion = getData(res, ID_EXCLUSION)
			breadth = getData(res, ID_BREADTH)
			apsc = getData(res, ID_APSC_ELECTIVES)
			flags = 0
			course = Course(link, code, title, credits, campus, dept, year, semester, semester_code, faculty, courselvl, description, prereq, coreq, exclusion, breadth, apsc, flags)
			course_list.append(course)
			print(course)
		return course_list

	except ValueError:
		return []

def generateData():	
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')
	headers = getHeader(res)
	elements = getElements(res, 'input', 'name', 'script')
	departments = getDepartments(elements)
	params = getParams(departments)
	courses = []
	#for i in range(0, len(params)):
		#courses += getCourse(headers, params[i])
	courses += getCourse(headers, params[randint(0,97)])
	return courses
	
if __name__ == '__main__':
	data = generateData()
	#cPickle.dump(data, open('courses.dat', 'wb'))