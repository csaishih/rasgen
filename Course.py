class Course:
	def __init__(self, link, code, title, credits, campus, dept, year, semester, semester_code, faculty):
		self.link = 'http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId=' + str(link)
		self.code = code
		self.title = title
		self.credits = credits
		self.campus = campus
		self.dept = dept
		self.year = year
		self.semester = semester
		self.semester_code = semester_code
		self.faculty = faculty

	def __repr__(self):
		return '\nLink: ' + self.link + '\nCode: ' + self.code + '\nTitle: ' + self.title + '\nCredits: ' + self.credits + '\nCampus: ' + self.campus +  '\nDepartment: ' + self.dept + '\nYear: ' + self.year + '\nSemester: ' + self.semester + '\nSemester code: ' + self.semester_code + '\nFaculty: ' + self.faculty