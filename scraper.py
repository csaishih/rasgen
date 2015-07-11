import requests
from lxml import html
from pymongo import MongoClient
from Department import Department

#define constants
REMOVE_SEARCH_FOR_COURSE_BY_DEPT = 72
REMOVE_RETURN_FALSE = 21

def getHeader(res):
	return {'Cookie':'kualiSessionId='+str(res.cookies['kualiSessionId'])+';JSESSIONID='+str(res.cookies['JSESSIONID'])}

def getTree(res):
	tree = html.fromstring(res.text)
	return tree.xpath('//input[@name="script"]')

def getData():	
	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start')
	headers = getHeader(res)
	tree = getTree(res)

	dept_list = []
	params = []
	for i in range(0, len(tree)):
		if 'searchForCourseByDept' in tree[i].value:
			dept_data = (tree[i].value[tree[i].value.find('searchForCourseByDept') + REMOVE_SEARCH_FOR_COURSE_BY_DEPT:len(tree[i].value) - REMOVE_RETURN_FALSE]).replace(',', '').replace("' '", "|").replace("''", "|").split('|')
			dept_list.append(Department(dept_data[0], dept_data[1], dept_data[2], dept_data[3]))
			p = {}
			p['divId'] = dept_data[0]
			p['deptId'] = dept_data[2]
			params.append(p)

	

	res = requests.get('http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/browseSearch', params=params[0], headers=headers)
	print(res.status_code)

#print('Status Code: ' + str(res.status_code))
#print(res.json()['aaData'][0])

if __name__ == '__main__':
	getData()
	client = MongoClient('localhost', 27017)